import re
from app.controllers.auth_controller import AuthController

def validate_username(username):
   
    if not re.match(r"^[a-zA-Z0-9]{3,20}$", username):
        return False
    return True

def validate_password(password):
  
    if not (8 <= len(password) <= 64):
        return False
    return True

def validate_command(command):
   
    if not re.match(r"^[a-z_]{1,20}$", command):
        return False
    return True

def start_auth_flow():
    auth = AuthController()
    print("=== SISTEMA DE GESTIÓN CON PRIVILEGIOS LIMITADOS v1.2 ===")
    
    
    user_in = input("Usuario: ")
    if not validate_username(user_in):
        print("[-] Error de Validación: El usuario debe ser alfanumérico (3-20 caracteres).")
        return
        
    pass_in = input("Contraseña: ")
    if not validate_password(pass_in):
        print("[-] Error de Validación: La contraseña debe tener entre 8 y 64 caracteres.")
        return 
    
    user = auth.attempt_login(user_in, pass_in)
    
    if user:
        print(f"\n[+] Sesión iniciada como: {user.username}")
        if user.role == "admin":
            print("\n--- Consola de Diagnóstico Segura ---")
            print("Comandos disponibles: check_status, get_version")
            cmd = input("Comando > ")
            
    
            if not validate_command(cmd):
                print("[-] Error de Validación: Formato de comando no permitido.")
            else:
                print(f"Resultado: {auth.run_system_diagnostic(cmd)}")
    else:
        print("\n[-] Credenciales inválidas.")
