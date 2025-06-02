import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import os
from Création_vecteur import extraction_features
 
def extraire_features(fichier_audio):
    return extraction_features(fichier_audio)

def charger_donnees(base_path):
    X = []  # vecteurs de caractéristiques
    y = []  # étiquettes de genre
    genres = os.listdir(base_path)

    for genre in genres:
        chemin_genre = os.path.join(base_path, genre)
        if not os.path.isdir(chemin_genre):
            continue
        for fichier in os.listdir(chemin_genre):
            if fichier.endswith(".au"):
                chemin_fichier = os.path.join(chemin_genre, fichier)
                features = extraire_features(chemin_fichier)
                X.append(features)
                y.append(genre)

    return np.array(X), np.array(y)

# Chemin vers ta base audio organisée par genre
chemin_base = "C:/Users/Administrateur/Documents/projet Artishow/playlist-curation/Dataset"  

num_features = 30    
data,labels=charger_donnees(chemin_base)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.3, random_state=42)
genres=np.unique(y_train)

num_classes = len(genres)

# 1. Créer et entraîner le modèle de régression logistique
model = LogisticRegression(
    multi_class='multinomial',  # Pour classification multi-classes
    solver='lbfgs',              # Optimiseur adapté aux petits jeux de données
    max_iter=1000,               # Augmenter si le modèle ne converge pas
    random_state=42
)

model.fit(X_train, y_train)

# 2. Prédire les classes pour X_test
y_pred = model.predict(X_test)

# 3. Évaluer les performances (optionnel)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")