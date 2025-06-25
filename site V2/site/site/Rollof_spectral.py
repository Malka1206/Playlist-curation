import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth
import librosa.display
import librosa

def signal_sinusoidal(frequence=440, duree=1.0, echantillon=10000):
    t = np.linspace(0, duree, int(echantillon * duree), endpoint=False)
    signal = np.sin(2 * np.pi * frequence * t)
    return signal

def Somme_de_sinusoide(frequences=[440, 880], duree=1.0, echantillon=16000):
    t = np.linspace(0, duree, int(echantillon * duree), endpoint=False)
    signal = sum(np.sin(2 * np.pi * f * t) for f in frequences)
    return signal

def signal_triangulaire(frequence=440, duree=1.0, echantillon=16000):
    t = np.linspace(0, duree, int(echantillon * duree), endpoint=False)
    signal = sawtooth(2 * np.pi * frequence * t, width=0.5)  
    return signal

def bruit_blanc(duree=1.0, echantillon=16000):
    t = np.linspace(0, duree, int(echantillon * duree), endpoint=False)
    signal = np.random.normal(0, 1, len(t))
    return signal


def charger_audio(chemin_fichier, sr=16000):
    signal, Fs = librosa.load(chemin_fichier, sr=sr)
    return signal, Fs

def compute_spectral_rollof(signal, sr, n_fft, hop_length):
    spectral_rolloff = librosa.feature.spectral_rolloff(y=signal, sr=sr, n_fft=n_fft, hop_length=hop_length,roll_percent=0.85)
    spectral_rolloff_variances=np.var(spectral_rolloff)
    spectral_rolloff_means=np.mean(spectral_rolloff)
    return spectral_rolloff_variances,spectral_rolloff_means

"""# Test du MFCC et charger le fichier audio
extension=input("donner l'extension du fichier: ")
musique=input("donner le nom du fichier "+extension+":" )
chemin_fichier = "C:/Users/Administrateur/Documents/projet Artishow/playlist-curation/Frequency features/"+musique+"."+extension
signal,Fs = charger_audio(chemin_fichier)

n_fft = 2048  # Taille de la FFT
hop_size = 512  # Décalage entre fenêtres
n_mels = 20  # Nombre de filtres MEL
n_mfcc = 13  # Nombre de coefficients MFCC conservés

spectral_rolloff_variances,spectral_rolloff_means= compute_spectral_rollof(signal, Fs, n_fft, hop_size)
print(spectral_rolloff_variances)
print(spectral_rolloff_means)"""

"""# Affichage du rolloff spectral
plt.figure(figsize=(10, 4))
plt.semilogy(spectral_rolloff.T, label="Rolloff Spectral (Hz)", color="r")
plt.ylabel("Fréquence (Hz)")
plt.xlabel("Trame (Time Frame)")
plt.legend()
plt.title("Rolloff Spectral (85%)")
plt.show()"""