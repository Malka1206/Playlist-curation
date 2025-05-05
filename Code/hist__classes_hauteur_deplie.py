import librosa
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

# === 1. Charger le fichier audio (.au ou autre) ===
"""audio_path = "C:\\Users\\ASUS ZEN BOOK\\Documents\\artishow\\test\\hiphop.00005 (1).au"""
def hist_deplie(y,sr):
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

    # === 6. Créer l'histogramme sous forme de tableau numérique ===
    hist_values, hist_bins = np.histogram(midi_notes, bins=bins)

    # === 7. Calculer SUM ===
    sum_hist = np.sum(hist_values)
    

    # === 8. Extraire l'octave dominante ===
    octaves = (midi_notes // 12).astype(int)  # Calculer l'octave pour chaque note MIDI
    unique_octaves, counts = np.unique(octaves, return_counts=True)  # Compter les occurrences par octave
    dominant_octave = unique_octaves[np.argmax(counts)]  # Identifier l'octave dominante

    return int(dominant_octave-1) , int(sum_hist)


"""xticks = np.arange(midi_notes.min(), midi_notes.max() + 1)
xtick_labels = [librosa.midi_to_note(m) for m in xticks]
plt.xticks(xticks, xtick_labels, rotation=45)

plt.title("Histogramme des hauteurs musicales (notes MIDI)")
plt.xlabel("Note (MIDI)")
plt.ylabel("Occurrence")
plt.grid(True)
plt.tight_layout()
plt.show()"""
