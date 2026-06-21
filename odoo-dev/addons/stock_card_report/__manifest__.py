{
    'name': "Enhanced Stock Card Report",
    'summary': "Detailed stock card with valuation, multi-warehouse and export",
    'description': """
        Enhanced Stock Card Report for Odoo Community Edition.
        Features: multi-warehouse, date range filter, running balance,
        valuation columns, PDF export, Excel export, chart view.
        Works with Odoo 18.0 and 19.0 Community Edition.
    """,
    'author': "FoxPink",
    'website': "https://github.com/FoxPink-dev",
    'category': 'Inventory/Reporting',
    'version': '19.0.1.0.0',
    'depends': ['stock', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/stock_card_wizard_views.xml',
        'views/stock_card_report_views.xml',
        'report/stock_card_report_templates.xml',
        'report/stock_card_report_reports.xml',
    ],
    'images': ['images/main_screenshot.png'],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
