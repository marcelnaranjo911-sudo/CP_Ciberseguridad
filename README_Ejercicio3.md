## CP3 Ciberseguridad - Ejercicio 3: Validación y Escape de Entradas
Este repositorio ha sido actualizado (Rama ejercicio_3) para implementar mecanismos de control de flujo y saneamiento de datos en la frontera de la aplicación, mitigando vectores de ataque como Inyección SQL y DoS (Denegación de Servicio).

## Cambios Realizados (Capa de Routes)
En esta fase, se ha fortalecido la interfaz de usuario (auth_routes.py) mediante:

Validación con Expresiones Regulares (Regex): Se filtran caracteres especiales en nombres de usuario y comandos.

Control de Longitud: Se establecieron límites estrictos (mínimos y máximos) para evitar desbordamientos de memoria o ataques de fuerza bruta con payloads masivos.

Patrón Fail-Fast: El sistema interrumpe la ejecución inmediatamente si detecta una entrada malformada, antes de procesar cualquier lógica en el controlador.

## Instrucciones de Prueba para el Profesor
Para verificar que las validaciones son efectivas, ejecute python run.py y realice las siguientes comprobaciones:

1. Prueba de Robustez (Usuario Inválido)
Entrada de Usuario: admin'-- o user!@#

Resultado esperado: El sistema debe imprimir [-] Error de Validación: El usuario debe ser alfanumérico y cerrar el programa. Esto demuestra que los caracteres de inyección son bloqueados en la entrada.

2. Prueba de Control de Longitud (Protección DoS)
Entrada de Password: (Escriba algo muy corto, menos de 8 caracteres).

Resultado esperado: El sistema rechaza la entrada indicando que la longitud es insuficiente.

3. Prueba de Flujo Completo (Validación + Privilegios)
Acceso: Loguearse como admin con la contraseña correcta.

Comando: Escriba un comando con símbolos como check;ls o 1+1.

Resultado esperado: La capa de routes bloqueará el comando por formato inválido. Si intenta un comando válido pero no autorizado (ej: delete_logs), la capa del controller (Ejercicio 2) lo bloqueará.

## Archivos Modificados
app/routes/auth_routes.py: Se añadieron las funciones validate_username, validate_password y validate_command.
