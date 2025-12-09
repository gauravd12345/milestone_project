from app.models import Task, User, db

def login_user(client):
    client.post(
        "/auth/login",
        data={"email": "test@example.com", "password": "password123"},
        follow_redirects=True,
    )

def test_edit_goal(client, app):
    login_user(client)

    # Create a goal
    with app.app_context():
        user = User.query.filter_by(email="test@example.com").first()
        goal = Task(title="Old Title", status="open", assignee_id=user.id)
        db.session.add(goal)
        db.session.commit()
        goal_id = goal.id

    # Edit the goal
    resp = client.post(
        f"/goals/{goal_id}/edit",
        data={
            "title": "New Title",
            "description": "",
            "course_code": "",
            "status": "in_progress",
            "due_date": "",
            "assignee_id": -1,
        },
        follow_redirects=True,
    )
    assert b"Goal updated" in resp.data

    # Confirm DB updated
    with app.app_context():
        updated = Task.query.get(goal_id)
        assert updated.title == "New Title"
        assert updated.status == "in_progress"
