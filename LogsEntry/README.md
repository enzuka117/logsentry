# Analizador de Logs de Apache

Este proyecto es un analizador básico de archivos de registro (`apache.log`) utilizado para extraer información útil sobre accesos, errores, IPs frecuentes y patrones de tráfico.  
Es una versión funcional para pruebas, pero fácilmente modificable para uso empresarial.

---

# ¿Qué hace este programa?

El script analiza un archivo `apache.log` y extrae:

- Total de solicitudes realizadas.
- IPs que más acceden al servidor.
- Conteo de respuestas 404 (errores de página no encontrada).
- Estadísticas de métodos HTTP utilizados (GET, POST, etc).
- Estadísticas de códigos de estado (200, 404, 500…).

Estos datos permiten entender comportamiento de usuarios, tráfico, errores y seguridad básica.

---

Requisitos

Instala dependencias con:

pip install -r requirements.txt


---

# Cómo usar el programa

1. Coloca tu archivo `apache.log` en la misma carpeta que el script.
2. Asegúrate de que el archivo se llama exactamente: apache.log

3. ejecuta el script: python logsentry.py

4. El programa leerá el log, lo analizará y mostrará en pantalla:

- Cantidad total de registros.
- Las IPs más frecuentes.
- Cantidad de errores 404.
- Estadísticas generales.

---

## Uso en un entorno empresarial

Para convertir este programa en una herramienta real debes:

###  1. Reemplazar el archivo de prueba  
Usar rutas reales como: /var/log/apache2/access.log


###  2. Agregar más validaciones  
Como manejar logs rotados:  

access.log.1
access.log.2.gz

###  3. Agregar visualizaciones gráficas  
Gráficas de tráfico diario, errores, IPs sospechosas, etc.

###  4. Conectarlo con bases de datos (opcional)
Enviar resultados a:

- MySQL  
- PostgreSQL  
- MongoDB  

###  5. Ejecutarlo automáticamente  
Con cron jobs:
crontab -e
0 * * * * python analizador.py



---

## © enzuka117

Proyecto creado como ejemplo para análisis básico de logs de Apache.
