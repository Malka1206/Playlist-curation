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

def compute_spectral_centroid(signal, sr, n_fft, hop_length):
    spectral_centroid = librosa.feature.spectral_centroid(y=signal, sr=sr, n_fft=n_fft, hop_length=hop_length)
    return spectral_centroid

# Test du MFCC et charger le fichier audio
extension=input("donner l'extension du fichier: ")
musique=input("donner le nom du fichier "+extension+":" )
chemin_fichier = "C:/Users/Administrateur/Documents/projet Artishow/playlist-curation/Frequency features/" +musique+"."+extension

signal,Fs = charger_audio(chemin_fichier)

n_fft = 2048  # Taille de la FFT
hop_size = 512  # Décalage entre fenêtres
n_mels = 20  # Nombre de filtres MEL
n_mfcc = 13  # Nombre de coefficients MFCC conservés

#showing spectral centroid
spectral_centroid = compute_spectral_centroid(signal, Fs, n_fft, hop_size)
print(spectral_centroid)

# 🔹 Affichage du Spectral Centroid
plt.figure(figsize=(10, 4))
frames = range(spectral_centroid.shape[1])
times = librosa.frames_to_time(frames, sr=Fs, hop_length=512)

plt.plot(times, spectral_centroid[0], label="Spectral Centroid", color="red")
plt.xlabel("Temps (s)")
plt.ylabel("Fréquence (Hz)")
plt.title("Spectral Centroid")
plt.legend()
plt.show()