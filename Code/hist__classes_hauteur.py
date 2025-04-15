import librosa
import matplotlib.pyplot as plt
import numpy as np

# === 1. Charger le fichier audio (.au ou autre) ===
audio_path = 'C:\\Users\\ASUS ZEN BOOK\\Documents\\artishow\\01-Come-Together-vinyl.au'  # Remplace par le chemin de ton fichier .au
y, sr = librosa.load(audio_path)

# === 2. Extraire les pitches (hauteurs) ===
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

# === 3. Garder les hauteurs dominantes avec une magnitude significative ===
pitch_values = []

for i in range(pitches.shape[1]):
    index = magnitudes[:, i].argmax()
    pitch = pitches[index, i]
    if pitch > 0:  # ignorer les silences
        pitch_values.append(pitch)

# === 4. Convertir en notes MIDI et calculer les classes de hauteur (Do, Do#, Ré, etc.) ===
midi_notes = 69 + 12 * np.log2(np.array(pitch_values) / 440.0)
pitch_classes = np.round(midi_notes) % 12  # modulo 12 pour ramener à une octave

# === 5. Afficher l'histogramme des classes de hauteur ===
plt.figure(figsize=(8, 4))
plt.hist(pitch_classes, bins=np.arange(13)-0.5, rwidth=0.8,
         color='mediumpurple', edgecolor='black')
plt.xticks(np.arange(12), ['C', 'C#', 'D', 'D#', 'E', 'F',
                           'F#', 'G', 'G#', 'A', 'A#', 'B'])
plt.title("Histogramme des classes de hauteur")
plt.xlabel("Note")
plt.ylabel("Occurrence")
plt.grid(True)
plt.tight_layout()
plt.show()
