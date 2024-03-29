# -*- coding: utf-8 -*-
{
    'name': "CRM Extends",
    'author': "Xetechs GT",
    'website': "http://www.xetechs.com",
    'support': 'Jonathan Quintero --> jquintero@xetechs.com',
    "version": "15.0.1.1.0",

    'depends': [
        'sale', 
        'purchase',
        'crm'
    ],
    'data': [
        'views/crm_lead_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
