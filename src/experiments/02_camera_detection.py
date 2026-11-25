"""
EMOTIONAL LAB - Expérimentation 02 : Connexion à la caméra

A quoi sert ce fichier :
    Ouvrir la caméra de l'ordinateur avec OpenCV et vérifier qu'elle est bien
    accessible. On en profite pour découvrir les options disponibles sur l'objet caméra.

Parties :
    1. Importation des librairies
    2. Lancement de la caméra
    3. Vérification de l'ouverture de la caméra
    4. Découverte des options de capture

Lancement : python src/experiments/02_camera_detection.py
"""

## Importation des librairies
import cv2 # qui est openCV  et qui s'installe avec pip install opencv-python
import numpy as np


## Lancement de la caméra
# cv2.VideoCapture(0) = caméra par défaut , (1) = 2e caméra , "video.mp4" = fichier vidéo local
cam = cv2.VideoCapture(0)


## Vérifions ue la caméra soit bien ouverte7
print(cam.isOpened())   # True = caméra accessible , False = caméra introuvable ou déjà utilisée


## Découvrir les options de capture disponibles pour la caméra
"""print(dir(cam))"""


## Notes
# - cam est un objet de type cv2.VideoCapture : il représente le flux vidéo, pas encore une image
# - isOpened() renvoie un booléen : c'est le premier réflexe avant toute capture
# - dir(cam) liste toutes les méthodes disponibles (read, release, get, set, ...)
