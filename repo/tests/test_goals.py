from app.models import Task, User, db


def login(client, email="test@example.com", password="password123"):
    return client.post(
        "/auth/login",
        data={"email": email, "password": password},
        follow_redirects=True,
    )


def test_create_goal(client, app):
    login(client)

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
        goals = Task.query.all()
        assert len(goals) == 1
        assert goals[0].title == "Read Chapter 3"


def test_mark_goal_done_and_completed_page(client, app):
    login(client)
    # Create a goal
    with app.app_context():
        user = User.query.filter_by(email="test@example.com").first()
        goal = Task(
            title="Finish homework",
            status="done",
            assignee_id=user.id,
        )
        db.session.add(goal)
        db.session.commit()

    # Completed page should show it
    resp = client.get("/goals/completed")
    assert b"Finish homework" in resp.data
