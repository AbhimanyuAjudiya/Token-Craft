{
    'name': 'Loyalty Flow Program',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Blockchain-inspired token system for Odoo POS',
    'depends': ['loyalty_program', 'point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/loyalty_program_views.xml',
        'views/pos_config_views.xml', 
        'views/pos_templates.xml',
        'data/loyalty_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}