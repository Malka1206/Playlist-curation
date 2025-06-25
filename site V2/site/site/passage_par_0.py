import librosa
import numpy as np
import matplotlib.pyplot as plt


def compute_passage_0(y,sr):
    # Calculer le taux de passage par zéro
    zero_crossings = librosa.feature.zero_crossing_rate(y)[0]

    # Extraire les caractéristiques
    mean_zcr = np.mean(zero_crossings)

    var_zcr = 0 
    for i in range(len(zero_crossings)):
        var_zcr= (zero_crossings[i]-mean_zcr)**2
    
    return var_zcr, mean_zcr
