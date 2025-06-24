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
    features = extraction_features(fichier_audio)
    features = np.array(features).reshape(1, -1)
    features_scaled = scaler.transform(features)

    # Obtenir les probabilités pour chaque classe
    probs = model.predict_proba(features_scaled)

    # Associer chaque genre à sa probabilité
    genre_probs = dict(zip(label_encoder.classes_, probs[0]))

    return genre_probs

# Exemple d'utilisation
chemin_audio = "C:\\Users\\MSI\\Downloads\\Le lac des cygnes ( Tchaikovski ).wmv.wav"
genre_probs = predire_genre(chemin_audio)
print(f"Les probas des genres sont : {genre_probs}")