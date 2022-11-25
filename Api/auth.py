from flask import Blueprint, request
import Services.auth as s

routes_auth = Blueprint("routes_auth", __name__)


@routes_auth.route("/ping")
def ping():
    return "pong"


@routes_auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    return s.login_service(data)


@routes_auth.route("/verify/token")
def verify():
    token = request.headers['Authorization'].split(" ")[1]
    return s.verify_service(token)

