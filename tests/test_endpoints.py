import pytest
from api.v1.views import get_questions

#  Test if endpoint returns all questions
def test_get_all_questions(client):
    expected_result = {
    "questions": [
    {
        'id': 1,
        'question': 'What is linting?',
        'answers': [{'one': 'Showing syntax errors'}, {'two': 'Highlight style error'}]
    },
    {
        'id': 2,
        'question': 'What is TDD?',
        'answers': [{'one': 'Writing tests'}, {'two': 'Writing tests before application code'}]
    }
    ]
}
    response = client.get('/api/v1/questions')
    assert response.status_code == 200
    assert b'"id":1' in response.data
    assert b'"id":2' in response.data
    assert expected_result == response.get_json()


#  Test if endpoint returns specified question
def test_fetch_question(client):
    expected_result = {
    "question": {
        "answers": [{
            "one": "Writing tests"},
            {"two": "Writing tests before application code"
        }],
        "id": 2,
        "question": "What is TDD?"
    }
}
    response = client.get('/api/v1/questions/2')
    assert response.status_code == 200
    assert expected_result == response.get_json()


# Test if question is posted and status is 201(created)
def test_post_question(client):
    response = client.post('/api/v1/questions', json={
        "question": "Which python test types do you know?"
        })
    assert response.status_code == 201
    assert b'Which python test types do you know?' in response.data


# Test if answer to particular question is posted
def test_post_answer(client):
    expected_result = {
    "question": {
        "answers": [
            {
                "one": "Showing syntax errors"
            },
            {
                "two": "Highlight style error"
            },
            {
                "three": "New answer"
            }
        ],
        "id": 1,
        "question": "What is linting?"
    }
}
    response = client.post('/api/v1/questions/2/answer', json={'three': 'New answer'}
        )
    assert response.status_code == 200
    assert expected_result == response.get_json()