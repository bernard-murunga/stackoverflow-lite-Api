from unittest import TestCase
from app import create_app
import json
from api.resources.questions import questions_dictionary
from api.resources.answers import answers_dictionary


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
            'question_title': 'Lists',
            'question_details': 'What is list comprehension?'
        }

        self.test_answer = {
            "answer_details": "It is a simple way of creating a lists"
        }

        self.blank_answer = {
            "answer_details": ""
        }


    
    def tearDown(self):
        pass

class TestAnswers(BaseTestCase):
    def post_question(self):
        #  post questions to get started

        get_token = json.loads(self.test_login.data.decode())
        
        access_token = get_token['access_token']

        results = self.test_client.post(
            'api/v1/questions', data=json.dumps(self.test_data), content_type='application/json',
             headers = {'Authorization' : 'Bearer '+ access_token })

        return results


    def post_answer(self):
        # post answer to question

        get_token = json.loads(self.test_login.data.decode())
        access_token = get_token['access_token']

        results = self.test_client.post(
            'api/v1/questions/1/answers',
            data=json.dumps(self.test_answer),
            content_type='application/json', headers = {'Authorization' : 'Bearer '+ access_token })

        return results

    def test_post_answer(self):
        # test if user can post answer

        self.post_question()
        get_token = json.loads(self.test_login.data.decode())
        access_token = get_token['access_token']

        answer = self.test_client.post(
            'api/v1/questions/1/answers',
            data=json.dumps(self.test_answer),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        self.assertEqual(answer.status_code, 201)

    def test_blank_answer(self):
        self.post_question()
        get_token = json.loads(self.test_login.data.decode())
        access_token = get_token['access_token']

        result = self.test_client.post(
            'api/v1/questions/1/answers',
            data=json.dumps(self.blank_answer),
            content_type='application/json',  headers = {'Authorization' : 'Bearer '+ access_token })

        self.assertEqual(result.status_code, 400)    