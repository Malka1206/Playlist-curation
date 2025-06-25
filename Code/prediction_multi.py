import joblib
import numpy as np
from Création_vecteur import extraction_features
import time

# Charger le modèle, le scaler et le label encoder
model = joblib.load("xgb_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

def extraire_features(fichier_audio):
    return extraction_features(fichier_audio)

def predire_genres_tries(fichier_audio):
    features = extraire_features(fichier_audio)
    features = np.array(features).reshape(1, -1)
    features_scaled = scaler.transform(features)

    # Obtenir les probabilités
    probs = model.predict_proba(features_scaled)[0]
    genre_probs = dict(zip(label_encoder.classes_, probs))

    # Filtrer les genres avec proba > 0.3
    genres_filtres = {genre: p for genre, p in genre_probs.items() if p > 0.3}

    # Si 0 ou 1 genre, relâcher le seuil
    if len(genres_filtres) <= 1:
        proba_max = max(probs)
        seuil = proba_max - 0.1
        genres_filtres = {genre: p for genre, p in genre_probs.items() if p >= seuil}

    # Trier par probabilité décroissante
    genres_tries = sorted(genres_filtres.items(), key=lambda x: x[1], reverse=True)

    return [str(genre) for genre, _ in genres_tries]

# Exemple d'utilisation
"""chemin_audio="C:\\Users\\Administrateur\\Downloads\\musics_actuel\\Eminem - Houdini (Lyrics).wav"
chemin_audio = "C:\\Users\\MSI\\Downloads\\Eminem - Houdini [Official Music Video].wav
print(predire_genres_tries(chemin_audio))"""
