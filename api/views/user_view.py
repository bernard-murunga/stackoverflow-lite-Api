from flask import jsonify, request
from flask_restful import  Resource
import datetime
from api.resources.users import user_list

now = datetime.datetime.now()

class RegisterUser(Resource):
    # Register user
    def post(self):
        new_user = {
            "user_name": request.json['user_name'],
            "password": request.json['password'],
            "created_at": str(now)
        }

        user_list.append(new_user)
        return jsonify({"message": "User created", "users": user_list})


class LoginUser(Resource):
    def post(self):
        username = request.json['username']
        password = request.json['password']

        return {"message": "Login successful", "username": username}

