import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

# === Charger le fichier audio ===
"""audio_file = 'C:\\Users\\ASUS ZEN BOOK\\Documents\\artishow\\01-Come-Together-vinyl.au'
y, sr = librosa.load(audio_file, sr=None)"""
def compute_beat_characterestics (y,sr):
    # === Calculer l'enveloppe d'énergie ===
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)

    # === Estimation du tempo sous forme d'histogramme ===
    tempos = librosa.beat.tempo(onset_envelope=onset_env, sr=sr, aggregate=None)

    # === Créer l'histogramme ===
    hist, bin_edges = np.histogram(tempos, bins=30)

    # === Trouver les pics dans l'histogramme ===
    peaks, _ = find_peaks(hist)

    # Vérifier qu’on a au moins deux pics
    if len(peaks) >= 2:
        # Récupérer les indices des deux plus grands pics
        top_two_idx = np.argsort(hist[peaks])[-2:][::-1]
        peak_indices = peaks[top_two_idx]
    
        # P1 et P2 : positions des pics (en BPM)
        bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
        P1 = bin_centers[peak_indices[0]]
        P2 = bin_centers[peak_indices[1]]
    
        # A0 et A1 : amplitudes relatives
        raw_A0 = hist[peak_indices[0]]
        raw_A1 = hist[peak_indices[1]]
        total_amp = raw_A0 + raw_A1
        A0 = raw_A0 / total_amp
        A1 = raw_A1 / total_amp

        # RA : ratio d'amplitude
        RA = raw_A1 / raw_A0
    if len(peaks) == 1:
        peak_index = peaks[0]

        bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
        P1 = bin_centers[peak_index]
        P2 = 0.0  # Valeur neutre
        raw_A0 = hist[peak_index]
        raw_A1 = 0.0
        total_amp = raw_A0
        A0 = 1.0
        A1 = 0.0
        RA = 0.0
    else:
        A0 = A1 = RA = P1 = P2 = 0.0
    # SUM : somme totale de l’histogramme
    SUM = np.sum(hist)

    # Résultat final
    result_tuple = (A0, A1, RA, P1, P2, SUM)
    return result_tuple

""" print("Résultat (A0, A1, RA, P1, P2, SUM) :")
    print(result_tuple)
else:
    print("Pas assez de pics trouvés dans l'histogramme pour extraire les features.")
"""




