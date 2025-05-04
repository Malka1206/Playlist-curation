from scipy.signal import find_peaks

# === 6.1. Calcul de FP0 ===
FP0 = int(np.argmax(hist))
print(f"FP0 (Classe de hauteur dominante) : {FP0}")

# === 6.2. Calcul de IPO1 ===
# Trouver les pics locaux
peaks, _ = find_peaks(hist)

if len(peaks) >= 2:
    # Prendre les deux pics les plus élevés
    top2_indices = peaks[np.argsort(hist[peaks])[-2:]]
    ipo1 = int(np.abs(top2_indices[1] - top2_indices[0]))  # distance entre les deux pics
    # S'assurer que l'intervalle est dans l'octave (0–6 max)
    ipo1 = min(ipo1, 12 - ipo1)
else:
    ipo1 = 0

print(f"IPO1 (Intervalle tonal dominant entre les deux classes de hauteur principales) : {ipo1}")
