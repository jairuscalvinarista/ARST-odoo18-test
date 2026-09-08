# -*- coding: utf-8 -*-
{
    'name': "ARISTA | Custom Enterprise Login Layout",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Jairus Calvin",
    'website': "https://arista-group.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Custom Enterprise Login Layout',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web', 'web_enterprise'],

    # always loaded
    'data': [
        # 'views/login_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'arst_login_layout/static/src/scss/custom_style.scss',
        ],
        'web.assets_backend': [
            'arst_login_layout/static/src/scss/custom_style.scss',
        ],
    },
}

