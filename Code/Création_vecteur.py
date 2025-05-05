import librosa
import numpy as np
from code_MFCC import MFCC
from spectral_centroid import compute_spectral_centroid
from Flux_spectral import compute_spectral_flux
from Rollof_spectral import compute_spectral_rollof
from passage_par_0 import compute_passage_0
from Caractéristique_à_faible_énergie import compute_carac_faible_energie
from Carac_a_partir_du_BH import compute_beat_characterestics
from Carac_a_partir_du_PH import compute_tonal_character
from hist__classes_hauteur_deplie import hist_replie

#FenAnalyse = 0.023 s
#FenTexture = 1 s --> 43 fenêtres d'analyse

def charger_audio(chemin_fichier, sr=16000): #sr : fréq d'échantillonnage
    signal, Fs = librosa.load(chemin_fichier, sr=sr)
    return signal, Fs

chemin_fichier=input("chemin_fichier = ")

signal,Fs = charger_audio(chemin_fichier)
n_fft = 2048  # Taille de la FFT
hop_size = 512  # Décalage entre fenêtres
n_mels = 20  # Nombre de filtres MEL
n_mfcc = 5  # Nombre de coefficients MFCC conservés

def création_vecteur(signal,Fs, n_fft, hop_size, n_mels, n_mfcc):
    MFCC_var,MFCC_mean = MFCC(signal,Fs, n_fft, hop_size, n_mels, n_mfcc)
    SpectCentr_var,SpectCentr_mean = compute_spectral_centroid(signal, Fs, n_fft, hop_size)
    SpectRollof_var,SpectRollof_mean = compute_spectral_rollof(signal, Fs, n_fft, hop_length=hop_size)
    SpectFlux_var,SpectFlux_mean = compute_spectral_flux(signal,n_ftt,hop_size)
    Pass0_var,Pass0_mean = compute_passage_0(signa,FS)
    LowEnergy = compute_carac_faible_energie(signal,Fs)
    A0, A1, RA, P1, P2, SUM = compute_beat_caracterics(signal)

    vect = np.concatenate((MFCC_var,MFCC_mean),axis=0)



    """
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
    vecteur=np.concatenate()
    return vecteur"""

vecteur=création_vecteur(signal,Fs, n_fft, hop_size, n_mels, n_mfcc)
print(vecteur)