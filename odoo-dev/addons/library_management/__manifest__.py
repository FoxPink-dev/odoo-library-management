{
    'name': "Library Management",
    'summary': "Manage books in your library",
    'description': """
        Simple library management module for learning Odoo development.
        Manage books, authors, and track availability.
    """,
    'author': "Vibecode Dev",
    'website': "https://github.com/vibecode-dev/odoo-library-management",
    'category': 'Knowledge',
    'version': '1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
}
