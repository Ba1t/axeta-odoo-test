# -*- coding: utf-8 -*-
{
    'name': "simpletask",

    'category': 'Test',
    'author': "Voronin Yuriy",
    'version': '0.1',

    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/templates.xml',
        'views/simpletask.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'summary': """Simple task module""",

    'description': """
        Module for managing tasks from users:
            - create new task
            - view tasks
    """,
}