import os

import pytest
from dotenv import load_dotenv

from app import create_app, db
from app.database.models import Question


@pytest.fixture
def app():
    load_dotenv()
    """
    Create and configure a new app instance for each test.
    """
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """
    A test client for the app.
    """
    return app.test_client()


@pytest.fixture
def db_session(app):
    with app.app_context():
        yield db.session
