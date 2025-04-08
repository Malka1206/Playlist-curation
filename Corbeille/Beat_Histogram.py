import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import os

def compute_beat_histogram(audio_file):
    # Vérifier l'extension du fichier
    valid_extensions = ['.wav', '.au']
    if not os.path.splitext(audio_file)[1].lower() in valid_extensions:
        raise ValueError(f"Format de fichier non pris en charge. Veuillez utiliser un fichier avec l'une des extensions suivantes : {valid_extensions}")

    # Charger l'audio
    y, sr = librosa.load(audio_file, sr=None)

    # Extraire le tempo et les pulsations
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    
    # S'assurer que tempo est une valeur scalaire
    if isinstance(tempo, np.ndarray):
        tempo = tempo[0]  # Prendre la première valeur si c'est un tableau

    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    # Calculer les intervalles entre les battements
    beat_intervals = np.diff(beat_times)

    # plt.figure(figsize=(10, 5))
    plt.hist(beat_intervals, bins=30, alpha=0.7, color='b', edgecolor='black')
    plt.xlabel('Intervalle entre les battements (secondes)')
    plt.ylabel('Fréquence')
    plt.title(f'Beat Histogram - Tempo estimé: {tempo:.2f} BPM')
    plt.grid(True)
    plt.show()

compute_beat_histogram("C:\\Users\\MSI\\Desktop\\TELECOM\\Artishow\\playlist-curation\\Code\\musique.wav")
