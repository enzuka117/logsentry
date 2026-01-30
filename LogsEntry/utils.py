import yaml
import os

def cargar_patrones(ruta="patterns.yaml"):
    # Obtener la carpeta actual donde está este archivo utils.py
    base_dir = os.path.dirname(__file__)

    # Construir ruta absoluta al YAML
    ruta_completa = os.path.join(base_dir, ruta)

    # Cargar YAML
    with open(ruta_completa, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
