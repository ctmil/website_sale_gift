# -*- coding: utf-8 -*-
{
    'name': "Website Sale Gift",

    'summary': """
        Website Sale Gift""",

    'description': """
        Website Sale Gift
    """,

    'author': "Codize, Moldeo Interactive",
    'website': "https://www.codize.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_sale', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}