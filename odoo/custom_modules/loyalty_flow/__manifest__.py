{
    "name": "Stakely Flow Integration",
    "version": "1.0",
    "author": "TokenCraft",
    "category": "Loyalty",
    "summary": "Integrate Flow blockchain with Odoo Loyalty",
    "depends": ["loyalty", "point_of_sale"],
    # "data": [],
    "data": [
        'views/loyalty_program_views.xml',
    ],
    "installable": True,
    "application": True,
}