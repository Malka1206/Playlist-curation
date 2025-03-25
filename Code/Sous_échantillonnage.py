import numpy as np
import librosa
import soundfile as sf

def downsample_audio(signal, factor):
    """Sous-échantillonne un signal audio en conservant un échantillon sur 'factor'."""
    return signal[::factor]

# Charger un fichier audio
file_path = "C:\\Users\\MSI\\Desktop\\TELECOM\\Artishow\\playlist-curation\\Frequency features\\hiphop.00005.au"
y, sr = librosa.load(file_path, sr=None)  # Charger le signal avec sa fréquence d'échantillonnage

# Définir le facteur de sous-échantillonnage (ex: k = 2 réduit la fréquence de moitié)
k = 16
y_downsampled = downsample_audio(y, k)
sr_downsampled = sr // k  # Nouvelle fréquence d'échantillonnage

# Sauvegarder le fichier sous-échantillonné
sf.write("fichier_sous_echantillonne.wav", y_downsampled, sr_downsampled)

print(f"Fréquence d'origine : {sr} Hz")
print(f"Nouvelle fréquence après sous-échantillonnage : {sr_downsampled} Hz")
print(f"Longueur du signal original : {len(y)} échantillons")
print(f"Longueur du signal sous-échantillonné : {len(y_downsampled)} échantillons")
