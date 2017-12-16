# coding=utf-8
__author__ = 'Valentin Grouès'


class Config(object):
    SECRET_KEY = ''
    TITLE = 'ExpressVPNWeb'
    EXPRESSVPNCMD = 'expressvpn'
    EXPRESSVPNCMD_LIST = EXPRESSVPNCMD + ' list'
    EXPRESSVPNCMD_DISCONNECT = EXPRESSVPNCMD + ' disconnect'
    EXPRESSVPNCMD_CONNECT = EXPRESSVPNCMD + ' connect {}'
    EXPRESSVPNCMD_STATUS = EXPRESSVPNCMD + ' status'
    EXPRESSVPNCMD_DIAGNOSTICS = EXPRESSVPNCMD + ' diagnostics'
    EXPRESSVPNCMD_DISCONNECT = EXPRESSVPNCMD + ' disconnect'


class DevConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True


class TestConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True
    TESTING = True
