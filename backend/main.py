from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
from datetime import datetime

app = FastAPI(title="Servidor de Control - Proyecto Phantom")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conexión interna hacia el contenedor de MongoDB
try:
    client = MongoClient("mongodb://mongodb:27017/", serverSelectionTimeoutMS=2000)
    db = client["robotics_logs_db"]
    collection = db["logs"]
except Exception as e:
    print(f"Error de conexión a MongoDB: {e}")

# Variable global para almacenar el comando en espera que leerá tu Arduino
ultimo_comando = "esperar"

class EventModel(BaseModel):
    componente: str
    accion: str
    estado: str

# 1. Este endpoint lo sigue usando tu Dashboard Web para mandar acciones fijas desde la página
@app.post("/api/events")
async def registrar_evento(event: EventModel):
    global ultimo_comando
    try:
        log_entry = event.dict()
        log_entry["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Guardamos en MongoDB para la tabla del Frontend
        result = collection.insert_one(log_entry)
        
        # Seteamos el comando para que el Arduino lo recoja en su próximo loop
        # Si mandas desde la web una acción, la usamos como comando directo
        ultimo_comando = event.accion
        
        return {"status": "success", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en BD: {e}")

# 2. ¡EL ENDPOINT CLAVE PARA TU ARDUINO! 
# Responde exactamente al GET que hace tu placa en la ruta '/leer_comando'
@app.get("/leer_comando")
async def leer_comando():
    global ultimo_comando
    # Guardamos temporalmente el comando actual para responderle al Arduino
    comando_a_retornar = ultimo_comando
    
    # Una vez que el Arduino lo lea, restauramos a "esperar" para que no repita el movimiento
    ultimo_comando = "esperar"
    
    return {"comando": comando_a_retornar}

# 3. El Frontend sigue usando este para listar el historial en la tabla
@app.get("/api/events")
async def obtener_eventos():
    try:
        logs = list(collection.find({}, {"_id": 0}).sort("timestamp", -1).limit(50))
        return logs
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al leer BD: {e}")

@app.get("/health")
async def health_check():
    return {"status": "online"}