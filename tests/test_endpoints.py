from unittest import TestCase
from app import create_app
import json
from api.resources.questions import questions_dictionary
from api.resources.answers import answers_dictionary

class BaseTestCase(TestCase):
    def setUp(self):
        self.app = create_app()
        self.test_client = self.app.test_client()

        self.test_question= {
            "question_title": "Colors",
            "question_details": "What color is the sky?"
            }

        self.test_answer = {
            "answer_details": "It is deprecated",
            "question_id": 1
        }

        self.mark_answer = {
            "question_id": 1,
            "answer_id": 1,
            "preferred": "yes"
            }

        self.test_user = {
            "username": "ben",
            "password": "wooii"
        }

class AllQuestionsTestCase(BaseTestCase):
    def test_getting_all_questions(self):
        result = self.test_client.get('/api/v1/questions')
        result_data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_data[0]['message'], 'Questions found')


class SpecificQuestion(BaseTestCase):
    def test_indvidual_question(self):
        result = self.test_client.get('/api/v1/questions/2')
        result_data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_data[0]['message'], 'Question found')


class PostQuestion(BaseTestCase):
    def test_posting_question(self):
        result = self.test_client.post('/api/v1/questions', data=json.dumps(
            self.test_question),  content_type='application/json')
        result_data = json.loads(result.data)

        self.assertEqual(result.status_code, 201)
        self.assertEqual(result_data['message'], 'Question posted')


class PostAnswer(BaseTestCase):
    def test_posting_answer(self):
        result = self.test_client.post('/api/v1/questions/2/answers', data=json.dumps(
            self.test_answer),  content_type='application/json')
        result_data = json.loads(result.data)

        self.assertEqual(result.status_code, 201)
        self.assertEqual(result_data[0]['message'], 'Answer posted')


class DeleteQuestion(BaseTestCase):
    def testing_question_deletion(self):
        result = self.test_client.delete('/api/v1/questions/2')
        result_data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_data[0]['message'], 'Question deleted')


class PreferAnswer(BaseTestCase):
    def test_preferring_answers(self):
        result = self.test_client.put('/api/v1/questions/1/answers/1',
        json.dumps(self.mark_answer), content_type='application/json')
        result_data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_data[0]['message'], 'Answer updated')


class RegisterUser(BaseTestCase):
    def test_user_reistration(self):
        result = self.test_client.post('/api/v1/auth/signup',
        json.dumps(self.test_user), content_type='application/json')
        result_data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_data[0]['message'], 'User created')

    def test_user_login(self):
        result = self.test_client.post('/api/v1/auth/login',
        json.dumps(self.test_user['username']), content_type='application/json')
        result_data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_data[0]['message'], 'Login successful')



if __name__ == '__main__':
    unittest.main()