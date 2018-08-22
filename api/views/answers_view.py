from flask import jsonify, request
from flask_restful import  Resource
import datetime
from api.resources.answers import answers_dictionary

now = datetime.datetime.now()


class Answers(Resource):
    #post answer
    def post(self,question_id):
        if 'answer_details' not in request.json:
            return {"message": "Answer details is required."}, 400

        answer = [answer for answer in answers_dictionary if answer['question_id'] == question_id]

        if len(answer) == 0:
            return {"message": "Question doesn't exist"}, 404

        new_answer = {
            "user_id": 1,
            "question_id": question_id,
            "answer_id": answers_dictionary[-1]['answer_id'] + 1,
            "answer_details": request.json['answer_details'],
            "preferred": "no",
            "created_at": now,
            "updated_at": now
        }

        answers_dictionary.append(new_answer)

        return jsonify({"message": "Answer posted"}, {"answers": answers_dictionary})

    # mark preferred answers
    def put(self,question_id,answer_id):
        question = [question for question in answers_dictionary if question['question_id'] == question_id]
        answer = [answer for answer in answers_dictionary if answer['answer_id'] == answer_id]

        if len(question) == 0:
            return {"message": "Question doesn't exist"}, 404

        if len(answer) == 0:
            return {"message": "Answer doesn't exist"},404

        answer[0]['preferred'] = request.json['preferred']
        answer[0]['updated_at'] = str(now)

        return jsonify({"message": "Answer updated"}, {"answers": answer[0]})



