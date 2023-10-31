#!/usr/bin/python3
"""
test the app in api
"""
from api.v1.app import app
from api.v1.views import *
import unittest


class MyAPITestCase(unittest.TestCase):
    def setUp(self):
        """ Create a test client """
        self.app = app.test_client()
        self.app.testing = True

    def test_blueprint_connection(self):
        """
        Send a GET request to a route defined in the blueprint
        """
        response = self.app.get('/api/v1/status')
        self.assertEqual(response.status_code, 200)

    def test_cors_acceptance(self):
        """
        Set the request headers to simulate a request from IP 0.0.0.0
        """
        headers = {'Origin': 'http://0.0.0.0'}
        response = self.app.get('/api/v1/status', headers=headers)
        self.assertEqual(response.status_code, 200)
