
# PROJET DE RECONNAISSANCE FACIALE  ( EMOTIONAL LAB)

## Importation des librairies
import cv2
import numpy as np


# Test de version des librairies
"""
print('Hello EMotional lab !')
print("Voici la version de opencv : ", cv2.__version__)
print("Voci la version de numpy  : ", np.__version__)"""


# Lancement de la caméra

cam = cv2.VideoCapture(0)
# Vérifions ue la caméra soit bien ouverte7

print(cam.isOpened())

# Découvrir les options de capture disponibles pour la caméra
"""print(dir(cam))"""

# Capturons une image de la caméra (elle retourne deux valeurs : un booléen et une image)
# ret pour le booléen et frame pour l'image capturée
ret, frame = cam.read()

# Affichons l'image capturée dans une fenêtre
"""print(ret)
print(frame)"""

# Ok ca a marché , nous allons maintenant tester plusieurs choses sur l'image capturée
"""
print("le type de cette  image est ", type(frame)) # pour verifier le type de l'image capturée
print("Voici la taille : ",frame.shape) # pour verifier la taille de l'image capturée
print("Voici le type : ",frame.dtype) # pour verifier le type des données de l'image capturée
print("Voici le nombre de dimensions : " ,frame.ndim) # pour verifier le nombre de dimensions de l'image capturée
print("Voici la taille : " ,frame.size) # pour verifier la taille de l'image capturée"""

# COmment OPenCV gère les couleurs ? 
# Au lieu d'utiliser le format RGB (rouge, vert, bleu) comme la plupart des librairies de traitement d'images, OpenCV utilise le format BGR (bleu, vert, rouge).
# BGR ( 41, 44, 41) = RGB ( 41, 44, 41) = Gris
# 

# Affichons le nombres de premieres images capturées par la caméra
frame[0:100 , 0:100]= [0, 0, 255] # on va colorer en rouge le carré de 100 pixels sur 100 en haut à gauche de l'image capturée ( c'est le principe du slicing en python)
cv2.imshow("main", frame ) # imshow attend deux arguments : le nom de la fenêtre et l'image à afficher sous forme de ndarray ( donc un tableau numpy) 
cv2.waitKey(7500) # waitKey attend un argument :  c'est le temps d'ouverture de l'image en millisecondes ( 0 = infini) et 7500 pour 7.5 secondes

# Petit exo d'expérimentation
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

# La frame [0,0] par exemple est le 1er pixel de l'image capturée ( donc le pixel en haut à gauche de l'image)
# Et donc pour voir par rapport a la couleur de ce pixel , on peut faire : frame [0,0, 1] = rouge , frame [0,0, 2] = vert , frame [0,0, 3] = bleu



