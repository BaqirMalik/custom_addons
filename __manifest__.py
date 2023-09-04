# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Student Management System",
    'version': '16.0.0',
    'category': '',
    'description': """This module helps to manage student and cources""",
    'author': 'Odoo Gates',
    'company': 'Odoo Gates',
    'maintainer': 'Odoo',
    'website': 'https://www.odoogates.com',
    'depends': ['base','mail'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
    'data':[
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/menu.xml',
    ]
}
