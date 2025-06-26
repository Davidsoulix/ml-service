import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

X = [
    "Busco financiamiento para mi startup",
    "Necesito crear una tienda online con ayuda del kit digital",
    "Quiero hacer una campaña publicitaria SEO",
    "Necesito gestionar Instagram y TikTok de mi empresa",
    "Spam, no quiero nada"
]
y = ["venture", "kit digital", "marketing", "redes sociales", "otros"]

modelo = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])
modelo.fit(X, y)

joblib.dump(modelo, "model/modelo_entrenado.pkl")
