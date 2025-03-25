import librosa
import numpy as np
import matplotlib.pyplot as plt

y, sr = librosa.load("C:\\Users\\MSI\\Desktop\\TELECOM\\Artishow\\playlist-curation\\Frequency features\\hiphop.00005.au")

zero_crossings = librosa.feature.zero_crossing_rate(y)[0]

mean_zcr = np.mean(zero_crossings)  # Moyenne du taux de passages par zéro
var_zcr = np.var(zero_crossings)    # Variance du taux de passages par zéro

plt.figure(figsize=(10, 4))
plt.plot(zero_crossings, label="Passages par zéro", color="r")
plt.xlabel("Trame (Time Frame)")
plt.ylabel("Taux de passage par zéro")
plt.title("Taux de passages par zéro du signal audio")
plt.legend()
plt.show()