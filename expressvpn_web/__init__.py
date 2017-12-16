# coding=utf-8
import csv
import os

from flask import Flask
from flask_assets import Environment
from webassets.loaders import PythonLoader as PythonAssetsLoader
import subprocess

import expressvpn_web.assets as assets

__author__ = 'Valentin Grouès'


def create_application():
    new_app = Flask(__name__, static_url_path="/static")
    env = os.environ.get('VPN_ENV', 'dev')  # will default to dev env if no var exported
    new_app.config.from_object('expressvpn_web.settings.%sConfig' % env.capitalize())
    new_app.config['ENV'] = env
    new_app.jinja_env.add_extension('jinja2.ext.i18n')

    return new_app


def get_list_of_servers():
    results = []
    expressvpn_cmd_list = app.config.get('EXPRESSVPNCMD_LIST', 'expressvpn list')
    result = subprocess.check_output(expressvpn_cmd_list, shell=True).decode('utf-8')
    csv_reader = csv.reader(result.split('\n')[2:], delimiter='\t')
    country = ""
    for row in csv_reader:
        if not row:
            continue
        code = row[0]
        country = row[1] or country
        location = row[5]
        if not location and len(row) > 4:
            location = row[4]
        if not location and len(row) > 6:
            location = row[6]
        if not location and len(row) > 3:
            location = row[3]
        if not location and len(row) > 2:
            location = row[2]
        results.append((code, country, location, False))
    return results


app = create_application()
servers = get_list_of_servers()

assets_env = Environment(app)
assets_loader = PythonAssetsLoader(assets)
for name, bundle in assets_loader.load_bundles().items():
    assets_env.register(name, bundle)
from .controllers import *
