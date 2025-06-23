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

01-08 Avril, Aziz & Malek:  Documentation sur les algorithmes de classification selon un modèle multi gaussien (GMM). Nous comparons les complexités temporelles des algorithmes Random Forest et GMM.

08 Avril, Aziz & Malek: Ecriture d'un code de classification GMM, pour des vecteurs de 19 caractéristiques, connaissant déjà la classification des données utilisées (genres des chansons dans notre base de données)

15 Avril, Aziz : Adaptation du code de la caractéristique à faible énergie, son application sur la base de données de 10 genres et 100 chansons par genre.
On a désormais une autre caractéristique entièrement calculée. Objectifs : Créer un seul fichier python pour le calcul de toutes les caractéristiques à utiliser, faire une classification grossière pour tester les codes de classification.
Documentation : Classification GMM, initialisation kmean

15 Avril, Molka : amélioration du code beat_histogramme et l'essayer sur quelques chansons et intégrer le code d'extraction des caractéristiques à partir du beat histogramme. Coder la conversion d'un fichier audio à un histogramme des classes des hauteurs.
Documentation : initialisation kmean.

15 Avril Malek: Correction et compréhension totale du code du réseau neuronnal GMM. Le GMM est un réseau neuronnal qui travaille avec des lois des vecteurs de probabilité gaussiennes, il fait partie de l'apprentissage par probabilité. Il est initialement utilisé pour de l'apprentissage non supérvisé (car il est très proche de l'algo Kmean) mais dans notre cas et conformément à l'un des document on l'utilisera dans un cadre d'apprentissage supérvisé. 
                Documentation : Lien TypeScript-Python (utiliser des fonctions python pour le fichier qui a été drop sur le index.html)

16 Avril Malek: Réalisation d'un code de transformation d'étiquette de genre en une de probabilité et mise en accord avec le reste du groupe sur une première version d'entraînement: On va pour la 1ère version utilsé un seul GMM pour un genre musicale et l'entraîner. Puis on va voir la performance du modèle (vitesse, précision, erreur, etc...), ensuite une session de debuggage s'il le faut. A la fin décider si on fait de l'optimisation ou on crée notre réseau complet et on commence la phase finale. 

16 Avril Aziz : (début) Création d'un site Web qui sert à détecter le genre du fichier audio déposé, programmé avec TypeScript (Voir commit site/script.ts)

20 Avril - 30 Avril, Aziz : Documentation sur la programmation en JavaScript/TypeScript (et sur la bibliothèque python flask), concernant les DropZones et la mise en page. Finalisation du site qui permet de faire glisser un fichier audio (type .au) dans la Dropzone, ayant un boutton détecter le genre, et qui affiche le genre de la chanson traitée. 

05 Mai Aziz : Erreur d'éxécution et debugging (il faut que la promesse sur script.ts soit résolue, ce qui n'est pas le cas) Je fais des tests primaires sur une fonction qui renvoie "hi"

05 Mai Aziz : Finalement, j'ai abandonné l'idée d'utiliser la bibiothèque flask car elle ne me permet pas d'appliquer ce que je veux. J'ai utilisé un serveur Node de JavaScript qui accède à une fonction fx qui prends en argument un fichier .au et qui renvoie une chaîne de caractères. Le site affiche bien la chaîne renvoyée par fx.

05 Mai Molka : corriger le code d'extraction des caractéristiques (octave dominante + SUM) et l'intégrer dans le code de l'histogramme déplié + vérification en l'essayant sur un fichier audio.
05 Mai Naoures : écrire le code d'extraction des caractéristiques à partir de l'histogramme replié et l'intégrer dans le code de l'histogramme + vérification en l'essayant sur un fichier audio.

