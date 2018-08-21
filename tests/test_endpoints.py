from unittest import TestCase
from app import create_app
import json

class BaseTestCase(TestCase):
    def setUp(self):
        self.app = create_app()
        self.test_client = self.app.test_client()

class AllQuestionsTestCase(BaseTestCase):
    def test_getting_all_questions(self):
        result = self.test_client.get('/api/v1/questions')
        result_data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_data['message'], 'Dictionary of questions')


class SpecificQuestion(BaseTestCase):
    def test_indvidual_question(self):
        result = self.test_client.get('/api/v1/questions/2')
        result_data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_data['message'], 'Dictionary containing question')


class PostQuestion(BaseTestCase):
    def test_posting_question(self):
        result = self.test_client.get('/api/v1/questions')
        result_data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_data['message'], 'Dictionary containing question')


class PostAnswer(BaseTestCase):
    def test_posting_answer(self):
        result = self.test_client.get('/api/v1/questions/2/answers')
        result_data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_data['message'], 'List containing answer')


class PreferAnswer(BaseTestCase):
    def test_preferring_answers(self):
        result = self.test_client.get('/api/v1/questions/2/answers/2')
        result_data = json.loads(result.data)

        self.assertEqual(result.status_code, 201)
        self.assertEqual(result_data['message'], 'Dictionary containing question')

    def test_user_marking_authorization(self):
        result  = self.test_client.get('/api/v1/questions/2/answers/2?username=""')
        result_data = json.loads(result.data)

        self.assertEqual(result_data.status_code, 401)
        self.assertEqual(result_data['message'], 'You are not authorized to mark or accept answer')


if __name__ == '__main__':
    unittest.main()