import librosa
import numpy as np
import os



def compute_carac_faible_energie(y,sr):
    # Définition des paramètres
    win_analysis = int(0.023 * sr)  # Fenêtre d'analyse = 23 ms
    hop_length = win_analysis // 2  # Overlap de 50% (typique)
    win_texture = int(1.0 * sr)  # Fenêtre de texture = 1s

    # Calcul de l'énergie RMS pour chaque fenêtre d'analyse
    rms = librosa.feature.rms(y=y, frame_length=win_analysis, hop_length=hop_length)[0]

    # Nombre de trames par seconde (dépend du hop_length)
    frames_per_sec = sr / hop_length

    # Découper en fenêtres de texture (1s)
    num_textures = len(rms) // int(frames_per_sec)

    low_energy_ratio = []

    for i in range(num_textures):
        start = int(i * frames_per_sec)
        end = int((i + 1) * frames_per_sec)
    
        rms_texture = rms[start:end]  # Sélectionner les valeurs RMS pour la fenêtre de texture
        mean_rms_texture = np.mean(rms_texture)  # Énergie RMS moyenne
        low_energy_count = np.sum(rms_texture < mean_rms_texture)  # Fenêtres avec RMS < moyenne
        low_energy_ratio.append(low_energy_count / len(rms_texture))  # Pourcentage

    # Moyenne globale de la caractéristique
    low_energy_feature = np.mean(low_energy_ratio)

    return low_energy_feature

# Charger un fichier audio
"""y, sr = librosa.load("C:\\Users\\user\\Desktop\\proj104\\metal00014.au")
def process_genre_folder(genre_path, num_songs):
    
    Traite un dossier de genre spécifique.
    
    Args:
        genre_path (str): Chemin vers le dossier du genre
        num_songs (int): Nombre de chansons à traiter
    Returns:
        list: Liste des caractéristiques LEF pour ce genre
    
    features = []
    audio_files = [f for f in os.listdir(genre_path) if f.endswith('.au')][:num_songs]
    
    for audio_file in audio_files:
        file_path = os.path.join(genre_path, audio_file)
        try:
            y, sr = librosa.load(file_path)
            lef = compute_carac_faible_energie(y, sr)
            features.append(float(lef))
        except Exception as e:
            print(f"Erreur avec {audio_file}: {str(e)}")
    
    return features

# Paramètres
genres_path = "C:\\Users\\user\\Desktop\\proj104\\genres"
num_songs_per_genre = 100  # Nombre de chansons à traiter par genre

# Initialisation du dictionnaire pour stocker les résultats
genre_features = {}

# Traitement de chaque genre
for genre in os.listdir(genres_path):
    genre_path = os.path.join(genres_path, genre)
    if os.path.isdir(genre_path):
        print(f"\nTraitement du genre : {genre}")
        genre_features[genre] = process_genre_folder(genre_path, num_songs_per_genre)

# Affichage des résultats
print("\nRésultats par genre :")
for genre, values in genre_features.items():
    if values:  # Vérifier que nous avons des valeurs
        mean_lef = np.mean(values)
        std_lef = np.std(values)
        print(f"\n{genre.upper()}:")
        print(f"Valeurs : {values}")

# Sauvegarde des résultats dans un fichier CSV
import csv

# Création du fichier CSV
with open('cfe.csv', 'w', newline='') as csvfile:
    # Création de l'écrivain CSV
    csvwriter = csv.writer(csvfile)
    
    # Écriture de l'en-tête
    csvwriter.writerow(['Genre', 'Valeurs'])
    
    # Écriture des données pour chaque genre
    for genre, values in genre_features.items():
        if values:  # Vérifier que nous avons des valeurs
            # Convertir la liste en chaîne de caractères
            values_str = ';'.join(map(str, values))
            csvwriter.writerow([genre, values_str])

"""
