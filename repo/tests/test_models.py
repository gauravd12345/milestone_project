from app.models import Task

def test_task_default_status():
    t = Task(title="Demo")
    assert t.status == "open"
