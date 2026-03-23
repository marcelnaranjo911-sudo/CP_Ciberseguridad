from app.services.user_service import UserService

class AuthController:
    def __init__(self):
        self.service = UserService()
        
        self.allowed_diagnostics = {
            "check_status": "Sistema Operativo: Online",
            "get_version": "Versión de la App: 1.1 (Security Patch applied)"
        }

    def attempt_login(self, username, password):
        return self.service.authenticate(username, password)

    def run_system_diagnostic(self, command):
       
        return self.allowed_diagnostics.get(command, "Error: Comando no autorizado o inexistente.")
