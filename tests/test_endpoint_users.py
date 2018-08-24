from unittest import TestCase
from api import create_app
import json


class BaseTestCase(TestCase):
    def setUp(self):
        self.app = create_app()
        self.test_client = self.app.test_client()

        
        self.sign_up = {
            'username': 'jack',
            'email': 'ben@gmail.com',
            'password': 'yubw'
        }

        self.login_credentials = {            
            "username" : "jack",
            "password" : "yubw"           
            } 

        self.test_client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.sign_up),
            content_type='application/json')

        self.test_login = self.test_client.post(
            '/api/v1/auth/login',
            data=json.dumps(self.login_credentials),
            content_type='application/json')

        self.test_data = {
            'username': 'jacky',
            'email': 'blue@gmail.com',
            'password': 'wooi'
        }

        self.test_answer = {
            "answer_details": "It is a simple way of creating a list"
        }

        self.blank_answer = {
            "answer_details": ""
        }


    
    def tearDown(self):
        pass

class TestUsers(BaseTestCase):
    
    
    def test_register_user(self):
        # test if user can be registered

        result = self.test_client.post(
            'api/v1/auth/signup',
            data=json.dumps(self.test_data),
            content_type='application/json')

        self.assertEqual(result.status_code, 200)

    def test_user_login(self):
        result = self.test_client.post(
            'api/v1/auth/login',
            data=json.dumps(self.login_credentials),
            content_type='application/json')

        self.assertEqual(result.status_code, 200)  