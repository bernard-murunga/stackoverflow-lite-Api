from flask import jsonify, request
from flask_restful import  Resource, fields, marshal, reqparse
import datetime
from api.resources.answers import answers_dictionary
from models.answers import Answers_model
from models.questions import Questions_model
from Validate import validations

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

now = datetime.datetime.now()

answer_fields = {
    'answer_details': fields.String
}

class Answers(Resource):
    #post answer
    @jwt_required
    def post(self,question_id):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('answer_details', type=str, required=True,
                                   help='Answer details is required',
                                   location='json')

        args = self.reqparse.parse_args()

        user_id = get_jwt_identity()

        all_questions = Questions_model.get_questions()
        
        validate_question = validations.question_id_found(all_questions, question_id)

        if validate_question:
            return {"message": "Question you are trying to answer not found"}, 404

        validate_answer = validations.duplicate_answer(args['answer_details'])

        if validate_answer:
            return {"message": "Answer already exists"}, 400

        new_answer = Answers_model.post_answer(user_id, question_id, args['answer_details'])

        if new_answer:
            return {"message": "Answer posted"}, 201

    # mark preferred answers
    @jwt_required
    def put(self,question_id,answer_id):
        
        user_id = get_jwt_identity()

        author_confirmation = validations.check_question_author(user_id, question_id) 

        if author_confirmation:
            return {"message": author_confirmation}

        approval = Answers_model.accept_answer(question_id, answer_id)

        if approval:
            return {"message": "Answer accepted"}, 201



