import json
from flask import Blueprint, request, jsonify
from Utils.function_jwt import validate_token
from redis import Redis

redis_endpoint = Blueprint("redis_endpoint", __name__)
r = Redis(host="redis-container", port=6379)


# Endpoint
def ping_service():
    try:
        if r.ping():
            response = jsonify({'Connection': "OK"})
            response.status_code = 200
            return response
        else:
            response = jsonify({'Connection': "NOT OK"})
            response.status_code = 500
            return response
    except Exception as e:
        return jsonify({'message': str(e)}, 404)


def validatePush(data_object):
    if 'msg' in data_object and type(data_object["msg"]) == str:
        return True
    else:
        return False


# Endpoint
def push_service(data):
    try:
        if validatePush(data_object=data):
            push_redis(r, "Queue", data["msg"])
            response = jsonify({'status': 'ok'})
            response.status_code = 200
            return response
        else:
            response = jsonify({"message": "invalid message input"})
            response.status_code = 400
            return response
    except Exception as e:
        return jsonify({'message': str(e)}, 404)


def push_redis(redis: Redis, key, msg):
    return redis.lpush(key, msg)


# Endpoint
def pop_service():
    try:
        if r.llen('Queue') != 0:
            deleted = pop_redis(r, "Queue")
            response = jsonify({"message": deleted})
            response.status_code = 200
            return response
        else:
            response = jsonify({"message": "Queue is empty"})
            response.status_code = 400
            return response
    except Exception as e:
        return jsonify({'message': str(e)}, 404)


def pop_redis(redis: Redis, key):
    return redis.lpop(key).decode("utf-8")


# Endpoint
def count_service():
    try:
        response = jsonify({"status": "ok", "count": count_redis(r, "Queue")})
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify({'message': str(e)}, 404)


def count_redis(redis: Redis, key):
    return redis.llen(key)
