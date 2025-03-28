{
    'name': 'Update Phone Information in Web',
    'description': 'This module will make unique phone when update information in web',
    'author': 'Ivan, PT Layani Solusi Indonesia',
    'license': 'LGPL-3',
    'version': '18.0.1.0.0',
    'depends': ['layani_user_by_phone','base', 'web', 'portal'],
    'assets': {
        'web.assets_frontend': [
            'layani_user_by_phone/static/src/css/signup.css',
        ],
    },
    'data': [
        'views/portal_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
