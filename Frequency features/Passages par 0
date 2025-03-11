import librosa
import numpy as np
import matplotlib.pyplot as plt

# Charger un fichier audio
y, sr = librosa.load("chemin/vers/fichier_audio.wav")

# Calculer le taux de passage par zéro
zero_crossings = librosa.feature.zero_crossing_rate(y)[0]

# Affichage du taux de passage par zéro
plt.figure(figsize=(10, 4))
plt.plot(zero_crossings, label="Passages par zéro", color="r")
plt.xlabel("Trame (Time Frame)")
plt.ylabel("Taux de passage par zéro")
plt.title("Taux de passages par zéro du signal audio")
plt.legend()
plt.show()
