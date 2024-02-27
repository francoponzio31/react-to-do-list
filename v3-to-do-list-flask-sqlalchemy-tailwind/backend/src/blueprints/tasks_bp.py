from flask import Blueprint, jsonify, request, current_app
from db.db_connection import db
from models.task_model import Task


tasks_bp = Blueprint("tasks", __name__, url_prefix="/api/tasks")

@tasks_bp.get("/")
def get_tasks():
    tasks = Task.query.all()
    tasks_json = [task.to_dict() for task in tasks] # TODO: usar serialización/deserialización con Marshmallow
    return jsonify({"success": True, "message": "successfull request", "tasks": tasks_json})


@tasks_bp.get("/<int:id>/")
def get_task(id):
    task = Task.query.get(id)
    if task:
        return jsonify({"success": True, "message": "successfull request", "task": task.to_dict()})
        
    return jsonify({"success": False, "message": "task not found"}), 404


@tasks_bp.post("/")
def create_task():
    task_text = request.json.get("text")
    if not task_text:
        return jsonify({"success": False, "message": "no task_text in body"}), 400
    
    new_task = Task(task_text)
    db.session.add(new_task)
    db.session.commit()

    tasks = Task.query.all()
    tasks_json = [task.to_dict() for task in tasks] # TODO: usar serialización/deserialización con Marshmallow

    return jsonify({"success": True, "message": "task created", "tasks": tasks_json}), 201


@tasks_bp.put("/<int:id>/")
def update_task(id):
    new_text = request.json.get("text")
    new_done = request.json.get("done")
    
    task = Task.query.filter_by(id=id).first()

    if task:
        if new_text is not None: task.text = new_text
        if new_done is not None: task.done = new_done
        db.session.commit()

        return jsonify({"success": True, "message": "task updated", "task": task})

    return jsonify({"success": False, "message": "task not found"}), 404


@tasks_bp.delete("/<int:id>/")
def delete_task(id):

    task = Task.query.filter_by(id=id).first()
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"success": True, "message": "task deleted", "task": task})

    return jsonify({"success": False, "message": "task not found"}), 404
