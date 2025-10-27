from config.google_config import get_sheet_by_key
from config.columnas_bitacora import COLUMNAS_BITACORA


def guardar_bitacora(data: dict):
    """Guarda los datos en la hoja de Bitácora."""
    sheet = get_sheet_by_key("BITACORA")
    valores = [data.get(col, "") for col in COLUMNAS_BITACORA]
    sheet.append_row(valores)
    return {"status": "ok", "mensaje": "Registro guardado en Bitácora ✅"}
