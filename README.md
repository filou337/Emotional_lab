# Emotional Lab

Projet personnel de **reconnaissance des émotions faciales** en Python.

L'objectif est de partir de la webcam, de détecter un visage, d'en extraire des caractéristiques puis de classifier l'expression faciale (joie, tristesse, surprise, ...).

Le projet est construit **pas à pas**, en apprenant chaque notion de Computer Vision et de Machine Learning avant de l'intégrer dans l'application.

---

## Sommaire

1. [Technologies](#technologies)
2. [Structure du projet](#structure-du-projet)
3. [Installation](#installation)
4. [Lancer le projet](#lancer-le-projet)
5. [Méthode de travail](#méthode-de-travail)
6. [Avancement](#avancement)
7. [Notions apprises](#notions-apprises)

---

## Technologies

| Librairie | Version | Rôle |
|---|---|---|
| Python | 3.x | Langage du projet |
| `opencv-python` (cv2) | 5.1.0.95 | Computer Vision : caméra, traitement d'images et de vidéos, détection |
| `numpy` | 2.5.5 | Calcul numérique : les images sont manipulées comme des tableaux (ndarray) |

> OpenCV et NumPy travaillent ensemble : OpenCV transforme les images et les vidéos en tableaux NumPy.

---

## Structure du projet

```text
Emotion_lab/
├── README.md                    # Présentation du projet (ce fichier)
├── requirements.txt             # Librairies à installer (reproductibilité)
├── .ignore                      # Fichiers et dossiers à ne pas versionner
├── Notes_globales_projet.txt    # Notes personnelles étape par étape
├── Inspirations.txt             # Idées et références
│
└── src/
    ├── main.py                  # Point d'entrée : orchestre les modules de l'application
    │
    ├── experiments/             # Scripts d'apprentissage, indépendants les uns des autres
    │   ├── 01_check_environment.py    # Vérifier l'installation d'OpenCV et NumPy
    │   ├── 02_camera_detection.py     # Ouvrir la caméra et vérifier son accès
    │   ├── 03_image_capture.py        # Capturer une image et explorer le ndarray
    │   ├── 04_pixel_manipulation.py   # Format BGR, slicing et affichage d'une image
    │   └── 05_live_video.py           # Flux vidéo en temps réel (en cours)
    │
    ├── computer_vision/         # (à venir) Caméra, détection de visage, Face Mesh
    │
    ├── machine_Learning/        # (à venir) Apprentissage automatique
    │   ├── __init__.py
    │   ├── feature_extraction.py      # Extraire les variables explicatives du visage
    │   └── emotion_classifier.py      # Classifier les expressions faciales
    │
    └── utils/                   # (à venir) Outils transverses
        ├── __init__.py
        └── metrics.py                 # Indicateurs de performance du modèle
```

### Rôle de chaque partie

| Dossier / Fichier | Responsabilité |
|---|---|
| `main.py` | Orchestrer l'application (chef d'orchestre) |
| `experiments/` | Tester et comprendre chaque notion séparément |
| `computer_vision/` | Gérer la webcam et l'analyse du visage |
| `machine_Learning/` | Extraire les caractéristiques et prédire l'émotion |
| `utils/` | Fonctions utilitaires réutilisables (métriques, ...) |

---

## Installation

```bash
# 1. Cloner le projet
git clone <url-du-repo>
cd Emotion_lab

# 2. Créer et activer l'environnement virtuel
python3 -m venv .venv
source .venv/bin/activate        # Linux / macOS
# .venv\Scripts\activate         # Windows

# 3. Mettre à jour pip et installer les dépendances
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

> Le dossier `.venv` n'est pas partagé sur Git : il est lourd, dépend de l'OS, de la version de Python et des chemins locaux. `requirements.txt` suffit pour recréer le même environnement.

---

## Lancer le projet

Application principale :

```bash
python src/main.py
```

Expérimentations (une par une) :

```bash
python src/experiments/01_check_environment.py
python src/experiments/02_camera_detection.py
python src/experiments/03_image_capture.py
python src/experiments/04_pixel_manipulation.py
python src/experiments/05_live_video.py
```

> Certaines lignes de test sont commentées (`"""..."""`) dans les fichiers : il suffit de les décommenter pour voir les résultats.

---

## Méthode de travail

Chaque fonctionnalité suit le même cycle avant d'arriver dans `main.py` :

```text
Expérimentation  →  Compréhension  →  Validation  →  Refactorisation  →  Module réutilisable  →  Intégration dans main.py
```

Les fichiers de `experiments/` ne sont pas importés directement dans `main.py` : on en extrait les fonctionnalités utiles, on les améliore, puis on les range dans le bon module.

---

## Avancement

| Étape | Statut |
|---|---|
| Setup (Python, venv, Git, requirements) | ✅ Fait |
| 01 - Vérification de l'environnement | ✅ Fait |
| 02 - Connexion à la caméra | ✅ Fait |
| 03 - Capture d'une image | ✅ Fait |
| 04 - Manipulation des pixels | ✅ Fait |
| 05 - Vidéo en direct | 🔄 En cours |
| Computer Vision (détection de visage, Face Mesh) | ⏳ À venir |
| Machine Learning (features, classification) | ⏳ À venir |
| Intégration dans `main.py` | ⏳ À venir |

---

## Notions apprises

**Computer Vision**
- `cv2.VideoCapture(0)` ouvre la caméra par défaut (`1` = 2e caméra, `"video.mp4"` = fichier local)
- `cam.isOpened()` vérifie que la caméra est accessible
- `cam.read()` renvoie `(ret, frame)` : un booléen de réussite et l'image
- Une image est un `numpy.ndarray` de forme `(hauteur, largeur, 3)` en `uint8` (valeurs de 0 à 255)
- OpenCV utilise le format **BGR** (bleu, vert, rouge) et non RGB
- Le slicing (`frame[0:100, 0:100]`) permet de modifier une zone de pixels sans boucle
- `cv2.imshow()` affiche une image, `cv2.waitKey()` garde la fenêtre ouverte

**Architecture logicielle**

| Principe | Définition |
|---|---|
| Modularité | Découper le programme en modules indépendants |
| Separation of Concerns | Séparer les différentes responsabilités |
| Single Responsibility | Une responsabilité principale par composant |
| Réutilisabilité | Réutiliser une fonctionnalité dans plusieurs programmes |
| Maintenabilité | Faciliter la correction et l'évolution du code |
| Entry Point | `main.py` est le point d'entrée du programme |

---

## Auteur

Philippe Roumbo, projet personnel d'apprentissage.
