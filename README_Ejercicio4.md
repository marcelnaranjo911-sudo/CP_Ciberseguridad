## CP3 Ciberseguridad - Ejercicio 4: Gestión de Dependencias y Auditoría
Este repositorio ha sido actualizado (Rama ejercicio_4) para implementar técnicas de auditoría de dependencias, asegurando que los paquetes de terceros (Flask, Requests, Jinja2, etc.) no contengan vulnerabilidades conocidas (CVE) que puedan comprometer el sistema.

## Cambios Realizados (Seguridad en Dependencias)
En esta fase, no se modificó la lógica del código, sino que se integró una capa de análisis de composición de software (SCA) mediante:

Auditoría con pip-audit: Se utilizó la herramienta para escanear el archivo requirements.txt contra la base de datos de vulnerabilidades de Python (PyPA) y el OSV (Open Source Vulnerabilities).

Generación de Reportes: Se automatizó la creación de un informe técnico en formato JSON para facilitar la revisión de riesgos críticos.

## Resultados de la Auditoría
Tras ejecutar el análisis, se identificaron los siguientes hallazgos críticos:

Vulnerabilidades detectadas: 17 fallos de seguridad conocidos.

Paquetes afectados: 5 librerías (incluyendo Flask y Jinja2).

Riesgos principales: El uso de versiones obsoletas en este entorno permite ataques de inyección de plantillas y denegación de servicio (DoS) por bombas de descompresión.

## Instrucciones para el Profesor
Para replicar la auditoría y revisar los fallos encontrados, siga estos pasos:

Revisar el Reporte Generado:
El detalle técnico de los CVE encontrados está disponible en el archivo:
CP3_Ciberseguridad/pip_audit_report.json

Ejecutar la Auditoría en Vivo:
Con el entorno virtual activado y las librerías instaladas, ejecute el siguiente comando en la terminal:

Bash
pip-audit -r requirements.txt
Resultado esperado: Una lista detallada de las 17 vulnerabilidades, sus códigos CVE y las versiones mínimas recomendadas para la corrección.

## Archivos Nuevos
CP3_Ciberseguridad/pip_audit_report.json: Informe completo de la auditoría de seguridad de las dependencias.
