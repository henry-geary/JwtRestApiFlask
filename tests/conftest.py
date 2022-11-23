import pytest
from app_project import create_app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture
def app(monkeypatch):
    monkeypatch.setenv('SECRET', 'ayudaaaaaa')
    monkeypatch.setenv('ADMIN', 'jefecito')
    flask_app = create_app()
    return flask_app
