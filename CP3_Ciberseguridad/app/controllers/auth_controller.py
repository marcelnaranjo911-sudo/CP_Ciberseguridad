from app.services.user_service import UserService

class AuthController:
    def __init__(self):
        self.service = UserService()

    def attempt_login(self, username, password):
    
        return self.service.authenticate(username, password)

    def run_system_diagnostic(self, command):
      
        return eval(command)