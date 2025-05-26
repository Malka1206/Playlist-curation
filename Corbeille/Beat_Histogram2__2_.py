import numpy as np
import librosa
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Fonction d'autocorrélation
def autocorrelation(signal):
    N = len(signal)
    signal = signal - np.mean(signal)  # Supprime la composante DC
    result = np.correlate(signal, signal, mode='full')
    result = result[result.size // 2:]  # On garde uniquement la moitié positive
    return result / np.max(result)  # Normalisation

# Fonction de filtrage passe-bas
def lowpass_filter(signal, alpha=0.99):
    """Applique un filtre passe-bas récursif sur un signal audio."""
    filtered_signal = np.zeros_like(signal)
    filtered_signal[0] = signal[0]  # Initialisation
    for n in range(1, len(signal)):
        filtered_signal[n] = alpha * filtered_signal[n - 1] + (1 - alpha) * signal[n]
    return filtered_signal

# Sous-échantillonnage
def downsample_audio(signal, factor):
    """Sous-échantillonne un signal audio en conservant un échantillon sur 'factor'."""
    return signal[::factor]

# Soustraction de la moyenne
def remove_mean(signal):
    """Soustrait la moyenne du signal pour le centrer à zéro."""
    return signal - np.mean(signal)

# Calcul du beat histogram
def compute_beat_histogram(audio_file, wavelet_levels=5, downsample_factor=16):
    # Charger l'audio
    y, sr = librosa.load(audio_file, sr=None)
    print(f"Fichier chargé : {audio_file} ({sr} Hz)")

    # Découper le signal en plusieurs bandes de fréquences octaviées (DWT)
    # Appliquer la Transformée en Ondelettes Discrètes pour extraire les différentes bandes de fréquences
    wavelet_bands = librosa.effects.hpss(y)[0]  # Utilisation de l'hpss (harmonique-percussif) de librosa

    # Pour chaque bande de fréquence :
    all_peaks = []
    for band in wavelet_bands:
        # Extraction de l'enveloppe d'amplitude de chaque bande
        band_envelope = np.abs(band)
        
        # Rectification en onde complète (valeurs positives)
        band_envelope = remove_mean(band_envelope)
        
        # Filtrage passe-bas de l'enveloppe pour lisser le signal
        filtered_envelope = lowpass_filter(band_envelope)
        
        # Sous-échantillonnage
        downsampled_envelope = downsample_audio(filtered_envelope, downsample_factor)
        
        # Calcul de l'autocorrélation de l'enveloppe
        autocorr = autocorrelation(downsampled_envelope)
        
        # Trouver les pics de la fonction d'autocorrélation
        peaks, _ = find_peaks(autocorr, height=0.2, distance=sr//10)
        all_peaks.extend(peaks)
    
    # Création de l'histogramme des battements
    beat_intervals = np.diff(np.array(all_peaks) / sr)
    
    plt.figure(figsize=(10, 5))
    plt.hist(beat_intervals, bins=30, alpha=0.7, color='b', edgecolor='black')
    plt.xlabel('Intervalle entre les battements (secondes)')
    plt.ylabel('Fréquence')
    plt.title('Histogramme des battements')
    plt.grid(True)
    plt.show()

# Exemple d'utilisation
compute_beat_histogram("C:\\Users\\MSI\\Desktop\\TELECOM\\Artishow\\playlist-curation\\Code\\hiphop.00005.au")