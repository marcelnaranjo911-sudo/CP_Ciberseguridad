from app.models.user_model import User

class UserService:
    def __init__(self):
        
        self.users = [
            User(1, "admin", "P4ssw0rd!_Admin", "admin"),
            User(2, "marcel", "estudiante_2026", "user")
        ]

    def authenticate(self, username, password):
        
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None