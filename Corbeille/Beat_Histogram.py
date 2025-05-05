import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import os

def compute_beat_histogram(audio_file):
    # Charger l'audio (librosa supporte directement .au)
    y, sr = librosa.load(audio_file, sr=None)
    print(f"Fichier chargé : {audio_file} ({sr} Hz)")

    # Extraire le tempo et les battements
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    # S'assurer que tempo est bien un scalaire
    if isinstance(tempo, np.ndarray):
        tempo = tempo[0]  # Prendre la première valeur si c'est un tableau

    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    print(f"Tempo estimé : {tempo:.2f} BPM")
    print(f"Nombre de battements détectés : {len(beat_times)}")

    # Vérifier s'il y a assez de battements détectés
    if len(beat_times) > 1:
        beat_intervals = np.diff(beat_times)

        # Affichage de l'histogramme des intervalles de battement
        plt.figure(figsize=(10, 5))
        plt.hist(beat_intervals, bins=30, alpha=0.7, color='b', edgecolor='black')
        plt.xlabel('Intervalle entre les battements (secondes)')
        plt.ylabel('Fréquence')
        plt.title(f'Beat Histogram - Tempo estimé: {tempo:.2f} BPM')
        plt.grid(True)
        plt.show()
    else:
        print("⚠ Pas assez de battements détectés pour générer un histogramme.")

# Exemple d'utilisation avec un fichier .au
compute_beat_histogram("C:\\Users\\MSI\\Desktop\\TELECOM\\Artishow\\playlist-curation\\Code\\hiphop.00005.au")

