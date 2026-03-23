## CP3 Ciberseguridad - Ejercicio 5: Análisis Estático y Calidad de Código (SAST)
Este repositorio ha sido actualizado (Rama **ejercicio_5**) para integrar el uso de herramientas automatizadas de análisis de código, cumpliendo con las prácticas de auditoría continua.

## Herramientas Utilizadas
* **Bandit:** Ejecutado para realizar un análisis SAST (Static Application Security Testing) en busca de vulnerabilidades en la sintaxis y lógica de Python (ej. uso de funciones inseguras, credenciales hardcodeadas).
* **Pylint:** Utilizado para analizar la robustez, convenciones de codificación y posibles errores lógicos que afecten la mantenibilidad del proyecto.

## Resultados
Los reportes generados por ambas herramientas se han exportado y adjuntado a este repositorio:
* `bandit_report.json`: Contiene los hallazgos de seguridad estructurados.
* `pylint_report.txt`: Contiene el puntaje de calidad y las recomendaciones de refactorización.

El análisis detallado de los hallazgos más críticos, junto con sus propuestas de remediación, se encuentra documentado en el informe técnico (Word) entregado junto a esta práctica.
