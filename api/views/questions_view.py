from flask import jsonify, request, make_response
from flask_restful import Resource, fields, marshal, reqparse
import datetime
from api.resources.questions import questions_dictionary
from models.questions import Questions_model
from Validate import validations


now = datetime.datetime.now()

question_fields = {
    'question_title': fields.String,
    'question_details': fields.String
}


class Questions(Resource):
    #  Return all questions
    def get(self):
        all_questions = Questions_model.get_questions()
        if not all_questions:
            return {"message": "No questions yet."}, 400

        return {"message": "Questions found", "questions": all_questions}

    #  Post a question.
    def post(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('question_title', type=str, required=True,
                                   help='Question title is required',
                                   location='json')
        self.reqparse.add_argument('question_details', type=str, required=True,
                                   help='Question details is required', location='json')

        args = self.reqparse.parse_args()

        all_questions = Questions_model.get_questions()
        
        check_question = validations.question_exists(all_questions, args['question_title'],args['question_details'])

        if check_question:
            return {"message": check_question}, 400


        user_id = 1
        
        questions = Questions_model(args['question_title'], args['question_details'],
             user_id).insert_question()     
        
        if questions:
            return {"message": "Question posted", "questions": marshal(questions, question_fields)}, 201


class SpecificQuestion(Resource):
    #  Get question using the question id
    def get(self, question_id):
        
        single_question = [question for question in questions_dictionary if question['question_id'] == question_id]

        if len(single_question) == 0:
            return {"message": "Question can't be blank"}, 404

        return {"message": "Question found", "questions": single_question}


    # Delete specific question by author
    def delete(self, question_id):
        question = [question for question in questions_dictionary if question['question_id'] == question_id]

        if len(question) == 0:
            return {"message": "Question to be deleted not found"}, 404

        questions_dictionary.remove(question[0])

        return jsonify({"message": "Question deleted"}, {"questions": questions_dictionary})



        
