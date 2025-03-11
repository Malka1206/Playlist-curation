import numpy as np
import librosa

def lowpass_filter(signal, alpha=0.99):
    """Applique un filtre passe-bas récursif sur un signal audio."""
    filtered_signal = np.zeros_like(signal)
    filtered_signal[0] = signal[0]  # Initialisation

    for n in range(1, len(signal)):
        filtered_signal[n] = (1 - alpha) * signal[n] + alpha * filtered_signal[n - 1]

    return filtered_signal

# Charger un fichier audio
file_path = "chemin/vers/fichier.wav"
y, sr = librosa.load(file_path, sr=None)

# Appliquer la rectification en onde complète
rectified_signal = np.abs(y)

# Appliquer le filtrage passe-bas
smoothed_envelope = lowpass_filter(rectified_signal, alpha=0.99)
