# use_cases/task_use_cases.py
class TaskUseCases:
    def __init__(self, task_repo):
        self.task_repo = task_repo

    def get_all_tasks(self):
        return self.task_repo.get_all()

    def create_task(self, title, description):
        new_task = self.task_repo.create(title, description)
        return new_task

    def mark_task_done(self, task_id):
        task = self.task_repo.get(task_id)
        if not task:
            raise ValueError("Task not found")
        task.is_done = True
        self.task_repo.update(task)
        return task
