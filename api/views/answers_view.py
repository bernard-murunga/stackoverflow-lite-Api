from flask import jsonify, request
from flask_restful import  Resource, fields, marshal, reqparse
import datetime
from api.resources.answers import answers_dictionary
from models.answers import Answers_model
from models.questions import Questions_model
from Validate import validations

now = datetime.datetime.now()

answer_fields = {
    'answer_details': fields.String
}

class Answers(Resource):
    #post answer
    def post(self,question_id):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('answer_details', type=str, required=True,
                                   help='Answer details is required',
                                   location='json')

        args = self.reqparse.parse_args()

        user_id = 1  # change later with JWT

        all_questions = Questions_model.get_questions()
        
        validate_question = validations.question_id_found(all_questions, question_id)

        if validate_question:
            return {"message": "Question you are trying to answer not found"}, 404

        validate_answer = validations.duplicate_answer(args['answer_details'])

        if validate_answer:
            return {"message": "Answer already exists"}, 400

        new_answer = Answers_model.post_answer(user_id, question_id, args['answer_details'])

        if new_answer:
            return {"message": "Answer posted", "answers": marshal(new_answer, answer_fields)}, 201

    # mark preferred answers
    def put(self,question_id,answer_id):
        # question = [question for question in answers_dictionary if question['question_id'] == question_id]
        # answer = [answer for answer in answers_dictionary if answer['answer_id'] == answer_id]

        # if len(question) == 0:
        #     return {"message": "Question doesn't exist"}, 404

        # if len(answer) == 0:
        #     return {"message": "Answer doesn't exist"},404

        # answer[0]['preferred'] = request.json['preferred']
        # answer[0]['updated_at'] = str(now)

        user_id = 1  ## change using JWT

        author_confirmation = validations.check_question_author(user_id, question_id) 

        if author_confirmation:
            return {"message": author_confirmation}

        approval = Answers_model.accept_answer(question_id, answer_id)

        if approval:
            return {"message": "Answer accepted"}, 201



