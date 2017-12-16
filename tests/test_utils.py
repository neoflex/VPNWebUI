# coding=utf-8
from expressvpn_web import get_list_of_servers
from tests import BaseTest

__author__ = 'Valentin Grouès'


class TestUtils(BaseTest):
    def test_parse_list(self):
        servers = get_list_of_servers()
        self.assertEquals(143, len(servers))
