import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def compute_beat_characteristics(audio_path, bpm_min=40, bpm_max=200):
    """
    Calcule les caractéristiques principales du beat histogramme.
    
    :param audio_path: Chemin du fichier audio
    :param bpm_min: BPM minimum considéré dans l'histogramme
    :param bpm_max: BPM maximum considéré dans l'histogramme
    :return: Dictionnaire contenant A0, A1, RA, P1, P2, SUM
    """
    # Charger l'audio
    y, sr = librosa.load(audio_path, sr=None)

    # Suppression de la moyenne
    y = y - np.mean(y)

    # Calcul de l'autocorrélation normalisée
    autocorr = np.correlate(y, y, mode='full')
    autocorr = autocorr[len(autocorr)//2:]  # On garde la moitié positive
    autocorr /= np.max(autocorr)  # Normalisation

    # Détection des pics de l'autocorrélation
    peaks, _ = find_peaks(autocorr, height=0.1)  # Seulement les pics significatifs

    # Convertir les pics en BPM
    lag_times = peaks / sr  # Convertit les indices en temps (secondes)
    bpm_values = 60 / lag_times  # Convertit les temps en BPM

    # Filtrer les valeurs BPM valides
    valid_idx = (bpm_values >= bpm_min) & (bpm_values <= bpm_max)
    bpm_values = bpm_values[valid_idx]
    peak_amplitudes = autocorr[peaks][valid_idx]

    # Construction de l'histogramme pondéré
    bpm_hist, bins = np.histogram(bpm_values, bins=np.arange(bpm_min, bpm_max, 1), weights=peak_amplitudes)

    # Trouver les deux plus grands pics de l'histogramme
    sorted_indices = np.argsort(bpm_hist)[::-1]  # Indices triés en ordre décroissant
    if len(sorted_indices) < 2:
        return None  # Pas assez de pics détectés
    
    peak1_idx, peak2_idx = sorted_indices[:2]  # Indices des deux plus grands pics
    P1, P2 = bins[peak1_idx], bins[peak2_idx]  # Périodes (en BPM)

    A0 = bpm_hist[peak1_idx] / np.sum(bpm_hist)  # Amplitude relative du 1er pic
    A1 = bpm_hist[peak2_idx] / np.sum(bpm_hist)  # Amplitude relative du 2e pic
    RA = A1 / A0 if A0 != 0 else 0  # Rapport entre A1 et A0
    SUM = np.sum(bpm_hist)  # Somme totale des amplitudes de l'histogramme

    return {
        "A0": A0, "A1": A1, "RA": RA,
        "P1": P1, "P2": P2, "SUM": SUM
    }

# Spécifier le chemin du fichier audio
audio_file = "chemin/vers/fichier.wav"

# Calculer les caractéristiques
features = compute_beat_characteristics(audio_file)

# Afficher les résultats
if features:
    print("Caractéristiques du Beat Histogramme :")
    print(f"A0 (Amplitude relative 1er pic) : {features['A0']:.4f}")
    print(f"A1 (Amplitude relative 2e pic)  : {features['A1']:.4f}")
    print(f"RA (Rapport A1/A0)             : {features['RA']:.4f}")
    print(f"P1 (Période 1er pic en BPM)    : {features['P1']:.2f}")
    print(f"P2 (Période 2e pic en BPM)     : {features['P2']:.2f}")
    print(f"SUM (Force du rythme)          : {features['SUM']:.4f}")
else:
    print("Pas assez de pics détectés pour extraire les caractéristiques.")
