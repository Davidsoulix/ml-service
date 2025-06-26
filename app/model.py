import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer

def cargar_modelo():
    modelo_path = os.path.join("model", "modelo_entrenado.pkl")
    return joblib.load(modelo_path)

def clasificar_solicitud(modelo, datos):
    texto = datos.solicitud.lower()
    return modelo.predict([texto])[0]
