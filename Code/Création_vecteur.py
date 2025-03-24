import librosa
import numpy as np
from code_MFCC import  MFCC
from spectral_centroid import compute_spectral_centroid
from Flux_spectral import compute_spectral_flux
from Rollof_spectral import compute_spectral_rollof

def charger_audio(chemin_fichier, sr=16000): #sr : fréq d'échantillonnage
    signal, Fs = librosa.load(chemin_fichier, sr=sr)
    return signal, Fs

# Test du MFCC et charger le fichier audio
extension=input("donner l'extension du fichier: ")
musique=input("donner le nom du fichier "+extension+":" )
chemin_fichier = "C:\\Users\\Administrateur\\Documents\\projet Artishow\\playlist-curation\\Frequency features\\" +musique+"."+extension

signal,Fs = charger_audio(chemin_fichier)
n_fft = 2048  # Taille de la FFT
hop_size = 512  # Décalage entre fenêtres
n_mels = 20  # Nombre de filtres MEL
n_mfcc = 5  # Nombre de coefficients MFCC conservés

def création_vecteur(signal,Fs, n_fft, hop_size, n_mels, n_mfcc):
    vecteur=[]
    a,b=0,0
    MFCC_var,MFCC_mean=MFCC(signal,Fs, n_fft, hop_size, n_mels, n_mfcc)
    vecteur=np.concatenate((MFCC_mean,MFCC_var),axis=0)
    a,b=compute_spectral_centroid(signal, Fs, n_fft, hop_size)
    vecteur=np.concatenate((vecteur,a),axis=0)
    vecteur=np.concatenate((vecteur,b),axis=0)
    a,b=compute_spectral_rollof(signal, Fs, n_fft, hop_length=hop_size)
    vecteur=np.concatenate((vecteur,a),axis=0)
    vecteur=np.concatenate((vecteur,b),axis=0)
    a,b=compute_spectral_flux(signal,n_fft, hop_length=hop_size)
    l=np.array([a,b])
    vecteur=np.concatenate((vecteur,l),axis=0)
    return vecteur

vecteur=création_vecteur(signal,Fs, n_fft, hop_size, n_mels, n_mfcc)
print(vecteur)