import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from scipy.signal import find_peaks

def load_audio(filepath):
    sample_rate, signal = wav.read(filepath)
    # Si stéréo, on garde une seule voie
    if signal.ndim > 1:
        signal = signal[:, 0]
    return sample_rate, signal

def autocorrelation(signal):
    N = len(signal)
    signal = signal - np.mean(signal)  # Supprime la composante DC
    result = np.correlate(signal, signal, mode='full')
    result = result[result.size // 2:]  # On garde uniquement la moitié positive
    return result / np.max(result)  # Normalisation

def find_autocorr_peaks(ac, sample_rate):
    # Détection des pics (ignore le pic à 0 décalage)
    peaks, _ = find_peaks(ac, height=0.1, distance=sample_rate//100)  # filtrage simple
    peak_times = peaks / sample_rate  # convertit en secondes
    return peaks, peak_times

def plot_autocorrelation(ac, sample_rate, peaks):
    lags = np.arange(len(ac)) / sample_rate
    plt.figure(figsize=(10, 4))
    plt.plot(lags, ac)
    plt.plot(lags[peaks], ac[peaks], "ro")
    plt.title("Autocorrélation du signal audio")
    plt.xlabel("Temps de décalage (s)")
    plt.ylabel("Amplitude normalisée")
    plt.grid()
    plt.show()

# Exemple d'utilisation
audio_path = "votre_fichier.wav"  # ← Remplace ce chemin par ton fichier audio
sr, signal = load_audio(audio_path)
ac = autocorrelation(signal)
peaks, peak_times = find_autocorr_peaks(ac, sr)

print("Pics détectés aux temps (s):", peak_times)
plot_autocorrelation(ac, sr, peaks)
