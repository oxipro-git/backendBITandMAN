import gspread
import os
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

CREDENTIALS_PATH = "/etc/secrets/credentials.json"

if not os.path.exists(CREDENTIALS_PATH):
    # fallback por si está en local
    CREDENTIALS_PATH = "credentials.json"

creds = Credentials.from_service_account_file(
    CREDENTIALS_PATH, scopes=SCOPE)

client = gspread.authorize(creds)

SHEETS_IDS = {
    # --- MANTENIMIENTO ---
    "BSGARCIA": "14HlbzFcqvLdFKlX-CDBA8hU-oJxwLbM4pLtFFE6ra-c",
    "JBUENO": "1N1G-c3NmrS6NZVqHB2IYkZYv-9p9vUwAWF7lxd01QJc",
    "MVARGAS": "1z8NwFBb4znL22oLWh79k4NUI9UYScWxMeN4ZldtX1HM",
    "EJE": "18VpRHRty1TPOzzSgNZpUyY5GyNn77YYUdC9SbNCPGC4",

    # --- BITÁCORA (actual) ---
    "BITACORA": "1D-DkH2Id3wyNTwSr7gklq0RdbUAy5NU4P__vIK0Jy60"
}


def get_sheet_by_key(key: str):
    """Devuelve la hoja de cálculo correspondiente al identificador
    (técnico o proyecto)."""
    sheet_id = SHEETS_IDS.get(key.upper())
    if not sheet_id:
        raise ValueError(f"Clave de hoja no registrada: {key}")
    return client.open_by_key(sheet_id).sheet1
