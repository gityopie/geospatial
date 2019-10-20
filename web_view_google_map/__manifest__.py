# Copyright (C) 2019, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'View Google Maps',
    'version': '12.0.1.0.0',
    'author': 'Open Source Integrators, Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/geospatial',
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'description': """
View Google Map
===============

Allows user to view partners (or any model contains geolocation) location 
on google maps.
""",
    'depends': [
        'base_setup',
        'base_geolocalize',
    ],
    'data': [
        'views/google_places_template.xml',
        'views/res_config_settings.xml'
    ],
    'demo': [],
    'images': ['static/description/thumbnails.png'],
    'qweb': ['static/src/xml/widget_places.xml'],
    'installable': True,
    'uninstall_hook': 'uninstall_hook',
    'maintainers': [
        'gityopie',
        'wolfhall'
    ],
}
