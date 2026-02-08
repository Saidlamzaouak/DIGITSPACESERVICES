# -*- coding: utf-8 -*-
{
    'name': "Amount Letter in Reports",
    'summary': """Display amount in letters on invoice and sale order PDF reports""",
    'description': """
        This module adds the amount in letters (amount_letter) field to:
        * Invoice reports (account.move)
        * Sale order reports (sale.order)
        
        The amount is displayed in French letters on the PDF reports.
    """,
    'author': "Metraco",
    'website': 'http://www.karizma-conseil.com',
    'category': 'Accounting/Sales',
    'version': '18.0.1.0.0',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'account',
        'sale',
    ],
    'data': [
        'security/security.xml',
        'reports/invoice_report.xml',
        'reports/sale_order_report.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
