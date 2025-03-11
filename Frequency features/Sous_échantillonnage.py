import numpy as np
import librosa
import soundfile as sf

def downsample_audio(signal, factor):
    """Sous-échantillonne un signal audio en conservant un échantillon sur 'factor'."""
    return signal[::factor]

# Charger un fichier audio
file_path = "chemin/vers/fichier.wav"
y, sr = librosa.load(file_path, sr=None)  # Charger le signal avec sa fréquence d'échantillonnage

# Définir le facteur de sous-échantillonnage (ex: k = 2 réduit la fréquence de moitié)
k = 2
y_downsampled = downsample_audio(y, k)
sr_downsampled = sr // k  # Nouvelle fréquence d'échantillonnage

# Sauvegarder le fichier sous-échantillonné
sf.write("fichier_sous_echantillonne.wav", y_downsampled, sr_downsampled)

#utiliser k=16
