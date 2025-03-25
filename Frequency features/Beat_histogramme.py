import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

def compute_beat_histogram(audio_path, bpm_min=40, bpm_max=200, duration=30):
    """
    Calcule le beat histogramme à partir de l'autocorrélation améliorée d'un fichier audio.
    
    :param audio_path: Chemin du fichier audio
    :param bpm_min: BPM minimum considéré dans l'histogramme
    :param bpm_max: BPM maximum considéré dans l'histogramme
    :param duration: Durée maximale de l'audio à charger (en secondes)
    :return: Histogramme des battements (beat histogram)
    """
    # Charger une partie de l'audio pour réduire le temps de calcu
    y, sr = librosa.load(audio_path, sr=None, duration=duration)

    # Suppression de la moyenne pour éviter le biais DC
    y = y - np.mean(y)

    # Calcul de l'autocorrélation normalisée
    autocorr = np.correlate(y, y, mode='full')
    autocorr = autocorr[len(autocorr)//2:]  # On garde la moitié positive
    autocorr /= np.max(autocorr)  # Normalisation

    # Trouver les pics de l'autocorrélation
    peaks = librosa.util.peak_pick(autocorr, pre_max=5, post_max=5, pre_avg=5, post_avg=5, delta=0.05, wait=5)

    # Convertir les pics en BPM
    lag_times = peaks / sr  # Convertit les indices en temps (secondes)
    lag_times = lag_times[lag_times > 0]  # Éliminer les valeurs nulles pour éviter la division par zéro
    bpm_values = 60 / lag_times  # Convertit les temps en BPM

    # Filtrer les valeurs de BPM valides
    bpm_values = bpm_values[(bpm_values >= bpm_min) & (bpm_values <= bpm_max)]

    # Vérifier que bpm_values et autocorr[peaks] ont la même taille
    valid_peaks = peaks[:len(bpm_values)]  # Ajuster les indices des pics si nécessaire
    bpm_hist, bins = np.histogram(bpm_values, bins=np.arange(bpm_min, bpm_max, 1), weights=autocorr[valid_peaks])

    return bpm_hist, bins

# Spécifier le chemin du fichier audio
audio_file = "hiphop.00005.au"

# Calculer le beat histogramme
bpm_hist, bins = compute_beat_histogram(audio_file)

# Affichage du beat histogramme
plt.figure(figsize=(10, 5))
plt.bar(bins[:-1], bpm_hist, width=1.0, color='b', alpha=0.7)
plt.xlabel("BPM (Battements par minute)")
plt.ylabel("Amplitude normalisée")
plt.title("Beat Histogramme")
plt.grid(True)
plt.show()


