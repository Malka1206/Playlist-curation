import numpy as np
from sklearn.cluster import KMeans
from scipy.stats import multivariate_normal

class GMM:
    def __init__(self, n_components, n_init=10, max_iter=100, tol=1e-4): #tol=tolerance
        self.n_components = n_components
        self.n_init = n_init
        self.max_iter = max_iter
        self.tol = tol

    def _initialize_parameters(self, X):
        # Utiliser KMeans pour initialiser les moyennes
        best_kmeans = None
        best_inertia = np.inf

        for _ in range(self.n_init):
            kmeans = KMeans(n_clusters=self.n_components, n_init=1).fit(X)
            if kmeans.inertia_ < best_inertia:
                best_kmeans = kmeans
                best_inertia = kmeans.inertia_

        self.means_ = best_kmeans.cluster_centers_
        labels = best_kmeans.labels_

        # Initialiser les poids et covariances diagonales
        n_samples, n_features = X.shape
        self.weights_ = np.zeros(self.n_components)
        self.covariances_ = np.zeros((self.n_components, n_features))
        
        for k in range(self.n_components):
            Xk = X[labels == k]
            self.weights_[k] = len(Xk) / n_samples
            self.covariances_[k] = np.var(Xk, axis=0) + 1e-6  # diagonale uniquement

    def E_step(self, X):
        n_samples, _ = X.shape
        self.resp_ = np.zeros((n_samples, self.n_components))

        for k in range(self.n_components):
            cov_diag = np.diag(self.covariances_[k])
            self.resp_[:, k] = self.weights_[k] * multivariate_normal.pdf(
                X, mean=self.means_[k], cov=cov_diag
            )

        # Normalisation des responsabilités
        self.resp_ = self.resp_ / self.resp_.sum(axis=1, keepdims=True)

    def M_step(self, X):
        n_samples = X.shape [0]
        Vecteur_somme_par_composante = self.resp_.sum(axis=0)

        self.weights_ = Vecteur_somme_par_composante / n_samples
        self.means_ = (self.resp_.T @ X) / Vecteur_somme_par_composante[:, np.newaxis]

        for k in range(self.n_components):
            diff = X - self.means_[k]
            weighted_diff = self.resp_[:, k][:, np.newaxis] * (diff ** 2)
            self.covariances_[k] = weighted_diff.sum(axis=0) / Vecteur_somme_par_composante[k] + 1e-6

    def fit(self, X):
        self._initialize_parameters(X)

        log_likelihood_old = None
        for _ in range(self.max_iter):
            self.E_step(X)
            self.M_step(X)

            # Calcul du log-vraisemblance
            log_likelihood = np.sum(np.log(self.resp_.sum(axis=1)))

            if log_likelihood_old is not None and abs(log_likelihood - log_likelihood_old) < self.tol:
                break
            log_likelihood_old = log_likelihood

    def predict_proba(self, X):
        probs = np.zeros((X.shape[0], self.n_components))
        for k in range(self.n_components):
            cov_diag = np.diag(self.covariances_[k])
            probs[:, k] = self.weights_[k] * multivariate_normal.pdf(X, self.means_[k], cov_diag)
        return probs.sum(axis=1)

    def predict(self, X):
        return np.argmax(self.predict_proba(X), axis=1)
