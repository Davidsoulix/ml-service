from pydantic import BaseModel

class SolicitudInput(BaseModel):
    nombre: str
    correo: str
    empresa: str
    solicitud: str
