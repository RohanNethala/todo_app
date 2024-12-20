# entities/task.py
class Task:
    def __init__(self, id: int, title: str, description: str, is_done: bool = False):
        self.id = id
        self.title = title
        self.description = description
        self.is_done = is_done
