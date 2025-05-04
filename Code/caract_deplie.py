from scipy.signal import find_peaks

# === 6. Créer l'histogramme sous forme de tableau numérique ===
hist_values, hist_bins = np.histogram(midi_notes, bins=bins)

# === 7. Calculer SUM ===
sum_hist = np.sum(hist_values)
print(f"SUM (total des hauteurs détectées) : {sum_hist}")

# === 8. Calculer UP0 ===
# Trouver les pics de l'histogramme (positions des hauteurs dominantes)
peaks, _ = find_peaks(hist_values)

if len(peaks) > 1:
    dominant_peak = peaks[np.argmax(hist_values[peaks])]
    distances = np.abs(peaks - dominant_peak)
    distances = distances[distances != 0]  # retirer 0 pour ne pas compter le même pic
    if len(distances) > 0:
        up0 = int(np.round(np.mean(distances)))
    else:
        up0 = 0
else:
    up0 = 0

print(f"UP0 (période dominante entre les pics) : {up0}")
