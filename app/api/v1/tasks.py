from flask import Blueprint, jsonify, request
from models.task import Task
from db import db

tasksRoute = Blueprint('tasksRoute', __name__)

@tasksRoute.route('/api/v1/tasks', methods=['GET'])
def get_tasks():
    db.session.commit()
    tasks = Task.query.all()
    print(tasks)
    return jsonify({
        'result': [{
            "name": task.name,
            "status": task.status,
            "id": task.id
        } for task in tasks]
    }), 200

@tasksRoute.route('/api/v1/task', methods=['POST','PUT'])
def create_task():
    params = request.json
    print(params)
    name = params.get('name')
    task = Task(
        name=name
    )
    db.session.add(task)
    db.session.commit()
    print(task)
    return jsonify({
        "result": [{
            "name": task.name,
            "status": task.status,
            "id": task.id
        }]
    }), 200
        

@tasksRoute.route('/api/v1/task/<task_id>', methods=['PUT', 'DELETE'])
def update_task(task_id): 
    db.session.commit()
    params = request.json
    print(params)
    if request.method == 'PUT':
        name = params.get('name')
        status = params.get('status')
        task = Task.query.filter_by(id=task_id).first()
        if name:
            task.name = name
        if status:
            task.status = status
        db.session.commit()

        print(task)
        return jsonify({
            "result": [{
                "name": task.name,
                "status": task.status,
                "id": task.id
            }]
        }), 200
    else:
        task = Task.query.filter_by(id=task_id)
        if task.count() > 0:
            task.delete()
            db.session.commit()
            return jsonify({}), 200
        else:
            return jsonify({"result": 'record not found'}), 404