from flask import request, jsonify
from Utils.function_jwt import write_token, validate_token
from os import getenv


def ping_service():
    try:
        return "pong"
    except Exception as e:
        return jsonify({'message': str(e)}, 404)


def login_service(data):
    try:
        if 'username' in data and type(data['username']) == str:
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
    except Exception as e:
        return jsonify({'message': str(e)}, 404)


def verify_service(token):
    try:
        return validate_token(token, output=True)
    except Exception as e:
        return jsonify({'message': str(e)}, 404)
