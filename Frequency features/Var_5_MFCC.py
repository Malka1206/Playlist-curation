import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

audio_file = input("donner le fichier audi")
y, sr = librosa.load(audio_file, sr=None, mono=True)  # Conserve le taux d'échantillonnage original

# Extraire les MFCCs
n_mfcc = 5  # On garde les 5 premiers coefficients
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)

# Définir la taille de la fenêtre de texture en échantillons (1 seconde)
window_size = sr  # 1 seconde = sr échantillons
hop_length = 512  # Pas de déplacement des fenêtres (standard)

# Calculer le nombre de frames par seconde
frames_per_sec = sr // hop_length

# Nombre total de fenêtres de texture (1 seconde chacune)
num_windows = mfccs.shape[1] // frames_per_sec

# Stocker les variances des MFCCs par fenêtre de texture
mfcc_variances = np.zeros((n_mfcc, num_windows))

# Calcul des variances par fenêtre de texture
for i in range(num_windows):
    start_frame = i * frames_per_sec
    end_frame = start_frame + frames_per_sec
    if end_frame > mfccs.shape[1]:  # Vérifier la taille
        break
    mfcc_variances[:, i] = np.var(mfccs[:, start_frame:end_frame], axis=1)

# Affichage des MFCCs sous forme de spectrogramme
#plt.figure(figsize=(10, 4))
#librosa.display.specshow(mfccs, x_axis="time", cmap="coolwarm", sr=sr, hop_length=hop_length)
#plt.colorbar(label="Amplitude")
#plt.title("MFCCs (5 premiers coefficients)")
#plt.xlabel("Temps")
#plt.ylabel("Coefficient MFCC")
#plt.show()

# Affichage des variances des MFCCs
print(f"Variances des 5 premiers coefficients MFCC par fenêtre de 1s :")
print(mfcc_variances)