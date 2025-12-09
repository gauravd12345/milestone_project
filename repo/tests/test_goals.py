from app.models import Task, User, db

def login_default_user(client):
    client.post(
        "/auth/login",
        data={"email": "test@example.com", "password": "password123"},
        follow_redirects=True,
    )

def test_create_goal(client, app):
    login_default_user(client)

    resp = client.post(
        "/goals/create",
        data={
            "title": "Read Chapter 3",
            "description": "Focus on sections 3.1–3.3",
            "course_code": "CS101",
            "status": "open",
            "due_date": "2025-12-31",
            "assignee_id": -1,
        },
        follow_redirects=True,
    )
    assert b"Goal created" in resp.data

    with app.app_context():
        goal = Task.query.first()
        assert goal.title == "Read Chapter 3"


def test_completed_goals_page(client, app):
    login_default_user(client)

    with app.app_context():
        user = User.query.filter_by(email="test@example.com").first()
        goal = Task(title="Finish homework", status="done", assignee_id=user.id)
        db.session.add(goal)
        db.session.commit()

    resp = client.get("/goals/completed")
    assert b"Finish homework" in resp.data
