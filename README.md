# CP3 Ciberseguridad - Auditoría de Sistemas

Este proyecto consiste en un sistema de autenticación modular (MVC/Service) desarrollado en Python, diseñado específicamente para prácticas de auditoría de seguridad, análisis de diseño y gestión de vulnerabilidades.

##  Estructura del Proyecto
El repositorio sigue un patrón de diseño por capas:
- `app/routes/`: Interfaz de usuario y flujos de entrada.
- `app/controllers/`: Lógica de control y orquestación.
- `app/services/`: Lógica de negocio y persistencia simulada.
- `app/models/`: Definición de objetos de datos.

##  Requisitos del Sistema
Para garantizar la reproducibilidad (según lo exigido en la CP3), se requieren las siguientes versiones de librerías (especificadas en `requirements.txt`):
- **Flask**: 2.0.1
- **Requests**: 2.25.1
- **Jinja2**: 3.0.0

##  Instalación y Uso

1. Clonar o descargar** el repositorio en su máquina local.

2. Crear un entorno virtual** para aislar las dependencias:
   ```bash
   python -m venv venv
   Activar el entorno:

Windows: .\venv\Scripts\activate
Linux/Mac: source venv/bin/activate

3. Instalar dependencias:
Bash
pip install -r requirements.txt

4. Ejecutar la aplicación:
Bash
python run.py

## Herramientas de Auditoría Utilizadas
Este proyecto está preparado para ser analizado con:

Bandit: Para Análisis Estático de Seguridad (SAST).

Pylint: Para calidad de código y errores sintácticos.

Pip-audit: Para detección de vulnerabilidades en dependencias.
