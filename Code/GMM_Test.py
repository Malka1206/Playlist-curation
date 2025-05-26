import numpy as np
from sklearn.mixture import GaussianMixture
import os
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split   
from Création_vecteur import extraction_features

class MultiGaussianClassifier:
    def __init__(self, classes, num_components):
        """
        Initialize the Multi Gaussian Classifier.
        :param num_classes: Number of classes in the dataset
        :param num_components: Number of Gaussian components per class
        """
        self.classes = classes
        self.num_components = num_components
        self.gmm_models = []

    def train(self, X_train, y_train):
        """
        Train the classifier using the training dataset.
        :param X_train: Training data (features)
        :param y_train: Training labels (class labels)
        """
        self.gmm_models = []
        for class_label in self.classes:
            # Extract data for the current class
            class_data = X_train[y_train == class_label]

            # Train a GMM for the current class
            gmm = GaussianMixture(n_components=self.num_components,init_params="kmeans",n_init=10,
                                   covariance_type="diag", random_state=42)
            gmm.fit(class_data)
            self.gmm_models.append(gmm)

    def classify(self, X):
        """
        Classify new data points.

        :param X: Data points to classify
        :return: Predicted class labels
        """
        predictions = []
        for x in X:
            # Compute the log-likelihood for each class
            log_likelihoods = [gmm.score_samples(x.reshape(1, -1))[0] for gmm in self.gmm_models]

            # Assign the class with the highest log-likelihood
            predicted_class = np.argmax(log_likelihoods)
            predictions.append(self.classes[predicted_class])
        return np.array(predictions)
    
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

# Initialize and train the classifier
classifier = MultiGaussianClassifier(classes=genres, num_components=num_features)
classifier.train(X_train, y_train)

# Classify the test data
y_pred = classifier.classify(X_test)
print("this is prediction", y_pred[:10])
print("this is test", y_test[:10])


# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Classification Accuracy: {accuracy * 100:.2f}%")  