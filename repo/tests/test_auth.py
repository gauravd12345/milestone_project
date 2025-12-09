from app.models import User, db

def test_register_and_login(client, app):
    # Register
    resp = client.post(
        "/auth/register",
        data={"email": "new@example.com", "password": "secret123"},
        follow_redirects=True,
    )
    assert b"Account created" in resp.data

    # Confirm user exists
    with app.app_context():
        user = User.query.filter_by(email="new@example.com").first()
        assert user is not None

    # Login
    resp = client.post(
        "/auth/login",
        data={"email": "new@example.com", "password": "secret123"},
        follow_redirects=True,
    )
    assert b"Welcome back" in resp.data
