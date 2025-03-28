{
    'name': 'Layani Action Generate QR Ewallet',
    'description': 'This module will generate Ewallet QR when checked',
    'author' : 'Ivan, PT Layani Solusi Indonesia',
    'license' : 'LGPL-3',
    'version' : '18.0.1.0.0', 
    'depends': ['loyalty','web'],
    'data': [
        'report/loyalty_report.xml',  
        'report/loyalty_report_templates.xml', 
     ],
     'installable': True,
     'application': False,
     'auto_install': False
}