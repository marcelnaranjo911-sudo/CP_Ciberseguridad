# CP3 Ciberseguridad - Auditoría de Sistemas (Ejercicio 2)

Este repositorio ha sido actualizado para aplicar el **Principio de Menor Privilegio**, eliminando vulnerabilidades de ejecución crítica y restringiendo el acceso según roles.

## Cambios Realizados (Ejercicio 2)
- **Eliminación de `eval()`**: Se suprimió la ejecución de funciones arbitrarias en `auth_controller.py`.
- **Implementación de Whitelist**: El administrador ahora solo puede ejecutar comandos pre-aprobados.
- **Segregación de Roles**: Los usuarios estándar no tienen acceso a la consola de diagnóstico.

## Requisitos del Sistema
Para garantizar la reproducibilidad (CP3), se requieren:
- **Flask**: 2.0.1 | **Requests**: 2.25.1 | **Jinja2**: 3.0.0

## Instalación y Uso
1. **Crear entorno virtual**: `python -m venv venv`
2. **Activar entorno**: 
   - Windows: `.\venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
3. **Instalar dependencias**: `pip install -r requirements.txt`
4. **Ejecutar**: `python run.py`

## Instrucciones de Prueba (Validación de Privilegios)
Para verificar que los servicios funcionan con permisos limitados, siga estos pasos:

### Prueba 1: Usuario Estándar (Restricción Total)
- **Credenciales**: Usuario: `marcel` | Pass: `estudiante_2026`
- **Resultado esperado**: El sistema permite el acceso pero **finaliza la ejecución** tras el login. No se muestra la consola de diagnóstico, confirmando que el usuario no tiene privilegios excesivos.

### Prueba 2: Administrador (Privilegio Mínimo)
- **Credenciales**: Usuario: `admin` | Pass: `P4ssw0rd!_Admin`
- **Acción**: Introducir el comando `check_status`.
- **Resultado esperado**: Devuelve "Sistema Operativo: Online". El servicio funciona, pero está limitado a la lista blanca.

### Prueba 3: Intento de Inyección (Bloqueo de RCE)
- **Acción (como admin)**: Intentar ejecutar un comando no autorizado (ej: `1+1` o `os.system`).
- **Resultado esperado**: El sistema devuelve "Error: Comando no autorizado", demostrando que la vulnerabilidad `eval()` ha sido mitigada satisfactoriamente.
