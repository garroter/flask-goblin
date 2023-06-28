import pytest
from app import create_app


@pytest.fixture(scope="class")
def app():
    app = create_app("Test")

    # with app.app_context():
    # db.create_all()

    yield app


@pytest.fixture(scope="class")
def client(app):
    return app.test_client()
