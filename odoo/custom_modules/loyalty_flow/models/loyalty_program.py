from odoo import models

class LoyaltyProgram(models.Model):
    _inherit = 'loyalty.program'
    
    def get_flow_service(self):
        # Initialize Flow SDK connection
        from .flow_service import FlowService
        return FlowService()  # Reuse existing Flow emulator config