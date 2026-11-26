import pytest

from app import create_app
from app.db import get_db, init_db


@pytest.fixture
def app(tmp_path):
    """An app that uses an empty, temporary database for each test."""
    app = create_app({
        "TESTING": True,
        "DATABASE": str(tmp_path / "test.db"),
    })
    with app.app_context():
        init_db()
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db(app):
    """A database connection for testing domain functions directly."""
    with app.app_context():
        yield get_db()
