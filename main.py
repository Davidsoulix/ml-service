from fastapi import FastAPI
from app.schemas import SolicitudInput
from app.model import cargar_modelo, clasificar_solicitud
from app import db

app = FastAPI()
modelo = cargar_modelo()

@app.post("/clasificar")
def clasificar(data: SolicitudInput):
    tipo = clasificar_solicitud(modelo, data)

    id_tipo = db.obtener_id_tipo_cliente(tipo)
    if id_tipo is None:
        return {"error": f"Tipo de cliente '{tipo}' no encontrado."}

    id_cliente = db.obtener_id_cliente(data.correo)
    if not id_cliente:
        id_cliente = db.crear_cliente(data.nombre, data.empresa, data.correo)

    db.crear_solicitud(data.solicitud, id_cliente, id_tipo)

    return {
        "nombre": data.nombre,
        "correo": data.correo,
        "empresa": data.empresa,
        "tipo_cliente": tipo,
        "status": "Solicitud registrada correctamente"
    }
