"""
EMOTIONAL LAB - Expérimentation 03 : Capture d'une image

A quoi sert ce fichier :
    Capturer une image (frame) depuis la caméra et comprendre ce qu'OpenCV
    nous renvoie : un booléen de réussite et une image sous forme de tableau NumPy.

Parties :
    1. Importation des librairies
    2. Lancement de la caméra (repris de 02)
    3. Capture d'une image
    4. Exploration de l'image capturée (type, taille, dimensions, ...)
    5. Petit exo d'expérimentation

Lancement : python src/experiments/03_image_capture.py
"""

## Importation des librairies
import cv2
import numpy as np


## Lancement de la caméra (repris de 02_camera_detection.py)
cam = cv2.VideoCapture(0)
print(cam.isOpened())


## Capture d'une image
# Capturons une image de la caméra (elle retourne deux valeurs : un booléen et une image)
# ret pour le booléen et frame pour l'image capturée
ret, frame = cam.read()

# Affichons l'image capturée dans une fenêtre
"""print(ret)
print(frame)"""


## Exploration de l'image capturée
# Ok ca a marché , nous allons maintenant tester plusieurs choses sur l'image capturée
"""
print("le type de cette  image est ", type(frame)) # pour verifier le type de l'image capturée
print("Voici la taille : ",frame.shape) # pour verifier la taille de l'image capturée
print("Voici le type : ",frame.dtype) # pour verifier le type des données de l'image capturée
print("Voici le nombre de dimensions : " ,frame.ndim) # pour verifier le nombre de dimensions de l'image capturée
print("Voici la taille : " ,frame.size) # pour verifier la taille de l'image capturée"""


## Petit exo d'expérimentation
"""
print("Voici l :",type(cam))# booléan
print("Voici l :",type(ret))# booléan
print("Voici l :",type(frame))# ndarray"""

# La capture a réussi , du coup là nous allons identifier pour frame : 
"""
print("shape : ",frame.shape) # VOici la taille de l'image capturée :  (480, 640, 3)
print("dtype:",frame.dtype) # VOici le type de l'image capturée : uint8
print("DImension Number : ",frame.ndim) # Voici le nombre de dimensions de l'image capturée : 3
print("Size : ",frame.size) # VOici la taille de l'image capturée : 921600
print("Octets : ",frame.nbytes) # Voici le nombre d'octets de l'image capturée
print(frame.shape[0] * frame.shape[1])  # 307200 pixels"""


## Notes
# - cam.read() renvoie un tuple (ret, frame) : ret = True si la capture a réussi
# - frame est un numpy.ndarray : une image n'est donc qu'un tableau de nombres
# - shape (480, 640, 3) = (hauteur, largeur, canaux de couleur)
# - dtype uint8 = chaque valeur est un entier entre 0 et 255
# - size = 480 x 640 x 3 = 921600 valeurs , et 480 x 640 = 307200 pixels
