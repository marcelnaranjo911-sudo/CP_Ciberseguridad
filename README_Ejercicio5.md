# CP3 Ciberseguridad - Ejercicio 5: Análisis Estático y Calidad de Código (SAST)

Este repositorio ha sido actualizado (Rama `ejercicio_5`) para integrar el uso de herramientas automatizadas de análisis de código, cumpliendo con las prácticas de auditoría continua y desarrollo seguro (Secure by Design).

## Estructura de la Auditoría (Before & After)
Para demostrar la evolución de la seguridad del código, se ha incluido una comparativa del estado del proyecto:

* **Before (Rama `main` inicial):** En la carpeta `/audit_before` se encuentran los reportes generados sobre el código base vulnerable (donde se detectaba el uso crítico de `eval()`).
* **After (Rama actual `ejercicio_5`):** En la raíz del proyecto se encuentran los reportes actualizados tras aplicar mitigaciones de seguridad (validaciones Regex, listas blancas de comandos).

## Herramientas Utilizadas

1.  **Bandit:** Ejecutado para realizar un análisis SAST (Static Application Security Testing). Ha validado con éxito la eliminación de vulnerabilidades críticas (RCE), reportando ahora únicamente problemas residuales de diseño (ej. contraseñas hardcodeadas).
2.  **Pylint:** Utilizado para analizar la robustez, convenciones de codificación y deuda técnica que pueda afectar la mantenibilidad a largo plazo del proyecto.

## Resultados

Los reportes finales generados se han exportado y adjuntado a este repositorio:
*  `bandit_report.json`: Contiene los hallazgos de seguridad estructurados.
*  `pylint_report.txt`: Contiene el puntaje de calidad y las recomendaciones de refactorización.

El análisis detallado de los hallazgos actuales, junto con sus propuestas de remediación para futuros sprints, se encuentra documentado en el informe técnico (Word) entregado junto a esta práctica.
