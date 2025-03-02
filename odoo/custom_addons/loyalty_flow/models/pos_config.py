from odoo import models, fields

class PosConfig(models.Model):
    _inherit = 'pos.config'

    loyalty_flow_program_id = fields.Many2one(
        'loyalty.program',
        string='Flow Loyalty Program',
        help="Link Flow Token Program to POS"
    )