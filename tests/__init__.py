# coding=utf-8
import os

from expressvpn_web import app

__author__ = 'Valentin Grouès'

from flask_testing import TestCase


def get_resource_path(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', filename)


class BaseTest(TestCase):
    def create_app(self):
        app.config.from_object('expressvpn_web.settings.TestConfig')
        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass

