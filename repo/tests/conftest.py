# tests/conftest.py
import os
import sys
from pathlib import Path

import pytest

# Make sure the "repo" root (which contains app/) is on sys.path,
# no matter where pytest is run from.
ROOT_DIR = Path(__file__).resolve().parents[1]  # this is the folder that has app/
sys.path.insert(0, str(ROOT_DIR))

from app import create_app, db  # now this should work
from app.models import User, Task


@pytest.fixture()
def app(tmp_path):
    """
    Create a fresh app + SQLite DB in a temporary directory for each test run.
    """
    os.environ["DATABASE_URL"] = f"sqlite:///{tmp_path / 'test.sqlite3'}"
    app = create_app()

    with app.app_context():
        db.create_all()
        # Create a default user used by some tests
        user = User(email="test@example.com")
        user.set_password("password123")
        db.session.add(user)
        db.session.commit()

    yield app

    # Teardown
    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
