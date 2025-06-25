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
    # Extraire les features
    features = extraire_features(fichier_audio)
    features = np.array(features).reshape(1, -1)
    features_scaled = scaler.transform(features)

    # Obtenir les probabilités
    probs = model.predict_proba(features_scaled)[0]
    genre_probs = dict(zip(label_encoder.classes_, probs))

    # Trier les genres par probabilité décroissante
    genre_probs_tries = dict(sorted(genre_probs.items(), key=lambda item: item[1], reverse=True))

    return genre_probs_tries

def crop_audio(input_file, output_file, start_seconds, duration_seconds):
    audio = AudioSegment.from_file(input_file)
    start_time = start_seconds * 1000
    end_time = (start_seconds + duration_seconds) * 1000
    cropped_audio = audio[start_time:end_time]
    cropped_audio.export(output_file, format="mp3")
    return output_file

# Exemple d'utilisation
chemin_audio = "C:\\Users\\MSI\\Desktop\\TELECOM\\Artishow\\playlist-curation\\test_cropping\\country.wav"
# Charger l'audio pour obtenir sa durée totale
y, sr = librosa.load(chemin_audio, sr=None)
total_duration = librosa.get_duration(y=y, sr=sr)

# Exemple d'utilisation
for duration_seconds in (5, 10, 20, 30, 60,int(total_duration)):
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

    print("La durée totale de la chanson est :" + str(total_duration))
    print(f"Temps d'exécution pour {duration_seconds} secondes : {elapsed_time:.2f} secondes")
    print(f"Genre prédit pour {duration_seconds} secondes : {genre_pred}\n")