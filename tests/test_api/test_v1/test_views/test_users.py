#!/usr/bin/python3
"""
testing users api
"""
from api.v1.app import app
from api.v1.views import *
import unittest
from models import storage
from models.user import User


class MyusersAPITestCase(unittest.TestCase):
    def setUp(self):
        """ Create a test client """
        self.app = app.test_client()
        self.app.testing = True

    def test_get_users(self):
        """ 
        Get users
        """
        user = User({'name': 'person1',
                    'email': "haha@haha.com",
                     'password': "verySecret"})
        user.save()
        response = self.app.get('/api/v1/users')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_get_user(self):
        """ 
        Get a user object
        """
        user = User({'name': 'person1',
                    'email': "haha@haha.com",
                     'password': "verySecret"})
        user.save()
        response = self.app.get(f'/api/v1/users/{user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_post_data(self):
        """
        Send a POST request that creates data
        """
        data = {'name': 'person1',
                'email': "haha@haha.com",
                'password': "verySecret"}
        response = self.app.post('/api/v1/users', json=data)
        self.assertEqual(response.status_code, 201)

    def test_delete_data(self):
        """
        Send a DELETE request that deletes data
        """
        data = {'name': 'person1',
                'email': "haha@haha.com",
                'password': "verySecret"}
        user = User(**data)
        user.save()
        response = self.app.get(f'/api/v1/users/{user.id}')
        self.assertEqual(response.status_code, 200)
        response = self.app.delete(f'/api/v1/users/{user.id}')
        self.assertEqual(response.status_code, 200)
        response = self.app.get(f'/api/v1/users/{user.id}')
        self.assertEqual(response.status_code, 404)

    def test_put_data(self):
        """
        Send a PUT request that updates data
        """
        data = {'name': 'person1',
                'email': "haha@haha.com",
                'password': "verySecret"}
        user = User(**data)
        user.save()
        response = self.app.put(f'/api/v1/users/{user.id}',
                                json={'name': 'person2'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.json['name'], 'person2')
