from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import GMM.py

# Données simulées (ex : une seule classe avec 3 composantes)
X, _ = make_blobs(n_samples=500, centers=3, cluster_std=1.0, random_state=42)

# Entraînement du GMM
gmm = GMM(n_components=3)
gmm.fit(X)

# Affichage des clusters estimés
plt.scatter(X[:, 0], X[:, 1], c=np.argmax(gmm.resp_, axis=1), cmap='viridis', s=15)
plt.scatter(gmm.means_[:, 0], gmm.means_[:, 1], c='red', marker='x', s=100, label='Centres')
plt.title("Responsabilités maximales par composante GMM")
plt.legend()
plt.show()
