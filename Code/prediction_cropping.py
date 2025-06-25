import joblib
import numpy as np
from Création_vecteur import extraction_features
from pydub import AudioSegment

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
chemin_audio = "C:\\Users\\Administrateur\\Downloads\\Eminem - Houdini (Lyrics).wav"
chemin_audio = crop_audio(chemin_audio,chemin_audio+"cropped"+str(duration_seconds),start_seconds,duration_seconds)
genre_pred = predire_genre(chemin_audio)
print(f"Le genre prédit est : {genre_pred}")