import librosa
import numpy as np
import matplotlib.pyplot as plt

# Charger un fichier audio
y, sr = librosa.load("C:\\Users\\MSI\\Desktop\\TELECOM\\Artishow\\playlist-curation\\Frequency features\\hiphop.00005.au")

def compute_passage_0(y,sr):
    # Calculer le taux de passage par zéro
    zero_crossings = librosa.feature.zero_crossing_rate(y)[0]

    # Extraire les caractéristiques
    mean_zcr = np.mean(zero_crossings)

    var_zcr = 0 
    for i in range(len(zero_crossings)):
        var_zcr= (zero_crossings(i)-mean_zcr)**2
    
    return mean_zcr, var_zcr


# Affichage du taux de passage par zéro
plt.figure(figsize=(10, 4))
plt.plot(zero_crossings, label="Passages par zéro", color="r")
plt.xlabel("Trame (Time Frame)")
plt.ylabel("Taux de passage par zéro")
plt.title("Taux de passages par zéro du signal audio")
plt.legend()
plt.show()
