# -*- coding: utf-8 -*-
{
    'name': "Simpletask",

    'category': 'Test',
    'author': 'Voronin Yuriy',
    'website': 'https://github.com/Ba1t/axeta-odoo-test',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/templates.xml',
        'views/simpletask.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],

    'summary': """Test task for "Axeta" """,

    'description': """
        Module for managing tasks from users:
            - create new task
            - edit existed task
            - view all tasks (list, form)
    """,
}