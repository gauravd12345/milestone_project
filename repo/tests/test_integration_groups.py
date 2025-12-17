# tests/test_integration_groups.py
from app.models import User, StudyGroup, GroupMembership, Nudge, db
from werkzeug.security import generate_password_hash


def make_user(email, password="secret123"):
    u = User(email=email, password_hash=generate_password_hash(password))
    db.session.add(u)
    db.session.commit()
    return u


def login(client, email, password="secret123"):
    return client.post(
        "/auth/login",
        data={"email": email, "password": password},
        follow_redirects=True,
    )


def test_group_create_and_auto_membership(client, app):
    with app.app_context():
        u = make_user("creator@test.com")
        creator_id = u.id
        creator_email = u.email

    login(client, creator_email)

    resp = client.post(
        "/groups/create",
        data={"name": "Test Group", "description": "Hi"},
        follow_redirects=True,
    )

    # Should render some page (likely group detail or list) without error
    assert resp.status_code == 200

    with app.app_context():
        g = StudyGroup.query.filter_by(name="Test Group").first()
        assert g is not None
        # Creator should be a member
        assert GroupMembership.query.filter_by(
            user_id=creator_id, group_id=g.id
        ).first() is not None


def test_join_group(client, app):
    with app.app_context():
        owner = make_user("own@test.com")
        g = StudyGroup(name="Joinable", owner=owner)
        db.session.add(g)
        db.session.add(GroupMembership(user=owner, group=g))
        db.session.commit()

        group_id = g.id
        other = make_user("other@test.com")
        other_id = other.id
        other_email = other.email

    login(client, other_email)

    resp = client.post(
        "/groups/join",
        data={"name": "Joinable"},
        follow_redirects=True,
    )

    assert resp.status_code == 200

    with app.app_context():
        assert GroupMembership.query.filter_by(
            user_id=other_id, group_id=group_id
        ).first() is not None


def test_send_nudge(client, app):
    with app.app_context():
        u1 = make_user("a@test.com")
        u2 = make_user("b@test.com")

        g = StudyGroup(name="NudgeGrp", owner=u1)
        db.session.add(g)
        db.session.add(GroupMembership(user=u1, group=g))
        db.session.add(GroupMembership(user=u2, group=g))
        db.session.commit()

        group_id = g.id
        sender_id = u1.id
        recipient_id = u2.id
        sender_email = u1.email

    login(client, sender_email)

    resp = client.post(
        f"/groups/{group_id}?to={recipient_id}",
        data={"message": "Keep going!"},
        follow_redirects=True,
    )

    assert resp.status_code == 200

    with app.app_context():
        nudge = Nudge.query.filter_by(
            sender_id=sender_id, recipient_id=recipient_id, group_id=group_id
        ).first()
        assert nudge is not None
        assert nudge.message == "Keep going!"
