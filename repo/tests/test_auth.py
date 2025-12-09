from app.models import User, db


def test_register_and_login(client, app):
    # Register a new user
    resp = client.post(
        "/auth/register",
        data={"email": "new@example.com", "password": "secret123"},
        follow_redirects=True,
    )
    assert b"Account created" in resp.data

    with app.app_context():
        u = User.query.filter_by(email="new@example.com").first()
        assert u is not None

    # Login with that user
    resp = client.post(
        "/auth/login",
        data={"email": "new@example.com", "password": "secret123"},
        follow_redirects=True,
    )
    assert b"Welcome back" in resp.data
