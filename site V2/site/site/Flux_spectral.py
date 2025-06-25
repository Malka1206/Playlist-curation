import librosa
import numpy as np
import matplotlib.pyplot as plt

def charger_audio(chemin_fichier, sr=16000):
    signal, Fs = librosa.load(chemin_fichier, sr=sr)
    return signal, Fs

def compute_spectral_flux(signal, n_fft, hop_length): 
    stft = np.abs(librosa.stft(signal, n_fft=n_fft, hop_length=hop_length))
    
    epsilon = 1e-16  # Pour éviter la division par zéro
    stft_norm = stft / (np.sum(stft, axis=0, keepdims=True) + epsilon)
    
    spectral_flux = np.sum((np.diff(stft_norm, axis=1))**2, axis=0)
    spectral_flux_variances = np.var(spectral_flux)
    spectral_flux_means = np.mean(spectral_flux)
    
    return spectral_flux_variances, spectral_flux_means
    

"""# Test du MFCC et charger le fichier audio
extension=input("donner l'extension du fichier: ")
musique=input("donner le nom du fichier "+extension+":" )
chemin_fichier = "C:/Users/Administrateur/Documents/projet Artishow/playlist-curation/Frequency features/"+musique+"."+extension
signal,Fs = charger_audio(chemin_fichier)

n_fft = 2048  # Taille de la FFT
hop_size = 512  # Décalage entre fenêtres

spectral_flux_variances,spectral_flux_means= compute_spectral_flux(signal,n_fft, hop_size)
print(spectral_flux_variances)
print(spectral_flux_means)"""

"""# Affichage du flux spectral
plt.figure(figsize=(10, 4))
plt.plot(spectral_flux, label="Flux Spectral", color="b")
plt.xlabel("Trame (Time Frame)")
plt.ylabel("Amplitude")
plt.title("Flux Spectral du signal audio")
plt.legend()
plt.show()"""
