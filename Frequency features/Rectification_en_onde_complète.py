import librosa
import numpy as np
import matplotlib.pyplot as plt

# Charger un fichier audio
y, sr = librosa.load("chemin/vers/fichier_audio.wav")

# Étape 1 : Rectification en onde complète
rectified_signal = np.abs(y)

# Étape 2 : Filtrage passe-bas pour lisser l'enveloppe
# On utilise une convolution avec une fenêtre de moyennage
window_size = int(0.01 * sr)  # Fenêtre de lissage de 10 ms
window = np.ones(window_size) / window_size  # Fenêtre moyenne
envelope = np.convolve(rectified_signal, window, mode='same')

# Affichage du signal original et de l'enveloppe
plt.figure(figsize=(12, 6))
plt.plot(y, label="Signal original", alpha=0.6)
plt.plot(envelope, label="Enveloppe temporelle (rectification + filtrage)", color='red', linewidth=2)
plt.xlabel("Temps (échantillons)")
plt.ylabel("Amplitude")
plt.title("Extraction de l'enveloppe temporelle par rectification en onde complète")
plt.legend()
plt.show()
