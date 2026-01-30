import re
from collections import Counter
from utils import cargar_patrones

#--------------------------------------------
# by enzuka117 - LogsEntry
# Análisis básico de archivos de log para detectar patrones sospechosos.
#prueba para repositorio parte 1

# --------------------------------------------
#   Leer archivo de log
# --------------------------------------------

def leer_log(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            yield linea.strip()


# --------------------------------------------
#   Extraer IP con regex
# --------------------------------------------

PATRON_IP = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

def extraer_ip(linea):
    match = re.search(PATRON_IP, linea)
    return match.group() if match else None


# --------------------------------------------
#   Detectar eventos sospechosos
# --------------------------------------------

def detectar_eventos(linea, patrones):
    eventos = []

    # User Agents sospechosos
    for ua in patrones.get("user_agents_sospechosos", []):
        if ua.lower() in linea.lower():
            eventos.append(f"User Agent sospechoso detectado: {ua}")

    # Rutas peligrosas o restringidas
    for ruta in patrones.get("rutas_prohibidas", []):
        if ruta in linea:
            eventos.append(f"Intento de acceso a ruta prohibida: {ruta}")

    # Códigos HTTP importantes
    for codigo in patrones.get("errores_interes", []):
        if f" {codigo} " in linea:
            eventos.append(f"Código HTTP sospechoso detectado: {codigo}")

    return eventos


# --------------------------------------------
#   Función principal
# --------------------------------------------

def analizar_log(ruta_log):
    patrones = cargar_patrones()
    ip_counter = Counter()
    eventos_sospechosos = []

    for linea in leer_log(ruta_log):
        
        # → Contar IPs
        ip = extraer_ip(linea)
        if ip:
            ip_counter[ip] += 1

        # → Detectar eventos
        eventos = detectar_eventos(linea, patrones)
        if eventos:
            eventos_sospechosos.append({
                "linea": linea,
                "eventos": eventos
            })

    return ip_counter.most_common(10), eventos_sospechosos


# --------------------------------------------
#   Ejecutar y mostrar resultados
# --------------------------------------------

import os

if __name__ == "__main__":
    base = os.path.dirname(__file__)
    ruta = os.path.join(base, "sample_logs", "apache.log")

    ips, eventos = analizar_log(ruta)

    print("\n=== TOP 10 IPs ===")
    for ip, count in ips:
        print(f"{ip} → {count} veces")

    print("\n=== EVENTOS SOSPECHOSOS ===")
    for evento in eventos:
        print(f"\nLínea: {evento['linea']}")
        for e in evento["eventos"]:
            print(f" - {e}")
