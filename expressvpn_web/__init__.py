# coding=utf-8
import csv
import os
from logging import warning

from flask import Flask
from flask_assets import Environment
from webassets.loaders import PythonLoader as PythonAssetsLoader
import subprocess
import socket

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
    if app.config.get('EXPRESSVPN'):
        cmd_list = app.config.get('EXPRESSVPNCMD_LIST', 'expressvpn list')
    else:
        cmd_list = app.config.get('NORDVPN_LIST', 'cd /etc/openvpn/ovpn_udp/ && ls -1')

    result = subprocess.check_output(cmd_list, shell=True).decode('utf-8')
    csv_reader = csv.reader(result.split('\n')[2:], delimiter='\t')
    country = ""

    print('Here')

    if app.config.get('EXPRESSVPN'):
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
    else:
        for row in csv_reader:
            if not row:
                continue
            code = row[0]
            results.append((code, 'US', 'NA', False))
    return results


def connect_management_interface():
    host = app.config.get('MANAGEMENT_IP', '127.0.0.1')
    port = int(app.config.get('MANAGEMENT_PORT', '5000'))
    password = app.config.get('MANAGEMENT_PASS', 'vpn')

    s = False
    try:
        if s:
            return s
        s = socket.create_connection((host, port), 3)

        # authenticate
        vpnauth = False
        #s.send(password.encode())

        while 1:
            sdata = s.recv(1024).decode('utf-8')
            if 'OpenVPN Management Interface Version' in sdata:
                # nothing on the socket anymore
                vpnauth = True
                break

    except socket.timeout as e:
        warning('socket timeout: {0!s}'.format(e))
        if s:
            s.shutdown(socket.SHUT_RDWR)
            s.close()
    except Exception as e:
        warning('unexpected error: {0!s}'.format(e))
    return s


app = create_application()
servers = get_list_of_servers()
mgmtinterface = connect_management_interface()

assets_env = Environment(app)
assets_loader = PythonAssetsLoader(assets)
for name, bundle in assets_loader.load_bundles().items():
    assets_env.register(name, bundle)
from .controllers import *
