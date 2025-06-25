import joblib
import numpy as np
from Création_vecteur import extraction_features
from pydub import AudioSegment
import time
import librosa

# Charger le modèle, le scaler et le label encoder
model = joblib.load("xgb_multi.pkl")
scaler = joblib.load("scaler_multi.pkl")
label_encoder = joblib.load("label_encoder_multi.pkl")

def extraire_features(fichier_audio):
    return extraction_features(fichier_audio)

def predire_genre(fichier_audio):
    y, sr = librosa.load(fichier_audio, sr=None)
    total_duration = librosa.get_duration(y=y, sr=sr)
    start_seconds = max(0, (total_duration - 30) / 2)
    chemin_audio_cropped = fichier_audio + "_cropped_" + str(30) + ".wav"
    chemin_audio_cropped = crop_audio(fichier_audio, chemin_audio_cropped, start_seconds, 30)
    # Extraire les features
    features = extraire_features(chemin_audio_cropped)
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
        
    # Trier les genres par probabilité décroissante
    genre_probs_tries = dict(sorted(genres_filtres.items(), key=lambda item: item[1], reverse=True))

    return genre_probs_tries

def crop_audio(input_file, output_file, start_seconds, duration_seconds):
    audio = AudioSegment.from_file(input_file)
    start_time = start_seconds * 1000
    end_time = (start_seconds + duration_seconds) * 1000
    cropped_audio = audio[start_time:end_time]
    cropped_audio.export(output_file, format="mp3")
    return output_file