from flask import Flask
from routes.auth import routes_auth
from routes.redis_endpoint import redis_endpoint
from dotenv import load_dotenv

app = Flask(__name__)

app.register_blueprint(routes_auth, url_prefix="/api")
app.register_blueprint(redis_endpoint, url_prefix="/api/queue")

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True, port=4000, host="0.0.0.0")
