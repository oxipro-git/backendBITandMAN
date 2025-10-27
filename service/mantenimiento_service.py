from config.google_config import get_sheet_by_key
from config.columnas_mantenimiento import COLUMNAS_MANTENIMIENTO
from datetime import datetime


def guardar_mantenimiento(nombre_tecnico: str, data: dict):
    """Guarda los datos en la hoja del técnico correspondiente."""
    sheet = get_sheet_by_key(nombre_tecnico)
    valores = [data.get(col, "") for col in COLUMNAS_MANTENIMIENTO]
    valores[-1] = datetime.now().isoformat()  # timestamp_backend
    sheet.append_row(valores)
    return {"status": "ok", "mensaje":
            f"Datos guardados en hoja de {nombre_tecnico}"}
