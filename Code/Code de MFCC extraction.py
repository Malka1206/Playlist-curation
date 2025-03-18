import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth
import librosa.display
from scipy.fftpack import dct
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


def charger_audio(chemin_fichier, sr=16000): #sr : fréq d'échantillonnage
    signal, Fs = librosa.load(chemin_fichier, sr=sr)
    return signal, Fs

# Test et affichage
"""signaux = {
    "Sinusoïde simple": signal_sinusoidal(),
    "Somme de sinusoïdes": Somme_de_sinusoide(),
    "Signal triangulaire": signal_sinusoidal(),
    "Bruit blanc": bruit_blanc(),
}

plt.figure(figsize=(10, 6))
for i, (title, (t, signal)) in enumerate(signaux.items()):
    plt.subplot(2, 2, i + 1)
    plt.plot(t[:500], signal[:500])  # Affichage des 1000 premiers points
    plt.title(title)
    plt.xlabel("Temps (s)")
    plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()"""

def compute_stft(signal, hop_size, n_fft, hann_window=True):
    # Définition de la fenêtre d'analyse
    window = np.hanning(n_fft) if hann_window else np.ones(n_fft)
    
    # Nombre de fenêtres que l'on peut extraire du signal
    num_frames = (len(signal) - n_fft) // hop_size + 1
    
    
    # Matrice pour stocker la STFT
    stft_matrix = np.zeros((n_fft // 2 + 1, num_frames), dtype=np.complex64)

    for i in range(num_frames):
        start = i * hop_size
        end = start + n_fft
        frame = signal[start:end] * window 
        stft_matrix[:, i] = np.fft.rfft(frame)  
    
    return stft_matrix

# 🔹 Test du code avec un signal sinusoïdal
"""t, signal = bruit_blanc()
hop_size = 512
n_fft = 2048
hann_window = True

stft_result = compute_stft(t, signal, hop_size, n_fft, hann_window)

#  Affichage du spectrogramme
plt.figure(figsize=(10, 6))
librosa.display.specshow(20 * np.log10(np.abs(stft_result) + 1e-6), sr=16000, hop_length=hop_size, x_axis="time", y_axis="log")
plt.colorbar(label="Amplitude (dB)")
plt.title("Spectrogramme STFT")
plt.xlabel("Temps (s)")
plt.ylabel("Fréquence (Hz)")
plt.show()"""

# Paramètres
duration = 1.0  # secondes

def MFCC(signal,Fs, n_fft, hop_size, n_mels, n_mfcc):
    # Calcul de la STFT
    stft_matrix = np.abs(compute_stft(signal, hop_size, n_fft))**2  

    # Création des filtres MEL
    mel_filters = librosa.filters.mel(sr=Fs, n_fft=n_fft, n_mels=n_mels)

    # Application du filtre MEL
    mel_spectrum = np.dot(mel_filters, stft_matrix)
    log_mel_spectrum = np.log(mel_spectrum + 1e-6)  

    # Application de la DCT pour obtenir les MFCCs
    mfccs = dct(log_mel_spectrum, type=2, axis=0, norm='ortho')[:n_mfcc]

    mfccs_used=mfccs[:n_mfcc,:]
    return mfccs_used, mfccs_used.shape

# Test du MFCC et charger le fichier audio
extension=input("donner l'extension du fichier: ")
musique=input("donner le nom du fichier "+extension+":" )
chemin_fichier = "C:\\Users\\MSI\\Desktop\\TELECOM\\Artishow\\playlist-curation\\Frequency features\\" +musique+"."+extension

signal,Fs = charger_audio(chemin_fichier)

n_fft = 2048  # Taille de la FFT
hop_size = 512  # Décalage entre fenêtres
n_mels = 20  # Nombre de filtres MEL
n_mfcc = 5  # Nombre de coefficients MFCC conservés

mfccs,mfccs_shape= MFCC(signal,Fs,n_fft,hop_size,n_mels,n_mfcc)

mfcc_variances=np.var(mfccs,axis=1)
print(mfcc_variances)

mfcc_means=np.mean(mfccs,axis=1)
print(mfcc_means)


"""plt.figure(figsize=(10, 4))
librosa.display.specshow(mfccs, x_axis='time', sr=Fs, hop_length=hop_size, cmap='coolwarm')
plt.colorbar(label='Amplitude')
plt.title('MFCCs')
plt.xlabel('Temps (s)')
plt.ylabel('Coefficients MFCC')
plt.show()"""