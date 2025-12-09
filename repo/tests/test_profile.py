from app.models import Task, User, db


def login(client, email="test@example.com", password="password123"):
    return client.post(
        "/auth/login",
        data={"email": email, "password": "password123"},
        follow_redirects=True,
    )


def test_profile_counts_goals(client, app):
    login(client)
    with app.app_context():
        user = User.query.filter_by(email="test@example.com").first()
        g1 = Task(title="G1", status="open", assignee_id=user.id, course_code="CS101")
        g2 = Task(title="G2", status="done", assignee_id=user.id, course_code="CS102")
        db.session.add_all([g1, g2])
        db.session.commit()

    resp = client.get("/profile")
    # Very light checks, just ensure page renders & mentions totals
    assert b"Total goals" in resp.data
    assert b"Completed goals" in resp.data
