import librosa
import numpy as np
from code_MFCC import MFCC
from spectral_centroid import compute_spectral_centroid
from Flux_spectral import compute_spectral_flux
from Rollof_spectral import compute_spectral_rollof
from passage_par_0 import compute_passage_0
from Caractéristique_à_faible_énergie import compute_carac_faible_energie
from carac_beathist import compute_beat_characterestics
from hist__classes_hauteur_replie import hist_replie
from hist__classes_hauteur_deplie import hist_deplie


#FenAnalyse = 0.023 s
#FenTexture = 1 s --> 43 fenêtres d'analyse

def charger_audio(chemin_fichier, sr=16000): #sr : fréq d'échantillonnage
    signal, Fs = librosa.load(chemin_fichier, sr=sr)
    return signal, Fs


n_fft = 2048  # Taille de la FFT
hop_size = 512  # Décalage entre fenêtres
n_mels = 20  # Nombre de filtres MEL
n_mfcc = 5  # Nombre de coefficients MFCC conservés

def création_vecteur(signal,Fs, n_fft, hop_size, n_mels, n_mfcc):
    MFCC_var,MFCC_mean = MFCC(signal,Fs, n_fft, hop_size, n_mels, n_mfcc)
    SpectCentr_var,SpectCentr_mean = compute_spectral_centroid(signal, Fs, n_fft, hop_size)
    SpectRollof_var,SpectRollof_mean = compute_spectral_rollof(signal, Fs, n_fft, hop_length=hop_size)
    SpectFlux_var,SpectFlux_mean = compute_spectral_flux(signal,n_fft,hop_size)
    Pass0_var,Pass0_mean = compute_passage_0(signal,Fs)
    LowEnergy = compute_carac_faible_energie(signal,Fs)
    A0, A1, RA, P1, P2, SUM = compute_beat_characterestics(signal,Fs)
    FA0, FP0, IPO1 = hist_replie(signal,Fs)
    octave, SUM1 = hist_deplie(signal,Fs)
    l=np.array([SpectCentr_var,SpectCentr_mean,SpectRollof_var,SpectRollof_mean,SpectFlux_var,SpectFlux_mean,Pass0_var,Pass0_mean,LowEnergy,
               A0, A1, RA, P1, P2, SUM, FA0, FP0, IPO1, octave, SUM1])
    vect = np.concatenate((MFCC_var,MFCC_mean,l),axis=0)
    return vect

def extraction_features(chemin_fichier):
    signal,Fs = charger_audio(chemin_fichier)
    return création_vecteur(signal,Fs, n_fft, hop_size, n_mels, n_mfcc)
    