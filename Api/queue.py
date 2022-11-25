import json
from flask import Blueprint, request
from Utils.function_jwt import validate_token
import Services.queue as s
from redis import Redis


queue = Blueprint("queue", __name__)
r = Redis(host="redis-container", port=6379)


@queue.before_request
def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token, output=False)


@queue.route("/ping_redis")
def ping():
    return s.ping_service()


@queue.route('/push', methods=['POST'])
def push():
    data = json.loads(request.data)
    return s.push_service(data)


@queue.route('/pop')
def pop():
    return s.pop_service()


@queue.route('/count')
def count():
    return s.count_service()
