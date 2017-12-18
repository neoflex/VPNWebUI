# coding=utf-8
__author__ = 'Valentin Grouès'


class Config(object):
    SECRET_KEY = ''
    TITLE = 'ExpressVPNWeb'
    EXPRESSVPN = False
    EXPRESSVPNCMD = 'expressvpn'
    EXPRESSVPNCMD_LIST = EXPRESSVPNCMD + ' list'
    EXPRESSVPNCMD_DISCONNECT = EXPRESSVPNCMD + ' disconnect'
    EXPRESSVPNCMD_CONNECT = EXPRESSVPNCMD + ' connect {}'
    EXPRESSVPNCMD_STATUS = EXPRESSVPNCMD + ' status'
    EXPRESSVPNCMD_DIAGNOSTICS = EXPRESSVPNCMD + ' diagnostics'
    EXPRESSVPNCMD_DISCONNECT = EXPRESSVPNCMD + ' disconnect'
    NORDVPN_LIST = 'cd /Users/christophe.trefois/dev/github/VPNWebUI/downloads/ovpn_udp && ls -1 us*'
    MANAGEMENT_IP = '192.168.178.56'
    MANAGEMENT_PORT = '23000'
    MANAGEMENT_PASS = 'vpn'


class DevConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True


class TestConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True
    TESTING = True
