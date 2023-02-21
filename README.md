# SMCQGIS22

Ce plugin permet d'effectuer une sélection de toutes les entités contenues au sein de couches choisies par l'utilisateur, et ceux sur toutes les couches du projet QGIS.

## Installation

### 1. Repérer le répertoire de destination 

Depuis QGIS, ouvrir le **répertoire utilisateur courant** : `Préférences > Profils utilisateurs > Ouvrir le dossier du profil actif`

Se rendre ensuite dans `python > plugins`, c'est dans ce répertoire que nous installerons l'extension.

### 2. Télécharger l'extension

Cliquer sur [ce lien](https://github.com/infogeo54/SMC_QGIS22/archive/master.zip) pour lancer le téléchargement.

L'extension est téléchargée au **format ZIP**, il est donc nécessaire de la **décompresser** avant de continuer.

### 3. Déplacer l'extension

Placer l'extension décompressée dans le **répertoire de destination** (voir étape 1).

### 4. Redémarrer QGIS

Les extensions sont chargées au démarrage de QGIS, il est donc nécessaire de redémarrer l'application pour que les changements soient pris en compte

### 5. Activer l'extension (si nécessaire)

Il est possible que l'extension ne soit pas activée par défaut, dans ce cas il suffit de se rendre dans l'interface de gestion des extensions `Extensions > Installer/Gérer les extensions`.

Rendez-vous ensuite dans l'onglet `Installées`, cherchez **SMC** et cochez la case correspondante.

## Fonctionnement

### 1. Réglage de l'emprise

Avant de procéder à la sélection des entités, il est nécessaire de **régler l'emprise** de sorte à se concentrer uniquement sur les **communes intéressantes**.

Il n'est pas nécessaire de contenir la totalité de la ou des communes au sein de l'emprise : il suffit simplement qu'une **partie** ou seulement la **délimitation** d'une commune soit contenue dans **l'emprise courante** pour qu'elle soit prise en compte.

### 2. Utilisation de l'extension

Arpès avoir réglé l'emprise, il suffit de lancer l'extension.

Il est alors nécessaire d'indiquer à l'extension les **noms des communes** sur lesquelles vous souhaiter effectuer la sélection des entités.

Pour ajouter une commune à la liste depuis laquelle l'extension procèdera à la sélection, il suffit de **cocher** la case à côté du nom de la commune en question.

### 3. Sélection

En cliquant sur le bouton `valider`, l'extension se charge de passer en revue la totalité des couches du projet afin de repérer les entités contenues au sein des communes choisies. Ces dernières sont alors **ajoutées à la sélection globale**.

Notez que **le temps de traitement est proportionnel au nombre d'entités présentes dans le projet QGIS**. La sélection peut alors prendre quelques secondes dans le cas d'un projet de grande envergure.