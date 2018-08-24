from flask import Flask
from flask_restful import Resource, Api
from api.views.questions_view import Questions, SpecificQuestion
from api.views.answers_view import Answers
from api.views.user_view import RegisterUser, LoginUser
from api.manage_db import create_tables
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    jwt = JWTManager(app)


    create_tables()

    api.add_resource(Questions, '/api/v1/questions')
    api.add_resource(SpecificQuestion, '/api/v1/questions/<int:question_id>')
    api.add_resource(Answers,'/api/v1/questions/<int:question_id>/answers',
    '/api/v1/questions/<int:question_id>/answers/<int:answer_id>')
    api.add_resource(RegisterUser, '/api/v1/auth/signup')
    api.add_resource(LoginUser, '/api/v1/auth/login')
    
    return app
