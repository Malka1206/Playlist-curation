import numpy as np
import librosa
import scipy.signal
import matplotlib.pyplot as plt
from collections import Counter

# ---- PARAMÈTRES ----
FRAME_SIZE = 512
SR = 22050
FREQ_THRESHOLD = 1000  # Hz

def frequency_to_midi(f):
    return int(np.round(12 * np.log2(f / 440.0) + 69))

def autocorr_enhanced(x):
    corr = np.correlate(x, x, mode='full')[len(x)//2:]
    corr -= np.mean(corr)
    corr /= np.max(np.abs(corr)) + 1e-6
    return corr

def process_band(y, sr, band):
    sos = None
    if band == 'low':
        sos = scipy.signal.butter(4, FREQ_THRESHOLD, btype='lowpass', fs=sr, output='sos')
    elif band == 'high':
        sos = scipy.signal.butter(4, FREQ_THRESHOLD, btype='highpass', fs=sr, output='sos')
    filtered = scipy.signal.sosfilt(sos, y)
    rectified = np.abs(filtered)
    envelope = scipy.signal.sosfilt(scipy.signal.butter(2, 10, 'low', fs=sr, output='sos'), rectified)
    return envelope

def extract_pitch_from_frame(frame, sr):
    ac = autocorr_enhanced(frame)
    min_lag = int(sr / 1000)  # max 1000 Hz
    max_lag = int(sr / 80)    # min ~80 Hz
    peaks, _ = scipy.signal.find_peaks(ac[min_lag:max_lag])
    if len(peaks) == 0:
        return []
    peaks += min_lag
    peak_values = ac[peaks]
    top_indices = np.argsort(peak_values)[-3:]  # top 3 peaks
    freqs = sr / peaks[top_indices]
    return freqs

def audio_to_histograms(y, sr):
    uph = Counter()
    fph = Counter()
    num_frames = len(y) // FRAME_SIZE
    for i in range(num_frames):
        frame = y[i*FRAME_SIZE:(i+1)*FRAME_SIZE]
        env_low = process_band(frame, sr, 'low')
        env_high = process_band(frame, sr, 'high')
        summed = env_low + env_high
        pitches = extract_pitch_from_frame(summed, sr)
        for f in pitches:
            if f <= 0: continue
            midi = frequency_to_midi(f)
            uph[midi] += 1
            chroma = midi % 12
            fph[chroma] += 1
    return uph, fph

def compute_features(uph, fph):
    uph_array = np.array(sorted(uph.items()))
    fph_array = np.array(sorted(fph.items()))

    if len(fph) == 0 or len(uph) == 0:
        return None

    FA0 = int(np.max(fph_array[:, 1]))
    FP0 = int(fph_array[np.argmax(fph_array[:, 1]), 0])
    UP0 = int(uph_array[np.argmax(uph_array[:, 1]), 0])

    # Top 2 peaks in FPH
    if len(fph_array) > 1:
        top2 = fph_array[np.argsort(fph_array[:, 1])[-2:]]
        IPO1 = int(top2[1][0]) - int(top2[0][0])
    else:
        IPO1 = 0

    SUM = int(np.sum(fph_array[:, 1]))

    return {'FA0': FA0, 'UP0': UP0, 'FP0': FP0, 'IPO1': IPO1, 'SUM': SUM}

def plot_histogram(counter, title, xlabel='MIDI note', ylabel='Count'):
    items = sorted(counter.items())
    x, y = zip(*items)
    plt.figure(figsize=(10, 4))
    plt.bar(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ---- LECTURE ET TRAITEMENT ----
def analyse_audio(file_path):
    y, sr = librosa.load(file_path, sr=SR)
    uph, fph = audio_to_histograms(y, sr)
    features = compute_features(uph, fph)

    # Affichage
    plot_histogram(uph, 'UPH (Histogramme Déplié)')
    plot_histogram(fph, 'FPH (Histogramme Replié)', xlabel='Classe de hauteur (chroma)')

    print("Caractéristiques extraites :")
    for k, v in features.items():
        print(f"{k} : {v}")

# ---- Exemple d'utilisation ----
# Remplace par ton fichier .au
analyse_audio("C:\\Users\\MSI\\Desktop\\TELECOM\\Artishow\\playlist-curation\\Code\\hiphop.00005.au")