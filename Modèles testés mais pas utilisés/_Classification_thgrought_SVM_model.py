#Classification thgrought SVM model

import numpy as np
import os
from sklearn.model_selection import train_test_split   
from Création_vecteur import extraction_features
from sklearn.preprocessing import StandardScaler, LabelEncoder, label_binarize
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, classification_report, roc_auc_score

def extraire_features(fichier_audio):
    return extraction_features(fichier_audio)

def charger_donnees(base_path):
    X = []      
    y = []  
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

chemin_base = "C:/Users/Administrateur/Documents/projet Artishow/playlist-curation/Dataset"  
data,labels=charger_donnees(chemin_base)

# Transformer les geres en numéros lisible par le SVM
label_encoder = LabelEncoder()
labels_num = label_encoder.fit_transform(labels)

# Split the data into training, testing and validation sets

# First split: train+val and test (80% / 20%)
X_temp, X_test, y_temp, y_test = train_test_split(data, labels_num, test_size=0.2, 
                                                  random_state=42, stratify=labels_num)

# Second split: train and val (from temp, 75% / 25% → 60% / 20% overall)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, 
                                                  random_state=42, stratify=y_temp)

# Normalisation pour que les features qui ont une range importante ne soient pas considérés comme 
# des features importants 
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

# Train SVM
svm = SVC(kernel='rbf', C=10, gamma='scale')
svm.fit(X_train, y_train)

# Validation performance
y_val_pred = svm.predict(X_val)
print("Validation Accuracy:", accuracy_score(y_val, y_val_pred))
print("\nValidation Report:\n", classification_report(y_val, y_val_pred, target_names=label_encoder.classes_))

# Prédictions sur les données de test
y_test_pred = svm.predict(X_test)

# précision
accuracy = accuracy_score(y_test, y_test_pred)
print("Test Accuracy:", accuracy)

# F1-score macro (moyenne sur les classes, utile pour classes déséquilibrées)
f1 = f1_score(y_test, y_test_pred, average='macro')
print("Test F1-score (macro):", f1)

# Rapport complet
print("\nTest Classification Report:\n", classification_report(y_test, y_test_pred, target_names=label_encoder.classes_))

"""# 🔵 AUC : nécessite une sortie en probabilité ET des labels binarisés
# Étape 1 : binariser les étiquettes
y_test_bin = label_binarize(y_test, classes=range(len(label_encoder.classes_)))

# Étape 2 : obtenir les probabilités de chaque classe
y_score = svm.decision_function(X_test)  

# Étape 3 : calcul de l’AUC macro
auc = roc_auc_score(y_test_bin, y_score, average='macro', multi_class='ovr')
print("Test AUC (macro, OvR):", auc)"""