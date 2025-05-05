import librosa
import matplotlib.pyplot as plt
import numpy as np

# === 1. Charger le fichier audio (.au ou autre) ===
audio_path = "C:\\Users\\MSI\\Desktop\\TELECOM\\Artishow\\playlist-curation\\Code\\hiphop.00005.au"

def get_first_frequency_for_pitch_class(pitch_class):
    """
    Renvoie la première fréquence (en Hz) correspondant à une classe de hauteur donnée (0–11).
    """
    for midi_note in range(0, 128):  # Plage MIDI typique
        if midi_note % 12 == pitch_class:
            freq = 440 * 2 ** ((midi_note - 69) / 12)
            return freq
    return None

def hist_deplie(audio_path):
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

    # === 4. Convertir en notes MIDI et calculer les classes de hauteur (0 à 11) ===
    midi_notes = 69 + 12 * np.log2(np.array(pitch_values) / 440.0)
    pitch_classes = np.round(midi_notes) % 12  # modulo 12 pour ramener à une octave (chroma)

    # === 5. Calcul de l'histogramme replié (FPH) ===
    hist, bins = np.histogram(pitch_classes, bins=np.arange(13)-0.5)

    # === 6. Calcul des carac ===
    FA0 = np.max(hist)
    FP0 = get_first_frequency_for_pitch_class(np.argmax(hist))
    # Trouver les deux pics les plus élevés
    top_two_indices = np.argsort(hist)[-2:][::-1]  # Deux plus grandes amplitudes
    peak1, peak2 = top_two_indices
    IPO1 = int(np.abs(hist[peak1] - hist[peak2]))

    return FA0, FP0, IPO1



# === 7. Afficher l'histogramme des pitch classes numériques ===
plt.figure(figsize=(8, 4))
plt.bar(np.arange(12), hist, width=0.8, color='mediumpurple', edgecolor='black')
plt.xticks(np.arange(12))  # Pas de noms de notes, juste 0 à 11
plt.title("Histogramme des classes de hauteur (FPH)")
plt.xlabel("Classe de hauteur (0–11)")
plt.ylabel("Occurrence")
plt.grid(True)
plt.tight_layout()
plt.show()


