from user import User

class Task:
    def __init__(self, title):
        self.title = title
        self.status = 'Новая'
        self.assigned_users = [] 
        
    def update_status(self, status):
        self.status = status
        
    def assign_user(self, user):
        if isinstance(user, User):  
            if user not in self.assigned_users:
                self.assigned_users.append(user)  
                user.assign_task(self)  
            else:
                raise ValueError("Пользователь уже назначен на эту задачу.")
        else:
            raise ValueError("Переданный объект должен быть экземпляром User.")