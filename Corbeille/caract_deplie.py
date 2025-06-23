from scipy.signal import find_peaks

# === 6. Créer l'histogramme sous forme de tableau numérique ===
hist_values, hist_bins = np.histogram(midi_notes, bins=bins)

# === 7. Calculer SUM ===
sum_hist = np.sum(hist_values)
print(f"SUM (total des hauteurs détectées) : {sum_hist}")

# === 6. Extraire l'octave dominante ===
octaves = (midi_notes // 12).astype(int)  # Calculer l'octave pour chaque note MIDI
unique_octaves, counts = np.unique(octaves, return_counts=True)  # Compter les occurrences par octave
dominant_octave = unique_octaves[np.argmax(counts)]  # Identifier l'octave dominante

print(f"L'octave dominante est : {dominant_octave-1}")
