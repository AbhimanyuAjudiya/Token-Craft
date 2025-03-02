# # from odoo import models

# # class LoyaltyProgram(models.Model):
# #     _inherit = 'loyalty.program'
    
# #     def get_flow_service(self):
# #         # Initialize Flow SDK connection
# #         from .flow_service import FlowService
# #         return FlowService()  # Reuse existing Flow emulator config

# import pandas as pd
# from sklearn.ensemble import RandomForestRegressor
# from odoo import models, fields, api

# class LoyaltyProgram(models.Model):
#     _inherit = 'loyalty.program'

#     flow_token_balance = fields.Float(string="Flow Token Balance", default=0.0)
#     flow_account_id = fields.Char(string="Flow Account ID")

#     def get_flow_service(self):
#         """
#         Initialize and return the FlowService instance from flow_service.py.
#         """
#         from .flow_service import FlowService
#         return FlowService()  # Reuse existing FlowService class

#     def predict_tokens(self, customer_data):
#         """
#         Predict the number of tokens to issue based on customer behavior using AI.
#         :param customer_data: Dictionary containing customer behavior data (e.g., is_new_customer, total_purchases, etc.)
#         :return: Predicted number of tokens
#         """
#         # Example training data (replace with real data from your Odoo database)
#         training_data = [
#             {'is_new_customer': 1, 'total_purchases': 100, 'tokens_issued': 100},
#             {'is_new_customer': 0, 'total_purchases': 500, 'tokens_issued': 50},
#             {'is_new_customer': 1, 'total_purchases': 200, 'tokens_issued': 150},
#             {'is_new_customer': 0, 'total_purchases': 300, 'tokens_issued': 75},
#         ]

#         # Convert training data to DataFrame
#         df = pd.DataFrame(training_data)

#         # Features (X) and target (y)
#         X = df[['is_new_customer', 'total_purchases']]
#         y = df['tokens_issued']

#         # Train a RandomForestRegressor model
#         model = RandomForestRegressor()
#         model.fit(X, y)

#         # Predict tokens for the given customer data
#         predicted_tokens = model.predict([[customer_data['is_new_customer'], customer_data['total_purchases']]])
#         return int(predicted_tokens[0])

#     def issue_tokens(self, customer_id, is_new_customer, total_purchases):
#         """
#         Issue tokens based on AI prediction.
#         """
#         # Get the FlowService instance
#         flow_service = self.get_flow_service()

#         # Prepare customer data for prediction
#         customer_data = {
#             'is_new_customer': 1 if is_new_customer else 0,
#             'total_purchases': total_purchases,
#         }

#         # Predict tokens using AI
#         tokens_to_issue = self.predict_tokens(customer_data)

#         # Mint tokens on the Flow blockchain using the existing FlowService
#         flow_service.mint_tokens(self.flow_account_id, tokens_to_issue)
#         self.flow_token_balance += tokens_to_issue

#     def sync_balance(self):
#         """
#         Sync token balance with the Flow blockchain.
#         """
#         # Get the FlowService instance
#         flow_service = self.get_flow_service()

#         # Query token balance from the Flow blockchain
#         balance = flow_service.get_balance(self.flow_account_id)
#         self.flow_token_balance = balance

from odoo import models, fields, api

class LoyaltyProgram(models.Model):
    _inherit = 'loyalty.program'

    flow_token_balance = fields.Float(string="Flow Token Balance", default=0.0)
    flow_account_id = fields.Char(string="Flow Account ID")

    def get_flow_service(self):
        """
        Initialize and return the FlowService instance from flow_service.py.
        """
        from .flow_service import FlowService
        return FlowService()  # Reuse existing FlowService class

    def predict_tokens(self, customer_data):
        """
        Predict the number of tokens to issue based on customer behavior.
        :param customer_data: Dictionary containing customer behavior data (e.g., is_new_customer, total_purchases, etc.)
        :return: Predicted number of tokens
        """
        # Simple logic for token prediction (replace with AI logic later)
        is_new_customer = customer_data.get('is_new_customer', False)
        total_purchases = customer_data.get('total_purchases', 0)

        if is_new_customer:
            return 100  # New customers get 100 tokens
        else:
            if total_purchases > 400:
                return 50  # Recurring customers with high purchases get 50 tokens
            else:
                return 75  # Recurring customers with medium purchases get 75 tokens

    def issue_tokens(self, customer_id, is_new_customer, total_purchases):
        """
        Issue tokens based on simple prediction logic.
        """
        # Get the FlowService instance
        flow_service = self.get_flow_service()

        # Prepare customer data for prediction
        customer_data = {
            'is_new_customer': is_new_customer,
            'total_purchases': total_purchases,
        }

        # Predict tokens using simple logic
        tokens_to_issue = self.predict_tokens(customer_data)

        # Mint tokens on the Flow blockchain using the existing FlowService
        flow_service.mint_tokens(self.flow_account_id, tokens_to_issue)
        self.flow_token_balance += tokens_to_issue

    def sync_balance(self):
        """
        Sync token balance with the Flow blockchain.
        """
        # Get the FlowService instance
        flow_service = self.get_flow_service()

        # Query token balance from the Flow blockchain
        balance = flow_service.get_balance(self.flow_account_id)
        self.flow_token_balance = balance