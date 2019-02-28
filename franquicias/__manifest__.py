# -*- coding: utf-8 -*-
{
    'name': "franquicias",

    'summary': """
        Modulo destinado a la administracion de distintas franquicias, incluyendo sus tiendas y empleados.""",

    'description': """
        Modulo destinado a la administracion de distintas franquicias, incluyendo sus tiendas y empleados.
    """,

    'author': "Pablo Ruiz Cuevas",
    'website': "http://www.franquicias.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
