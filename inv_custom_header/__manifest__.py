# -*- coding: utf-8 -*-
{
    'name': "Custom PDF Header",
    'summary': """Custom header for PDF reports with company information and services""",
    'description': """
        This module customizes the PDF header (web.external_layout_striped) to display:
        * Company logo
        * Company information (name, address)
        * Company services
        
        The header will show a professional layout with company details and services list.
    """,
    'author': "Metraco",
    'website': 'http://www.karizma-conseil.com',
    'category': 'Reporting',
    'version': '18.0.1.0.0',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'security/security.xml',
        'views/res_company_views.xml',
        'reports/external_layout_striped.xml',
        'reports/rapport_v14.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
