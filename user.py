class User:
    def __init__(self, username):
        self.username = username
        self.tasks = []
        
    def assign_task(self, task):
        from task import Task
        if isinstance(task, Task): 
            self.tasks.append(task)
        else:
            raise ValueError("Задача должна быть экземпляром Task.")