import librosa
import matplotlib.pyplot as plt
import numpy as np

# === 1. Charger le fichier audio (.au ou autre) ===
audio_path = "C:\\Users\\MSI\\Desktop\\TELECOM\\Artishow\\playlist-curation\\Code\\hiphop.00005.au"
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

# === 4. Convertir en notes MIDI (arrondies à l'entier le plus proche) ===
midi_notes = np.round(69 + 12 * np.log2(np.array(pitch_values) / 440.0))

# === 5. Afficher l'histogramme des hauteurs (notes MIDI) ===
plt.figure(figsize=(10, 5))
bins = np.arange(midi_notes.min(), midi_notes.max() + 2) - 0.5
plt.hist(midi_notes, bins=bins, rwidth=0.8, color='skyblue', edgecolor='black')

# Étiquettes des notes (optionnel)
xticks = np.arange(midi_notes.min(), midi_notes.max() + 1)
xtick_labels = [librosa.midi_to_note(m) for m in xticks]
plt.xticks(xticks, xtick_labels, rotation=45)

plt.title("Histogramme des hauteurs musicales (notes MIDI)")
plt.xlabel("Note (MIDI)")
plt.ylabel("Occurrence")
plt.grid(True)
plt.tight_layout()
plt.show()
