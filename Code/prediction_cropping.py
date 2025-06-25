import joblib
import numpy as np
from Création_vecteur import extraction_features
from pydub import AudioSegment
import librosa
import time

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

chemin_audio = "C:\\Users\\MSI\\Downloads\\classique.wav"

# Exemple d'utilisation
for duration_seconds in (10, 20, 30, 60):
    # Charger l'audio pour obtenir sa durée totale
    y, sr = librosa.load(chemin_audio, sr=None)
    total_duration = librosa.get_duration(y=y, sr=sr)
    
    # Calculer le point de départ
    start_seconds = max(0, (total_duration - duration_seconds) / 2)

    # Découper l'audio
    chemin_audio_cropped = chemin_audio + "_cropped_" + str(duration_seconds) + ".wav"
    chemin_audio_cropped = crop_audio(chemin_audio, chemin_audio_cropped, start_seconds, duration_seconds)

    # Mesure du temps de prédiction
    start_time = time.time()
    genre_pred = predire_genre(chemin_audio_cropped)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Temps d'exécution pour {duration_seconds} secondes : {elapsed_time:.2f} secondes")
    print(f"Genre prédit pour {duration_seconds} secondes : {genre_pred}\n")

print(f"Temps d'exécution pour {duration_seconds} secondes : {elapsed_time:.2f} secondes")
print(f"Genre prédit pour {duration_seconds} secondes : {genre_pred}\n")