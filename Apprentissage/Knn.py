import os
import random
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import numpy as np


def extraire_features(fichier_audio):
    
    return [random.random() for _ in range(25)]  # FAUX : à remplacer par la vraie fonction

# Chargement des données
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
chemin_base = "dataset"  # à adapter si besoin

# 1. Chargement
X, y = charger_donnees(chemin_base)

# 2. Séparation en apprentissage/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

# 3. Création et entraînement du modèle KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# 4. Prédictions
y_pred = knn.predict(X_test)

# 5. Évaluation
print("Accuracy :", accuracy_score(y_test, y_pred))
print("Rapport de classification :")
print(classification_report(y_test, y_pred))
