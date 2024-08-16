from user import User
from project import Project
from task import Task


username = input("Добавьте пользователя: ")
task_title = input("Создайте задачу: ")
project_name = input("Имя проекта: ")


user1 = User(username)
task1 = Task(task_title)
project1 = Project(project_name)


project1.add_task(task1)
project1.assign_user_to_task(user1, task1)

print(f"Пользователь {user1.username} назначен на задачу {task1.title}")
