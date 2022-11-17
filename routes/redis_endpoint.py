import json
from flask import Blueprint, request, jsonify
from function_jwt import validate_token
from redis import Redis


r = Redis(host="redis-container", port=6379)
redis_endpoint = Blueprint("redis_endpoint", __name__)


@redis_endpoint.route("/ping_redis")
def ping_redis():
    if r.ping():
        response = jsonify({'Connection': "OK"})
        response.status_code = 200
        return response

    else:
        response = jsonify({'Connection': "NOT OK"})
        response.status_code = 500
        return response



@redis_endpoint.before_request
def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token, output=False)


def validatePush(data_object):
    if 'msg' in data_object and type(data_object["msg"]) == str:
        return True
    else:
        return False


@redis_endpoint.route('/push', methods=['POST'])
def push():
    data = json.loads(request.data)
    if validatePush(data_object=data):
        if data["msg"]:
            r.lpush("Queue", data["msg"])
            response = jsonify({'status': 'ok'})
            response.status_code = 200
            return response
    else:
        response = jsonify({"message": "invalid message input"})
        response.status_code = 400
        return response


@redis_endpoint.route('/pop')
def pop():
    if r.llen('Queue') != 0:
        deleted = r.lpop('Queue').decode("utf-8")
        response = jsonify({"message": deleted})
        response.status_code = 200
        return response
    else:
        response = jsonify({"message": "Queue is empty"})
        response.status_code = 400
        return response


@redis_endpoint.route('/count')
def count():
    response = jsonify({"status": "ok", "count": r.llen('Queue')})
    response.status_code = 200
    return response



