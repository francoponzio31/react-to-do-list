from flask import Blueprint, jsonify, request


tasks_bp = Blueprint("tasks", __name__, url_prefix="/api/tasks")

tasks = []

@tasks_bp.get("/")
def get_tasks():
    return jsonify({"success": True, "message": "successfull request", "tasks": tasks})


@tasks_bp.get("/<int:id>/")
def get_task(id):
    for task in tasks:
        if task["id"] == id:
            return jsonify({"success": True, "message": "successfull request", "task": task})
        
    return jsonify({"success": False, "message": "task not found"}), 404


@tasks_bp.post("/")
def create_task():
    task_text = request.json.get("text")
    if not task_text:
        return jsonify({"success": False, "message": "no task_text in body"}), 400
    
    tasks.append(
        {
            "id": tasks[-1]["id"] + 1 if tasks else 0,
            "text": task_text,
            "done": False
        }
    )

    return jsonify({"success": True, "message": "task created", "tasks": tasks}), 201


@tasks_bp.put("/<int:id>/")
def update_task(id):
    new_text = request.json.get("text")
    new_done = request.json.get("done")
    
    for task in tasks:
        if task["id"] == id:
            if new_text is not None: task["text"] = new_text
            if new_done is not None: task["done"] = new_done
            return jsonify({"success": True, "message": "task updated", "task": task})

    return jsonify({"success": False, "message": "task not found"}), 404


@tasks_bp.delete("/<int:id>/")
def delete_task(id):
   
    for index, task in enumerate(tasks):
        if task["id"] == id:
            tasks.pop(index)
            return jsonify({"success": True, "message": "task deleted", "task": task})

    return jsonify({"success": False, "message": "task not found"}), 404
