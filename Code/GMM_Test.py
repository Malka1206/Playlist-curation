import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.metrics import accuracy_score

class MultiGaussianClassifier:
    def __init__(self, num_classes, num_components=1):
        """
        Initialize the Multi Gaussian Classifier.

        :param num_classes: Number of classes in the dataset
        :param num_components: Number of Gaussian components per class
        """
        self.num_classes = num_classes
        self.num_components = num_components
        self.gmm_models = []

    def train(self, X_train, y_train):
        """
        Train the classifier using the training dataset.

        :param X_train: Training data (features)
        :param y_train: Training labels (class labels)
        """
        self.gmm_models = []
        for class_label in range(self.num_classes):
            # Extract data for the current class
            class_data = X_train[y_train == class_label]

            # Train a GMM for the current class
            gmm = GaussianMixture(n_components=self.num_components, covariance_type='full', random_state=42)
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
            log_likelihoods = [gmm.score_samples(x.reshape(1, -1)) for gmm in self.gmm_models]

            # Assign the class with the highest log-likelihood
            predicted_class = np.argmax(log_likelihoods)
            predictions.append(predicted_class)
        return np.array(predictions)


# Example usage
if __name__ == "__main__":
    # Generate synthetic data for demonstration (replace with your actual data)
    np.random.seed(42)
    num_classes = 10
    num_features = 19
    num_samples_per_class = 100

    # Create synthetic data for each class
    data = []
    labels = []
    for class_label in range(num_classes):
        class_data = np.random.multivariate_normal(
            mean=np.random.rand(num_features) * 10,  # Random mean for each class
            cov=np.eye(num_features),  # Identity covariance matrix
            size=num_samples_per_class
        )
        data.append(class_data)
        labels.extend([class_label] * num_samples_per_class)

    # Combine data and labels
    data = np.vstack(data)
    labels = np.array(labels)

    # Split the data into training and testing sets
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.3, random_state=42)

    # Initialize and train the classifier
    classifier = MultiGaussianClassifier(num_classes=num_classes)
    classifier.train(X_train, y_train)

    # Classify the test data
    y_pred = classifier.classify(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Classification Accuracy: {accuracy * 100:.2f}%")

    # Example of classifying new data
    new_data = np.random.multivariate_normal(mean=np.random.rand(num_features) * 10, cov=np.eye(num_features), size=5)
    new_predictions = classifier.classify(new_data)
    print("New Data Predictions:", new_predictions)