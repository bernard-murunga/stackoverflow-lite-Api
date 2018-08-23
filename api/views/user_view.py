from flask import jsonify, request
from flask_restful import  Resource, fields, marshal, reqparse
import datetime
from api.resources.users import user_list
from models.users import User_model
from Validate import validations

now = datetime.datetime.now()

user_fields = {
    'username': fields.String,
    'email': fields.String,
    'password': fields.String
}

class RegisterUser(Resource):
    # Register user
    def post(self):
        # new_user = {
        #     "user_name": request.json['user_name'],
        #     "email": request.json['email'],
        #     "password": request.json['password'],
        #     "created_at": str(now)
        # }

        # user_list.append(new_user)

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True,
                                   help='Username is required',
                                   location='json')
        self.reqparse.add_argument('email', type=str, required=True,
                                   help='Email is required', location='json')
        self.reqparse.add_argument('password', type=str, required=True,
                                   help='Password is required', location='json')

        args = self.reqparse.parse_args()

        all_users = User_model.users()

        user_exists = validations.check_user_duplication(all_users, args['username'], args['email']) 

        if user_exists:
            return {"message": user_exists} 

        validate_input = validations.validate_username(args['username'])

        if validate_input:
            return {"message": validate_input}

        new_user = User_model.register_user(args['username'], args['email'], args['password'])

        if new_user:
            return {"message": "User created"}


class LoginUser(Resource):
    def post(self):
        username = request.json['username']
        password = request.json['password']

        return {"message": "Login successful", "username": username}

