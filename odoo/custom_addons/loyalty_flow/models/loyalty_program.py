from odoo import models, fields

class LoyaltyProgram(models.Model):
    _inherit = 'loyalty.program'

    allow_flow = fields.Boolean('Enable Flow Tokens')
    flow_points = fields.Integer('Flow Tokens', default=0)
    flow_tier_ids = fields.One2many('loyalty.flow.tier', 'program_id', string='Flow Tiers')

class LoyaltyFlowTier(models.Model):
    _name = 'loyalty.flow.tier'
    _description = 'Flow Reward Tiers'  # Required in Odoo 18
    
    program_id = fields.Many2one('loyalty.program')
    flow_points_required = fields.Integer('Required Flow Tokens')
    discount_percent = fields.Float('Discount (%)')