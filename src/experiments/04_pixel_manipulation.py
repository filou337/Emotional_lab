"""
EMOTIONAL LAB - Expérimentation 04 : Manipulation des pixels

A quoi sert ce fichier :
    Comprendre comment OpenCV gère les couleurs (format BGR) et modifier
    directement les pixels d'une image capturée grâce au slicing NumPy,
    puis afficher le résultat dans une fenêtre.

Parties :
    1. Importation des librairies
    2. Lancement de la caméra et capture d'une image (repris de 02 et 03)
    3. Comment OpenCV gère les couleurs (BGR)
    4. Modification des pixels et affichage de l'image
    5. Accès à un pixel précis

Lancement : python src/experiments/04_pixel_manipulation.py
"""

## Importation des librairies
import cv2
import numpy as np


## Lancement de la caméra et capture d'une image (repris de 02 et 03)
cam = cv2.VideoCapture(0)
print(cam.isOpened())
ret, frame = cam.read()


## COmment OPenCV gère les couleurs ? 
# Au lieu d'utiliser le format RGB (rouge, vert, bleu) comme la plupart des librairies de traitement d'images, OpenCV utilise le format BGR (bleu, vert, rouge).
# BGR ( 41, 44, 41) = RGB ( 41, 44, 41) = Gris
# 


## Modification des pixels et affichage
# Affichons le nombres de premieres images capturées par la caméra
frame[0:100 , 0:100]= [0, 0, 255] # on va colorer en rouge le carré de 100 pixels sur 100 en haut à gauche de l'image capturée ( c'est le principe du slicing en python)
cv2.imshow("main", frame ) # imshow attend deux arguments : le nom de la fenêtre et l'image à afficher sous forme de ndarray ( donc un tableau numpy) 
cv2.waitKey(7500) # waitKey attend un argument :  c'est le temps d'ouverture de l'image en millisecondes ( 0 = infini) et 7500 pour 7.5 secondes


## Accès à un pixel précis
# La frame [0,0] par exemple est le 1er pixel de l'image capturée ( donc le pixel en haut à gauche de l'image)
# Et donc pour voir par rapport a la couleur de ce pixel , on peut faire : frame [0,0, 1] = rouge , frame [0,0, 2] = vert , frame [0,0, 3] = bleu


## Notes
# - frame[ligne, colonne] : on lit d'abord la hauteur (y) puis la largeur (x)
# - [0, 0, 255] en BGR = 0 bleu , 0 vert , 255 rouge => rouge pur
# - Le slicing frame[0:100, 0:100] modifie directement l'image : pas besoin de boucle sur chaque pixel
# - NB : les canaux commencent à l'index 0 et sont dans l'ordre BGR :
#   frame[0,0,0] = bleu , frame[0,0,1] = vert , frame[0,0,2] = rouge (frame[0,0,3] n'existe pas)
