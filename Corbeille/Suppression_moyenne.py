import numpy as np

import librosa
import soundfile as sf

def remove_mean(signal):
    """Soustrait la moyenne du signal pour le centrer à zéro."""
    return signal - np.mean(signal)

# Charger un fichier audio
file_path = "C:\\Users\\MSI\\Desktop\\TELECOM\\Artishow\\playlist-curation\\Frequency features\\hiphop.00005.au"
y, sr = librosa.load(file_path, sr=None)  # Charger avec la fréquence d'échantillonnage originale

# Suppression de la moyenne
y_centered = remove_mean(y)

# Sauvegarder le fichier audio centré
sf.write("fichier_centre.wav", y_centered, sr)

# Vérification : la moyenne doit être proche de zéro
print("Moyenne du signal après centrage :", np.mean(y_centered))
