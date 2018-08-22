from flask import jsonify, request, make_response
from flask_restful import Resource
import datetime
from api.resources.questions import questions_dictionary


now = datetime.datetime.now()

class Questions(Resource):
    #  Return all questions
    def get(self):
        return jsonify({"message": "Questions found"},{"questions": questions_dictionary})

    #  Post a question.
    def post(self):
        if not request.json or not 'question_title' in request.json:
            return make_response(jsonify({"message": "Title of the question is required."}), 400)

        if not request.json or not 'question_details' in request.json:
            return make_response(jsonify({"message": "Details of question is required."}), 400)

        new_question = {
            "user_id": 1,
            "question_id": questions_dictionary[-1]['question_id'] + 1,
            "question_title": request.json['question_title'],
            "question_details": request.json['question_details'],
            "created_at": now,
            "updated_at": now
        }

        questions_dictionary.append(new_question)

        return jsonify({"message": "Question posted"}, {"questions": questions_dictionary})


class SpecificQuestion(Resource):
    #  Get question using the question id
    def get(self, question_id):
        single_question = [question for question in questions_dictionary if question['question_id'] == question_id]

        if len(single_question) == 0:
            return {"message": "Question can't be blank"}, 404

        return jsonify({"message": "Question found"}, {"questions": single_question})


    # Delete specific question by author
    def delete(self, question_id):
        question = [question for question in questions_dictionary if question['question_id'] == question_id]

        if len(question) == 0:
            return {"message": "Question to be deleted not found"}, 404

        questions_dictionary.remove(question[0])

        return jsonify({"message": "Question deleted"}, {"questions": questions_dictionary})



        
