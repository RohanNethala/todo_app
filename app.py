# app.py
from flask import Flask, jsonify, request
from adapters.task_repo_sqlite import TaskRepoSQLite
from use_cases.task_use_cases import TaskUseCases

app = Flask(__name__)

# Initialize repository and use cases
task_repo = TaskRepoSQLite(db_path="tasks.db")
task_use_cases = TaskUseCases(task_repo)

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = task_use_cases.get_all_tasks()
    return jsonify([vars(task) for task in tasks])

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    new_task = task_use_cases.create_task(data["title"], data["description"])
    return jsonify(vars(new_task)), 201

@app.route("/tasks/<int:task_id>/done", methods=["POST"])
def mark_task_done(task_id):
    try:
        updated_task = task_use_cases.mark_task_done(task_id)
        return jsonify(vars(updated_task))
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

if __name__ == "__main__":
    app.run(debug=True)
