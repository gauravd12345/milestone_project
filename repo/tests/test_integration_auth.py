# tests/test_integration_auth.py
from app.models import User


def test_register_login_logout_flow(client):
    # Register
    resp = client.post(
        "/auth/register",
        data={"email": "a@b.com", "password": "test123"},
        follow_redirects=True,
    )
    assert resp.status_code == 200
    assert b"Account created" in resp.data or b"account created" in resp.data.lower()

    # Login
    resp = client.post(
        "/auth/login",
        data={"email": "a@b.com", "password": "test123"},
        follow_redirects=True,
    )
    assert resp.status_code == 200
    # Just confirm the user ended up somewhere valid
    assert b"StudyBuddy" in resp.data

    # Logout
    resp = client.get("/auth/logout", follow_redirects=True)
    assert resp.status_code == 200
    assert b"logged out" in resp.data.lower() or b"Login" in resp.data


def test_dashboard_requires_login(client):
    resp = client.get("/profile", follow_redirects=False)
    assert resp.status_code == 302
    assert "/auth/login" in resp.headers["Location"]
