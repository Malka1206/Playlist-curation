import librosa
import numpy as np
import matplotlib.pyplot as plt

# Charger un fichier audio
y, sr = librosa.load("chemin/vers/fichier_audio.wav")

# Calculer le spectrogramme en magnitude avec la STFT
stft = np.abs(librosa.stft(y))

# Normalisation : division par la somme des magnitudes par trame pour obtenir Nt[n]
stft_norm = stft / np.sum(stft, axis=0, keepdims=True)

# Calcul du flux spectral (différence au carré entre trames successives)
spectral_flux = np.sum((np.diff(stft_norm, axis=1))**2, axis=0)

# Affichage du flux spectral
plt.figure(figsize=(10, 4))
plt.plot(spectral_flux, label="Flux Spectral", color="b")
plt.xlabel("Trame (Time Frame)")
plt.ylabel("Amplitude")
plt.title("Flux Spectral du signal audio")
plt.legend()
plt.show()
