from flask import Blueprint, request, jsonify
from function_jwt import write_token, validate_token
from os import getenv


routes_auth = Blueprint("routes_auth", __name__)


@routes_auth.route("/ping")
def ping():
    return "pong"


def validateLogin(data_object):
    if 'username' in data_object and type(data_object['username']) == str:
        return True
    else:
        return False


@routes_auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if validateLogin(data_object=data):
        if data['username'] == getenv("ADMIN"):
            token_str = write_token(data=request.get_json()).decode("utf-8")
            response = jsonify({"Status": "Successfully Auth", "token": token_str})
            response.status_code = 200
            return response
        else:
            response = jsonify({"message": "User not found"})
            response.status_code = 404
            return response
    else:
        response = jsonify({"message": "Invalid user data"})
        response.status_code = 400
        return response


@routes_auth.route("/verify/token")
def verify():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token, output=True)

