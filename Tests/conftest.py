import pytest
from __init import create_app
from flask import jsonify


@pytest.fixture
def login_env(monkeypatch):
    monkeypatch.setenv('ADMIN', 'jefecito')
    monkeypatch.setenv('SECRET', 'ayuda')


@pytest.fixture
def app(monkeypatch):
    monkeypatch.setenv('USERNAME', 'jefecito')
    monkeypatch.setenv('SECRET', 'ayuda')
    flask_app = create_app()
    return flask_app


# START mocks for test_service_queue
@pytest.fixture
def URL_LOGING_TEST():
    return "http://localhost:4000/api/login"


@pytest.fixture
def URL_TOKEN_TEST():
    return 'http://localhost:4000/api/verify/token'


@pytest.fixture
def URL_QUEUE():
    return 'http://localhost:4000/api/queue'


@pytest.fixture
def expected_response_push():
    response = jsonify({"status": "ok"})
    response.status_code = 200
    return response


@pytest.fixture
def key():
    return 'Test'


@pytest.fixture
def msg():
    return 'Buenos dias'


# END mocks for test_api_queue

@pytest.fixture
def auth(mocker):
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" \
            ".eyJ1c2VybmFtZSI6ImplZmVjaXRvIiwiZXhwIjoxNjY5NDcyNDQyfQ" \
            ".BJJ8ApXrZlc7etFhX6Sbw4ZURtixa34zOv_5ctAyiwk"
    mocker.patch("Api.auth.login", return_value=token)
    mocker.patch("Api.queue.verify_token_middleware", return_value=True)
    return token
