from flask import jsonify, request
from flask_restful import  Resource, fields, marshal, reqparse
import datetime
from api.resources.users import user_list
from models.users import User_model
from Validate import validations
from flask_jwt_extended import (create_access_token, create_refresh_token,
 jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


now = datetime.datetime.now()

user_fields = {
    'username': fields.String,
    'email': fields.String,
    'password': fields.String
}

class RegisterUser(Resource):
    # Register user
    def post(self):
        
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

        access_token = create_access_token(identity = args['username'])
        refresh_token = create_refresh_token(identity = args['username'])

        if new_user:
            return {"message": "User created", "access_token": access_token,
             "refresh_token": refresh_token}


class LoginUser(Resource):
    def post(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True,
                                   help='Username is required',
                                   location='json')

        self.reqparse.add_argument('password', type=str, required=True,
                                   help='Password is required',
                                   location='json')

        args = self.reqparse.parse_args()

        user = User_model.user_id(args['username'], args['password'])
        
        if user:
            access_token = create_access_token(identity = user)
            refresh_token = create_refresh_token(identity = user)
            return {
                "message": "Login successful",
                "access_token": access_token,
                "refresh_token": refresh_token
                }
        else:
            return {'message': 'Wrong credentials'}

