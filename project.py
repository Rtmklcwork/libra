from user import User
from task import Task

class Project:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.tasks = []
        
    def add_task(self, task):
        if isinstance(task, Task):  
            self.tasks.append(task)
        else:
            raise ValueError("Добавляемый объект должен быть экземпляром Task.")
        
    def remove_task(self, task):
        if isinstance(task, Task): 
            if task in self.tasks:
                self.tasks.remove(task)
            else:
                raise ValueError("Задача не найдена.")
        else:
            raise ValueError("Удаляемый объект должен быть экземпляром Task.")
            
    def assign_user_to_task(self, user, task):
        if isinstance(user, User) and isinstance(task, Task): 
            if task in self.tasks:
                task.assign_user(user)
                if user not in self.users:
                    self.users.append(user)
            else:
                raise ValueError("Задача не найдена в проекте.")
        else:
            raise ValueError("Переданы некорректные объекты.")
