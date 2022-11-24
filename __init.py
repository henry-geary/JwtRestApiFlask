from flask import Flask
from Api.auth import routes_auth
from Api.queue import queue


def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes_auth, url_prefix="/api")
    app.register_blueprint(queue, url_prefix="/api/queue")
    return app
