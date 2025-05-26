#passe_bas
def lowpass_filter(signal, alpha=0.99):
    """Applique un filtre passe-bas récursif sur un signal audio."""
    filtered_signal = np.zeros_like(signal)
    filtered_signal[0] = signal[0]  # Initialisation

    for n in range(1, len(signal)):
        filtered_signal[n] = (1 - alpha) * signal[n] + alpha * filtered_signal[n - 1]

    return filtered_signal

# Charger un fichier audio
file_path = "C:\\Users\\MSI\\Desktop\\TELECOM\\Artishow\\playlist-curation\\Frequency features\\hiphop.00005.au"
y, sr = librosa.load(file_path, sr=None)

# Appliquer la rectification en onde complète
rectified_signal = np.abs(y)

# Appliquer le filtrage passe-bas
smoothed_envelope = lowpass_filter(rectified_signal, alpha=0.99)


#sous_echantillonnage
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



#rectification_onde_complete
import librosa
import numpy as np
import matplotlib.pyplot as plt

# Charger un fichier audio
y, sr = librosa.load("C:\\Users\\MSI\\Desktop\\TELECOM\\Artishow\\playlist-curation\\Frequency features\\hiphop.00005.au")

# Étape 1 : Rectification en onde complète
rectified_signal = np.abs(y)

# Étape 2 : Filtrage passe-bas pour lisser l'enveloppe
# On utilise une convolution avec une fenêtre de moyennage
window_size = int(0.01 * sr)  # Fenêtre de lissage de 10 ms
window = np.ones(window_size) / window_size  # Fenêtre moyenne
envelope = np.convolve(rectified_signal, window, mode='same')


#suppression_moyenne
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
