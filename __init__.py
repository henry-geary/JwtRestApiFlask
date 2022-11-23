from flask import Flask
from routes.auth import routes_auth
from routes.redis_endpoint import redis_endpoint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes_auth, url_prefix="/api")
    app.register_blueprint(redis_endpoint, url_prefix="/api/queue")
    return app
