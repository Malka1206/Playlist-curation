14 Février Malek+Nawres+Molka+Aziz: Début du travai sur le projet, lecture des documents et compréhension de la problématique
18 Février Malek: Lecture de certains documents dans le dossier référence, choix provisoire d'une certaine caractéristique permattant de détecter les genres musicaux et exploration de cette piste 
18 Février Molka : mettre en forme un planning + lecture de certains documents
23 Février Malek : Lire documentation + Réalisation du code pour extraire une carectéritique audio "mfcc" manuellement
25 Février - 02 Mars : Molka, Naoures : lecture de deux références bibliographiques et identification des caractéristiques à extraire des fichiers audio

25 Février - 02 Mars, Aziz: Utilisation de la librairie Kaggle sur python pour exploiter une base de données. Celle ci contient 100 chansons par genre, pour 10 genres.
lien: https://www.kaggle.com/datasets/carlthome/gtzan-genre-collection/data

04 Mars (tous) : Présentation des recherches de chacun et discussion des caractéristiques et des classificateurs à utiliser
11 Mars Malek: Ajout d'une autre caractéristique spectrale (spectral centroid) dans le code, la sortie va être un vecteur
25 Mars Malek: Ajout des scripts spectral flux et rollof spectrale ainsi qu'un script qui regroupe tous les caractéristiques en un vecteur via importation par module

A faire pour 01 Avril - 08 Avril : distrubution entre Molka et Nawres des scripts des caractéristiques rythmiques et les regrouper en un vecteur/ Aziz: écriture de code de knn, kmean et exploration d'autre script de classificateur/ Malek: Réalisation et compréhension du script d'un classificateur GMM (gaussian mixed model) ainsi que des recherches sur d'autres classificateurs

01-08 Avril, Aziz & Malek:  Documentation sur les algorithmes de classification selon un modèle multi gaussien (GMM). Nous comparons les complexités temporelles des algorithmes Random Forest et GMM.

08 Avril, Aziz & Malek: Ecriture d'un code de classification GMM, pour des vecteurs de 19 caractéristiques, connaissant déjà la classification des données utilisées (genres des chansons dans notre base de données)

15 Avril, Aziz : Adaptation du code de la caractéristique à faible énergie, son application sur la base de données de 10 genres et 100 chansons par genre.
On a désormais une autre caractéristique entièrement calculée. Objectifs : Créer un seul fichier python pour le calcul de toutes les caractéristiques à utiliser, faire une classification grossière pour tester les codes de classification.