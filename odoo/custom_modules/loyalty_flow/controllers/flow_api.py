from odoo import http
from odoo.http import request
import json
import logging
from .ai_service import DiscountAI  # Assuming you have an AI service for discounts

_logger = logging.getLogger(__name__)

class FlowAPIController(http.Controller):
    
    # --------------------------------------------
    # 1. Mint Tokens (Triggered after purchase)
    # --------------------------------------------
    @http.route('/api/mint_tokens', type='json', auth='public', methods=['POST'], csrf=False)
    def mint_tokens(self, **kwargs):
        try:
            data = json.loads(request.httprequest.data)
            customer_address = data.get('customer_address')
            is_new_customer = data.get('is_new_customer', False)  # New parameter
            total_purchases = data.get('total_purchases', 0)  # New parameter
            
            if not customer_address:
                return {"error": "Missing customer_address"}, 400
            
            # Get the loyalty program model
            loyalty_program = request.env['loyalty.program'].sudo().search([], limit=1)
            
            # Predict the number of tokens to issue using AI
            customer_data = {
                'is_new_customer': is_new_customer,
                'total_purchases': total_purchases,
            }
            tokens_to_issue = loyalty_program.predict_tokens(customer_data)
            
            # Get Flow service from model
            flow_service = loyalty_program.get_flow_service()
            
            # Call Flow SDK to mint tokens
            tx_result = flow_service.mint_tokens(customer_address, tokens_to_issue)
            
            return {
                "status": "success",
                "transaction_id": tx_result['txId'],
                "balance": tx_result['balance'],
                "tokens_issued": tokens_to_issue  # Return the number of tokens issued
            }
            
        except Exception as e:
            _logger.error(f"FlowAPI Mint Error: {str(e)}")
            return {"error": str(e)}, 500

    # --------------------------------------------
    # 2. Stake Tokens (Customer action)
    # --------------------------------------------
    @http.route('/api/stake_tokens', type='json', auth='public', methods=['POST'])
    def stake_tokens(self, **kwargs):
        try:
            data = json.loads(request.httprequest.data)
            customer_address = data.get('customer_address')
            amount = data.get('amount')
            
            flow_service = request.env['loyalty.program'].sudo().get_flow_service()
            stake_result = flow_service.stake_tokens(customer_address, amount)
            
            return {
                "status": "success",
                "staked_amount": amount,
                "discount_tier": stake_result['discount_tier']  # e.g., "tier_1"
            }
            
        except Exception as e:
            return {"error": str(e)}, 500

    # --------------------------------------------
    # 3. Get Token Balance (For React dashboard)
    # --------------------------------------------
    @http.route('/api/token_balance', type='json', auth='public', methods=['GET'])
    def get_token_balance(self, customer_address, **kwargs):
        try:
            flow_service = request.env['loyalty.program'].sudo().get_flow_service()
            balance = flow_service.get_balance(customer_address)
            
            return {
                "balance": balance,
                "address": customer_address
            }
            
        except Exception as e:
            return {"error": str(e)}, 500
        
@http.route('/api/test_ai_predictions', type='json', auth='public', methods=['POST'])
def test_ai_predictions(self, **kwargs):
    try:
        loyalty_program = request.env['loyalty.program'].sudo().search([], limit=1)
        loyalty_program.test_ai_predictions()
        return {"status": "success", "message": "AI predictions tested successfully"}
    except Exception as e:
        return {"error": str(e)}, 500