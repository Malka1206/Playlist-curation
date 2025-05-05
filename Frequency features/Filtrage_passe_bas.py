import numpy as np
import librosa
import matplotlib.pyplot as plt

def lowpass_filter(signal, alpha=0.99):
    """Applique un filtre passe-bas récursif sur un signal audio."""
    filtered_signal = np.zeros_like(signal)
    filtered_signal[0] = signal[0]  # Initialisation

    for n in range(1, len(signal)):
        filtered_signal[n] = (1 - alpha) * signal[n] + alpha * filtered_signal[n - 1]

    return filtered_signal

# Charger un fichier audio
file_path = "C:\\Users\\MSI\\Desktop\\TELECOM\\Artishow\\playlist-curation\\Frequency features\\hiphop.00005.au"
y, sr = librosa.load(file_path, sr=None)

# Appliquer la rectification en onde complète
rectified_signal = np.abs(y)

# Appliquer le filtrage passe-bas
smoothed_envelope = lowpass_filter(rectified_signal, alpha=0.99)

# Sélectionner une portion du signal pour affichage (par exemple, 1 seconde)
t = np.linspace(0, len(y) / sr, len(y))  # Axe temporel en secondes
t_display = t[:int(sr)]  # Garder 1 seconde d'affichage

# Affichage du signal original et de l'enveloppe lissée
plt.figure(figsize=(12, 6))
plt.plot(t_display, y[:int(sr)], label="Signal original", alpha=0.6)
plt.plot(t_display, rectified_signal[:int(sr)], label="Signal rectifié (enveloppe brute)", alpha=0.6)
plt.plot(t_display, smoothed_envelope[:int(sr)], label="Enveloppe lissée (filtrée)", linewidth=2, color="red")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.title("Effet du filtrage passe-bas sur l'enveloppe du signal")
plt.grid()
plt.show()

#Le signal brut est affiché en bleu (avec transparence).
#L’enveloppe brute (rectification) est affichée en orange.
#L’enveloppe lissée (après filtrage passe-bas) est affichée en rouge, plus lisse que l’enveloppe brute.
#On limite l'affichage à 1 seconde pour une meilleure lisibilité.
