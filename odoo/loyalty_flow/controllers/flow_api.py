# File: loyalty_flow/controllers/flow_api.py
from odoo import http
from odoo.http import request
import json
import logging

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
            amount = data.get('amount')
            
            if not customer_address or not amount:
                return {"error": "Missing parameters"}, 400
            
            # Get Flow service from model
            flow_service = request.env['loyalty.program'].sudo().get_flow_service()
            
            # Call Flow SDK to mint tokens
            tx_result = flow_service.mint_tokens(customer_address, amount)
            
            return {
                "status": "success",
                "transaction_id": tx_result['txId'],
                "balance": tx_result['balance']
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