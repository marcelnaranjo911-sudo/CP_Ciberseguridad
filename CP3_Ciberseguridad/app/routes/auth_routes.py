from app.controllers.auth_controller import AuthController

def start_auth_flow():
    auth = AuthController()
    print("=== SISTEMA DE GESTIÓN CON PRIVILEGIOS LIMITADOS v1.1 ===")
    
    user_in = input("Usuario: ")
    pass_in = input("Contraseña: ")
    
    user = auth.attempt_login(user_in, pass_in)
    
    if user:
        print(f"\n[+] Sesión iniciada como: {user.username}")
        if user.role == "admin":
        
            print("\n--- Consola de Diagnóstico Segura ---")
            print("Comandos disponibles: check_status, get_version")
            cmd = input("Comando > ")
            
            print(f"Resultado: {auth.run_system_diagnostic(cmd)}")
    else:
        print("\n[-] Credenciales inválidas.")
