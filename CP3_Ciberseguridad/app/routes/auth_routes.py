from app.controllers.auth_controller import AuthController

def start_auth_flow():
    auth = AuthController()
    print("=== SISTEMA DE AUTENTICACIÓN SEGURO v1.0 ===")
    

    user_in = input("Usuario: ")
    pass_in = input("Contraseña: ")
    
    user = auth.attempt_login(user_in, pass_in)
    
    if user:
        print(f"\n[+] Acceso concedido: {user.username} (Rol: {user.role})")
        if user.role == "admin":
    
            print("\n--- Consola de Diagnóstico (Solo Admin) ---")
            cmd = input("Ejecutar comando interno: ")
            print(f"Resultado: {auth.run_system_diagnostic(cmd)}")
    else:
        print("\n[-] Credenciales inválidas.")