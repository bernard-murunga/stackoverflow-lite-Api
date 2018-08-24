from unittest import TestCase
from api import create_app
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


        self.test_question= {
            "question_title": "Colors",
            "question_details": "What color is the sky?"
            }

        self.test_client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.sign_up),
            content_type='application/json')

        self.test_login = self.test_client.post(
            '/api/v1/auth/login',
            data=json.dumps(self.login_credentials),
            content_type='application/json')

    def tearDown(self):
        pass

class AllQuestionsTestCase(BaseTestCase):
    def post_question(self):
        #  post questions to get started

        get_token = json.loads(self.test_login.data.decode())
        
        access_token = get_token['access_token']

        results = self.test_client.post(
            'api/v1/questions', data=json.dumps(self.test_question), content_type='application/json',
             headers = {'Authorization' : 'Bearer '+ access_token })

        return results

    def test_all_questions(self):
        # get all questions
        
        get_token = json.loads(self.test_login.data.decode())
        access_token = get_token['access_token']

        response = self.test_client.get('/api/v1/questions', headers = {'Authorization' : 'Bearer '+ access_token })
        self.assertEqual(response.status_code, 200)


    def test_indvidual_question(self):
        get_token = json.loads(self.test_login.data.decode())
        access_token = get_token['access_token']

        self.post_question()

        response = self.test_client.get('/api/v1/questions/6', headers = {'Authorization' : 'Bearer '+ access_token })
        self.assertEqual(response.status_code, 200)
   

    def testing_question_deletion(self):
        get_token = json.loads(self.test_login.data.decode())
        access_token = get_token['access_token']

        self.post_question()

        response = self.test_client.delete('/api/v1/questions/4', headers = {'Authorization' : 'Bearer '+ access_token })
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()