import librosa
import numpy as np
import matplotlib.pyplot as plt

y, sr = librosa.load("chemin/vers/fichier_audio.wav")

zero_crossings = librosa.feature.zero_crossing_rate(y)[0]

plt.figure(figsize=(10, 4))
plt.plot(zero_crossings, label="Passages par zéro", color="r")
plt.xlabel("Trame (Time Frame)")
plt.ylabel("Taux de passage par zéro")
plt.title("Taux de passages par zéro du signal audio")
plt.legend()
plt.show()
