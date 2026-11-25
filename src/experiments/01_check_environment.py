"""
EMOTIONAL LAB - Expérimentation 01 : Vérification de l'environnement

A quoi sert ce fichier :
    Vérifier que l'environnement Python (.venv) est bien en place et que les
    librairies principales du projet (OpenCV et NumPy) sont installées et importables.
    C'est la toute première étape avant de travailler avec la caméra.

Parties :
    1. Importation des librairies
    2. Test de version des librairies

Lancement : python src/experiments/01_check_environment.py
"""

## Importation des librairies
import cv2      # OpenCV : Computer Vision, traitement d'images et de vidéos
import numpy as np  # NumPy : manipulation de tableaux multidimensionnels (les images sont des tableaux)


## Test de version des librairies
"""
print('Hello EMotional lab !')
print("Voici la version de opencv : ", cv2.__version__)
print("Voci la version de numpy  : ", np.__version__)"""


## Notes
# - Si l'import échoue (ModuleNotFoundError), c'est que le .venv n'est pas activé
#   ou que les librairies ne sont pas installées : pip install -r requirements.txt
# - OpenCV et NumPy travaillent ensemble : OpenCV transforme les images / vidéos en tableaux NumPy (ndarray)
# - Connaître les versions permet de garantir la reproductibilité du projet (requirements.txt)
