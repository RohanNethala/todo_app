# adapters/task_repo_sqlite.py
import sqlite3
from entities.task import Task

class TaskRepoSQLite:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            is_done BOOLEAN
        )""")
        self.conn.commit()

    def create(self, title, description):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO tasks (title, description, is_done) VALUES (?, ?, ?)",
                       (title, description, False))
        self.conn.commit()
        return Task(cursor.lastrowid, title, description, False)

    def get(self, task_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, title, description, is_done FROM tasks WHERE id = ?", (task_id,))
        row = cursor.fetchone()
        if row:
            return Task(*row)
        return None

    def update(self, task):
        self.conn.execute(
            "UPDATE tasks SET title = ?, description = ?, is_done = ? WHERE id = ?",
            (task.title, task.description, task.is_done, task.id)
        )
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, title, description, is_done FROM tasks")
        rows = cursor.fetchall()
        return [Task(*row) for row in rows]
