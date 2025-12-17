# tests/test_permissions.py
from app.models import User, db
from werkzeug.security import generate_password_hash


def make_user(email):
  u = User(email=email, password_hash=generate_password_hash("pw"))
  db.session.add(u)
  db.session.commit()
  return u


def test_student_cannot_access_other_profile(client, app):
    with app.app_context():
        u1 = make_user("one@test.com")
        u2 = make_user("two@test.com")

    client.post(
        "/auth/login",
        data={"email": "one@test.com", "password": "pw"},
        follow_redirects=True,
    )

    # adapt this to however you *would* try to hit another profile;
    # for now just assert that /profile only shows current user.
    resp = client.get("/profile", follow_redirects=True)

    assert resp.status_code == 200
    # Should not expose the other user's email anywhere
    assert b"two@test.com" not in resp.data
