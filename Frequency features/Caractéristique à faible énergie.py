import librosa
import numpy as np

# Charger un fichier audio
y, sr = librosa.load("chemin/vers/fichier_audio.wav")

# Définition des paramètres
win_analysis = int(0.023 * sr)  # Fenêtre d'analyse = 23 ms
hop_length = win_analysis // 2  # Overlap de 50% (typique)
win_texture = int(1.0 * sr)  # Fenêtre de texture = 1s

# Calcul de l'énergie RMS pour chaque fenêtre d'analyse
rms = librosa.feature.rms(y=y, frame_length=win_analysis, hop_length=hop_length)[0]

# Nombre de trames par seconde (dépend du hop_length)
frames_per_sec = sr / hop_length

# Découper en fenêtres de texture (1s)
num_textures = len(rms) // int(frames_per_sec)

low_energy_ratio = []

for i in range(num_textures):
    start = int(i * frames_per_sec)
    end = int((i + 1) * frames_per_sec)
    
    rms_texture = rms[start:end]  # Sélectionner les valeurs RMS pour la fenêtre de texture
    mean_rms_texture = np.mean(rms_texture)  # Énergie RMS moyenne
    low_energy_count = np.sum(rms_texture < mean_rms_texture)  # Fenêtres avec RMS < moyenne
    low_energy_ratio.append(low_energy_count / len(rms_texture))  # Pourcentage

# Moyenne globale de la caractéristique
low_energy_feature = np.mean(low_energy_ratio)

# Affichage du résultat
print(f"Caractéristique à faible énergie : {low_energy_feature:.2%}")
