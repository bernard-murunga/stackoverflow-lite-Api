from flask import Flask, jsonify, abort, make_response, request

from . import app

questions = [
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


@app.route('/api/v1/questions', methods=['GET'])
def get_questions():
    return jsonify({'questions': questions})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/v1/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    question = [question for question in questions if question['id'] == question_id]
    if len(question) == 0:
        abort(404)
    return jsonify({'question': question[0]})


@app.route('/api/v1/questions', methods=['POST'])
def create_question():
    if not request.json or not 'question' in request.json:
        abort(400)
    question = {
        'id': questions[-1]['id'] + 1,
        'question': request.json['question']
    }
    questions.append(question)
    return jsonify({'question': question}), 201


@app.route('/api/v1/questions/<int:question_id>/answer', methods=['POST'])
def create_answer(question_id):
    question = [question for question in questions if question['id'] == question_id]
    if not request.json:
        abort(404)
    # question[0]['answers'] = request.json.get('answers', question[0]['answers'])
    answer = {'three': 'New answer'}
    questions[0]['answers'].append(answer)
    
    return jsonify({'question': questions[0]})


if __name__ == '__main__':
    app.run(debug=True)
