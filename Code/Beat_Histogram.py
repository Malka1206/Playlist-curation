import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

def compute_beat_histogram(audio_file):
    # Charger l'audio
    y, sr = librosa.load(audio_file, sr=None)
    
    # Extraire le tempo et les pulsations
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    
    # Calculer les intervalles entre les battements
    beat_intervals = np.diff(beat_times)
    
    # Afficher l'histogramme
    plt.figure(figsize=(10, 5))
    plt.hist(beat_intervals, bins=30, alpha=0.7, color='b', edgecolor='black')
    plt.xlabel('Intervalle entre les battements (secondes)')
    plt.ylabel('Fréquence')
    plt.title(f'Beat Histogram - Tempo estimé: {tempo:.2f} BPM')
    plt.grid(True)
    plt.show()

# Exemple d'utilisation
# Remplace 'audio_file.wav' par le chemin de ton fichier audio
#audio_path = "chemin/vers/audio.wav"
#compute_beat_histogram(audio_path)