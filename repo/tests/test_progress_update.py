from app.models import Task, User, db

def login_default_user(client):
    client.post(
        "/auth/login",
        data={"email": "test@example.com", "password": "password123"},
        follow_redirects=True,
    )

def test_progress_update_saved(client, app):
    login_default_user(client)

    # Create a goal first
    with app.app_context():
        user = User.query.filter_by(email="test@example.com").first()
        goal = Task(
            title="Read Chapter 5",
            status="open",
            assignee_id=user.id,
        )
        db.session.add(goal)
        db.session.commit()
        goal_id = goal.id

    # Submit a progress update
    resp = client.post(
        f"/goals/{goal_id}/edit",
        data={
            "title": "Read Chapter 5",
            "description": "",
            "course_code": "",
            "status": "in_progress",
            "due_date": "",
            "assignee_id": -1,
            "progress_note": "Finished 20 pages today.",
        },
        follow_redirects=True,
    )

    assert b"Goal updated" in resp.data

    # Validate DB was updated
    with app.app_context():
        updated = Task.query.get(goal_id)
        assert updated.progress_note == "Finished 20 pages today."
