import json
import pdb
from app.db import db 
from app.models.task import Task

def test_api_to_get_all_tasks(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    db.session.query(Task).delete()
    db.session.commit()
    response = test_client.get('/api/v1/tasks')
    print(response)
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['result'] == []

def test_api_to_get_all_tasks_with_1_record(test_client):
    """
    GIVEN a Flask application configured for testing and creating a task before requesting
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    db.session.query(Task).delete()
    db.session.commit()
    task = Task('tttt')
    db.session.add(task)
    db.session.commit()
    response = test_client.get('/api/v1/tasks')
    print(response)
    data = json.loads(response.data)
    result = data['result'][0]
    assert response.status_code == 200
    assert result['name'] == task.name
    assert result['status'] == task.status
    assert result['id'] == task.id

def test_api_to_create_a_task(test_client):
    """
    GIVEN a Flask application configured for testing and creating a task before requesting
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    db.session.query(Task).delete()
    db.session.commit()
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    response = test_client.post('/api/v1/task', data=json.dumps({"name": 'test_task'}), headers=headers)
    print(response)
    data = json.loads(response.data)
    result = data['result'][0]
    assert response.status_code == 200
    assert result['name'] == 'test_task'

def test_api_to_update_a_task(test_client):
    """
    GIVEN a Flask application configured for testing and creating a task before requesting
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    db.session.query(Task).delete()
    db.session.commit()
    task = Task('tttt')
    db.session.add(task)
    db.session.commit()
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    response = test_client.put('/api/v1/task/%s' % task.id, data=json.dumps({"name": 'study'}), headers=headers)
    print(response)
    data = json.loads(response.data)
    result = data['result'][0]
    assert response.status_code == 200
    assert result['name'] == 'study'

def test_api_to_delete_a_task(test_client):
    """
    GIVEN a Flask application configured for testing and creating a task before requesting
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    db.session.query(Task).delete()
    db.session.commit()
    task = Task('tttt')
    db.session.add(task)
    db.session.commit()
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    response = test_client.delete('/api/v1/task/%s' % task.id, data=json.dumps({}), headers=headers)
    print(response)
    assert response.status_code == 200