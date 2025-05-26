import librosa
import librosa.display
import matplotlib.pyplot as plt
audio_file = 'C:\\Users\\ASUS ZEN BOOK\\Documents\\artishow\\hiphop.00005.au'
y, sr = librosa.load(audio_file, sr=None)

# Calculer l'enveloppe d'énergie
onset_env = librosa.onset.onset_strength(y=y, sr=sr)

# Estimation multiple du tempo (pas juste un seul)
tempos = librosa.beat.tempo(onset_envelope=onset_env, sr=sr,
                            aggregate=None)

plt.figure(figsize=(10, 5))
plt.hist(tempos, bins=30, color='purple', edgecolor='black', alpha=0.7)
plt.xlabel("Tempo (BPM)")
plt.ylabel("Importance / Confiance")
plt.title("Beat Histogram (librosa)")
plt.grid(True)
plt.show()



