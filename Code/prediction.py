import joblib
import numpy as np
from Création_vecteur import extraction_features

# Charger le modèle, le scaler et le label encoder
model = joblib.load("xgb_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

def extraire_features(fichier_audio):
    return extraction_features(fichier_audio)

def predire_genre(fichier_audio):
    # Extraire les features
    features = extraire_features(fichier_audio)
    features = np.array(features).reshape(1, -1)

    # Normaliser les features
    features_scaled = scaler.transform(features)

    # Prédire le genre
    prediction = model.predict(features_scaled)

    # Convertir l'étiquette en genre
    genre = label_encoder.inverse_transform(prediction)
    return genre[0]

# Exemple d'utilisation
chemin_audio = "C:\\Users\\Administrateur\\Downloads\\musics_actuel\\Eminem - Houdini (Lyrics).wav"
genre_pred = predire_genre(chemin_audio)
print(f"Le genre prédit est : {genre_pred}")