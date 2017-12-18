# coding=utf-8
import subprocess

from flask import render_template, redirect, url_for, flash

from expressvpn_web import app, servers

__author__ = 'Valentin Grouès'


@app.route('/vpn')
def servers_list():
    #expressvpn_cmd_status = app.config.get('EXPRESSVPNCMD_STATUS', 'expressvpn status')
    #status = subprocess.check_output(expressvpn_cmd_status, shell=True).decode('utf-8')
    return render_template('servers.html', servers=servers, status='connected')


@app.route('/vpn/connect/<code>')
def connect(code):
    expressvpn_cmd_disconnect = app.config.get('EXPRESSVPNCMD_DISCONNECT', 'expressvpn disconnect')
    expressvpn_cmd_connect = app.config.get('EXPRESSVPNCMD_CONNECT', 'expressvpn connect {}').format(code)
    expressvpn_cmd_status = app.config.get('EXPRESSVPNCMD_STATUS', 'expressvpn status')
    try:
        subprocess.check_output(expressvpn_cmd_disconnect, shell=True).decode('utf-8')
    except subprocess.CalledProcessError:
        pass
    result = subprocess.check_output(expressvpn_cmd_connect, shell=True).decode('utf-8')
    status = subprocess.check_output(expressvpn_cmd_status, shell=True).decode('utf-8')
    flash(status, 'success')
    return redirect(url_for("servers_list"))


@app.route('/vpn/ban/<index>')
def ban(index):
    index = int(index)
    code, country, location, banned = servers[index]
    servers[index] = (code, country, location, not banned)
    return redirect(url_for("servers_list"))


@app.route('/vpn/disconnect')
def disconnect():
    expressvpn_cmd_disconnect = app.config.get('EXPRESSVPNCMD_DISCONNECT', 'expressvpn disconnect')
    result = subprocess.check_output(expressvpn_cmd_disconnect, shell=True).decode('utf-8')
    flash(result, 'success')
    return redirect(url_for("servers_list"))


@app.route('/vpn/diagnostics')
def diagnostics():
    expressvpn_cmd_diagnostics = app.config.get('EXPRESSVPNCMD_DIAGNOSTICS', 'expressvpn diagnostics')
    expressvpn_cmd_status = app.config.get('EXPRESSVPNCMD_STATUS', 'expressvpn status')
    diagnostics = subprocess.check_output(expressvpn_cmd_diagnostics, shell=True).decode('utf-8')
    status = subprocess.check_output(expressvpn_cmd_status, shell=True).decode('utf-8')
    return render_template("diagnostics.html", status=status, diagnostics=diagnostics)
