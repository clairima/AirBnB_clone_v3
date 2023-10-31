#!/usr/bin/python3
"""
testing cities api
"""
from api.v1.app import app
from api.v1.views import *
import unittest
from models import storage
from models.state import State
from models.city import City


class MyCitiesAPITestCase(unittest.TestCase):
    def setUp(self):
        """ Create a test client """
        self.app = app.test_client()
        self.app.testing = True

    def test_get_cities_state(self):
        """
        Get cities for a state
        """
        state = State({'name': 'California'})
        state.save()
        city = City({'name': "here", 'state_id': state.id})
        city.save()
        response = self.app.get(f'/api/v1/states/{state.id}/cities')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_get_city(self):
        """
        Get a city object
        """
        state = State({'name': 'California'})
        state.save()
        city = City({'name': "here", 'state_id': state.id})
        city.save()
        response = self.app.get(f'/api/v1/cities/{city.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_post_data(self):
        """
        Send a POST request that creates data
        """
        state = State({'name': 'California'})
        state.save()
        response = self.app.post(f'/api/v1/states/{state.id}/cities',
                                 json={'name': 'Cairo'})
        self.assertEqual(response.status_code, 201)

    def test_delete_data(self):
        """
        Send a DELETE request that deletes data
        """
        state = State({'name': 'California'})
        state.save()
        city = City({'name': "here", 'state_id': state.id})
        city.save()
        response = self.app.get(f'/api/v1/cities/{city.id}')
        self.assertEqual(response.status_code, 200)
        response = self.app.delete(f'/api/v1/cities/{city.id}')
        self.assertEqual(response.status_code, 200)
        response = self.app.get(f'/api/v1/cities/{city.id}')
        self.assertEqual(response.status_code, 404)

    def test_put_data(self):
        """
        Send a PUT request that updates data
        """
        state = State({'name': 'California'})
        state.save()
        city = City({'name': "here", 'state_id': state.id})
        city.save()
        response = self.app.put(f'/api/v1/cities/{city.id}',
                                json={'name': 'Cairo'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.json['name'], 'Cairo')
