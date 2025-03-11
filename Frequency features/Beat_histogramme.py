import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

def compute_beat_histogram(audio_path, bpm_min=40, bpm_max=200):
    """
    Calcule le beat histogramme à partir de l'autocorrélation améliorée d'un fichier audio.
    
    :param audio_path: Chemin du fichier audio
    :param bpm_min: BPM minimum considéré dans l'histogramme
    :param bpm_max: BPM maximum considéré dans l'histogramme
    :return: Histogramme des battements (beat histogram)
    """
    # Charger l'audio
    y, sr = librosa.load(audio_path, sr=None)

    # Suppression de la moyenne pour éviter le biais DC
    y = y - np.mean(y)

    # Calcul de l'autocorrélation normalisée
    autocorr = np.correlate(y, y, mode='full')
    autocorr = autocorr[len(autocorr)//2:]  # On garde la moitié positive
    autocorr /= np.max(autocorr)  # Normalisation

    # Trouver les pics de l'autocorrélation
    peaks = librosa.util.peak_pick(autocorr, pre_max=10, post_max=10, pre_avg=10, post_avg=10, delta=0.01, wait=10)

    # Convertir les pics en BPM
    lag_times = peaks / sr  # Convertit les indices en temps (secondes)
    bpm_values = 60 / lag_times  # Convertit les temps en BPM

    # Filtrer les valeurs de BPM valides
    bpm_values = bpm_values[(bpm_values >= bpm_min) & (bpm_values <= bpm_max)]

    # Construction de l'histogramme des BPM
    bpm_hist, bins = np.histogram(bpm_values, bins=np.arange(bpm_min, bpm_max, 1), weights=autocorr[peaks])

    return bpm_hist, bins

# Spécifier le chemin du fichier audio
audio_file = "chemin/vers/fichier.wav"

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
