"""
EMOTIONAL LAB - Expérimentation 05 : Vidéo en direct

A quoi sert ce fichier :
    Passer d'une image fixe (03 et 04) à un flux vidéo en temps réel :
    capturer les images de la caméra en continu et les afficher dans une fenêtre,
    jusqu'à ce que l'utilisateur décide d'arrêter.

Parties :
    1. Importation des librairies
    2. Lancement de la caméra
    3. Boucle de lecture du flux vidéo
    4. Affichage en direct
    5. Arrêt de la vidéo et libération de la caméra

Lancement : python src/experiments/05_live_video.py
"""

## Importation des librairies

import cv2 # qui est openCV  et qui s'installe avec pip install opencv-python

## Lancement de la caméra

# Re-creation de l'objet caméra (cv2.VideoCapture) pour s'assurer qu'il est bien ouvert et prêt à capturer des images.
cam = cv2.VideoCapture(0)  # 0 = caméra par défaut , 1 = 2e caméra , "video.mp4" = fichier vidéo local

# Sachant qu'une vidéeo n'est qu'une succession d'images (frames), on peut lire le flux vidéo en continu avec une boucle while
# car on veut que la caméra prenne plusieurs image par seconde tant que nous le voulons.
# On va donc créer une boucle infinie qui va lire les images de la caméra et les afficher dans une fenêtre, jusqu'à ce que l'utilisateur décide d'arrêter.
# Par contre por sortir de la boucle nous allons utiliser break pour sortir de la boucle while et libérer la caméra et fermer la fenêtre d'affichage.
# Dans notre projet on utilisera break seulement si on veut sortir de la boucle pour éviter un crash de l'application.
while True : 
    # 1ere étape: lire une image de la caméra
    ret, frame  = cam.read()
    cv2.imshow("05_live_video", frame)  # Afficher l'image dans une fenêtre nommée "Live Video"
# On avait utilisé cv2.waitKey(0) pour attendre une touche de l'utilisateur pour passer à l'image suivante, 
# mais ici on veut que la vidéo défile automatiquement, donc on va utiliser cv2.waitKey(1) qui attend 1 milliseconde avant de passer à l'image suivante.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break  
    if not cam.isOpened():
        raise RuntimeError("Erreur: , la caméra n'est pas accessible ou déjà utilisée.")
    if ret == False: 
        print("Erreur: Impossible de lire l'image de la caméra.")
        break # Si la lecture de l'image a échoué, on sort de la boucle


cam.release()  # Libérer la caméra
cv2.destroyAllWindows()  # Fermer toutes les fenêtres d'affichage


## Notes

# 0xFF représente le masque binaire 11111111, qui permet de ne garder que les 8 bits de poids faible du code ASCII de la touche pressée. 
# donc il permet aux utilisateur de pouvoir utiliser une touche de leur clavier pour arrêter la vidéo en direct. ( en l'occurrence la touche "q" pour quitter

# NOtion apprise : 
# - Une vidéo est une succession d'images (frames) capturées par la caméra à une certaine fréquence (fps)
# - Pour lire un flux vidéo en continu, on utilise une boucle while qui lit les images
# - Pour afficher les images, on utilise cv2.imshow() dans la boucle while
# - Pour sortir de la boucle while, on peut utiliser cv2.waitKey() pour attendre une touche de l'utilisateur et break pour sortir de la boucle
#- Pour libérer la caméra et fermer la fenêtre d'affichage, on utilise cam.release(),  cv2.destroyAllWindows() ou 0xFF dans une boucle while pour ne garder que les 8 bits de poids faible du code ASCII de la touche pressée. 
#- On a utilisé "& 0xFF" pour faire du bitmasking soit le fait qu'on ne conserve que les 8 derniers bits pour comparer avec le code ASCII de la touche "q" pour quitter la vidéo en direct.
# - Raise sert a lever une exception si la caméra n'est pas accessible ou déjà utilisée, ce qui permet de gérer les erreurs et d'éviter un crash de l'application.
# -RUntimeError est une exception qui est levée lorsqu'une erreur d'exécution se produit, par exemple si la caméra n'est pas accessible ou déjà utilisée.