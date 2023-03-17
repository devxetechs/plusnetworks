# -*- coding: utf-8 -*-
{
    'name': 'Partner Extends',
    'version': '15.0.0.1',
    'author': "Xetechs, S.A.",
    'website': 'https:/www.xetechs.com',
    'support': 'Jonathan Quintero --> jquintero@xetechs.com',
    'sequence': 1,
    'license':'OPL-1',
    'depends': [
        'base',
        'contacts',
        'helpdesk',
        'helpdesk_timesheet',
        'hr'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_country_region_views.xml',
        'views/res_country_municipality_views.xml',
        'views/res_partner_views.xml',
        'views/hr_employee_views.xml',
        'views/helpdesk_ticket_views.xml',
        'data/municipality_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}