05 Mai Malek: Réalisation du code knn (le modèle le plus facile d'apprentissage) pour tester les vecteurs caractéristiques réalisés. Execution et essais d'entraînement qui n'ont pas pu aboutir: en effet il y avait des fautes dans des scrypts d'extraction de certains features donc session de debuggage pour tout les scrypts. On conttinue donc de travailler sur le knn, une fois cette session fini et qu'on a pu entrainer notre modèle sans problème avec le knn, on n'aura pas de mal à le changer puisque le GMM y est très proche.

08 Mai - 22 Mai Aziz : Utilisation d'une API de Deezer (Codé en TypeScript, avec un serveur Astro) dans le serveur du site créé pour permettre à l'utilisateur d'écouter des musiques. L'objectif est de demander des chansons selon des critères choisis. Ce critère est le genre, qui sera estimé par le modèle de classification de musique qui ne tardera pas d'être fini.

08 Mai - 22 Mai Naoures : Débuggage du code de création du vecteur et gestion des exceptions dans les fonctions élémentaires de calcul de caractéristiques

26 Mai (tous) : test du code KNN pour vérifier l'exploitabilité des vecteurs de caractéristiques tirés des chansons de la base + test du code GMM sur la même base en sortie on a eu une faible précision 30%

25 et 26 Mai Aziz : Documentation sur deux modèles de classification (GNN et Random forest) et sur l'utilisation d'API Deezer et Node de JavaScript (Le site marche correctement avec astro sinon). Débugging de la page web de traitement du fichier fourni par l'utilisateur. Le site arrive bien dès maintenant à traiter correctement des fichiers audio avec une fonction python choisie. en cours : Rajout de l'affichage des playlist

28 mai : réunion avec les encadrants, discussion de notre avancée sur le projet, les problèmes rencontrés (accuracy de 40% du GMM), les prochaines étapes

2 Juin Malek+Naoures:discussion des remarques des encadrants, lecture de la description des modèles proposés par une autre référence bibliograpgique  Création de scrypt pour 4 autres modèle de classification SVM , XGB , LogisticRegression en mode ovr et en mode multinomiale et RandomForest. Test sur la base de donnée complète et on obtinet partout de très bon résultat on fera le choix de l'algorithme avec lequel on va continuer la classification d'ici la prochine scéance. On a aussi calculer divers métrique comme le support, la précision, le recall et le Fscore pour le modèle et pour chaque classe ceci nous permettra de bien choisir le modèle (on a trouvé une meilleure précision --> voir fichier de comparaison dans apprentissage), défintion des principales tâches qui nous restent à faire : Ce qui nous reste à faire :
-	Finaliser le site
-	Chercher une meilleure base de musique actuelle
-	Préparer le poster à présenter le jour j, à envoyer au plus tard le18 juin (juste avant les partiels)

28 mai - 02 juin Aziz : Utilisation d'un serveur astro à la place de node de JavaScipt à cause de problèmes de compilation. Préparation des listes des chansons utilisées pour la génération de playlists.

06 juin - 11 juin Aziz : Essai d'API Youtube pour la préparation du site, qui pourrait permettre d'implémenter un seul serveur pour le traitement des fichiers (l'API Deezer nécessite un serveur Node de JavaScript)

14 juin Aziz : Test d'un classificateur XGB (accuracy 6.2) et decision tree (5.9), recherche d'autres bases de données (test et entraînement)

20 juin - 22 juin Aziz : Le problème python/typescipt est enfin résolu, après avoir essayé beaucoup de types de serveurs. La librairie python fastAPI permet de lancer un serveur qui s'occupe du traitement du fichier audio envoyé par l'utilisateur.

22 juin Aziz : création de la liste des liens de musiques qui va servir à la génération de playlists

23 juin Toute l'équipe : Liste des musiques de recommendations prête. Tests de fonctions python sur le site et codage d'un algorithme de choix de chansons en fonction du genre du fichier rentré.

23 juin Molka : Structuration du plan de la présentation + début de la réalisation de la présentation

23 juin Aziz : Le site permet la reccommendation de playlist grâce à un fichier déposé par l'utilisateur.