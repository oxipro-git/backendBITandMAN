from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from service.mantenimiento_service import guardar_mantenimiento
from service.bitacora_service import guardar_bitacora

app = FastAPI()

# ✅ Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",  # para pruebas locales
        "https://frontend-oxipro.onrender.com"  # si luego subes el
        # front a Render
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"mensaje": "Backend unificado funcionando ✅"}


@app.post("/guardar/mantenimiento/")
def guardar_mantenimiento_api(data: dict):
    tecnico = data.get("nombre_tecnico")
    if not tecnico:
        return {"status": "error", "mensaje":
                "Falta el campo 'nombre_tecnico'"}
    return guardar_mantenimiento(tecnico, data)


@app.post("/guardar/bitacora/")
def guardar_bitacora_api(data: dict):
    return guardar_bitacora(data)
