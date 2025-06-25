import joblib
import numpy as np
from Création_vecteur import extraction_features
from pydub import AudioSegment

# Charger le modèle, le scaler et le label encoder
model = joblib.load("xgb_multi.pkl")
scaler = joblib.load("scaler_multi.pkl")
label_encoder = joblib.load("label_encoder_multi.pkl")

def extraire_features(fichier_audio):
    return extraction_features(fichier_audio)

def predire_genre(fichier_audio):
    # Extraire les features
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

def crop_audio(input_file, output_file, start_seconds, duration_seconds):
    audio = AudioSegment.from_file(input_file)
    start_time = start_seconds * 1000
    end_time = (start_seconds + duration_seconds) * 1000
    cropped_audio = audio[start_time:end_time]
    cropped_audio.export(output_file, format="mp3")
    return output_file

# Exemple d'utilisation
duration_seconds = 10
start_seconds = 10
chemin_audio = "C:\\Users\\Administrateur\\Downloads\\musics_actuel\\Eminem - Houdini (Lyrics).wav"
chemin_audio = crop_audio(chemin_audio,chemin_audio+"cropped"+str(duration_seconds),start_seconds,duration_seconds)
genre_pred = predire_genre(chemin_audio)
print(f"Le genre prédit est : {genre_pred}")