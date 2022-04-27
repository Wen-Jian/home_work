from app.models.task import Task

def test_new_task(new_task):
    """
    GIVEN a Task model
    WHEN a new Task is created
    THEN check the status, and name fields are defined correctly
    """
    assert new_task.name == 'Test Task'
    assert new_task.status == False