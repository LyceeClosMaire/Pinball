# Créé par guyard, le 27/03/2017 en Python 3.2

# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *


pygame.init()
# ***
# on crée une fenêtre de 800x600 pixels
fenetre = pygame.display.set_mode( (800,900) )
# ***
clock = pygame.time.Clock()


# on charge une image dans la variable "image"
imageflipl = pygame.image.load("flippersL.png").convert_alpha()
imageflipr = pygame.image.load("flippersR.png").convert_alpha()
rotatedflipl = imageflipl
rotatedflipr = imageflipr

rectl = rotatedflipl.get_rect(center = (162, 757) )
rectr = rotatedflipr.get_rect(center = (494, 757) )

degree = 0

continuer = True
while continuer:
    fenetre.fill( [0, 0 ,0] )

    # on l'affiche aux coordonnées (10,10)
    fenetre.blit(rotatedflipl, rectl)
    fenetre.blit(rotatedflipr, rectr)

    pygame.display.flip()

    # On récupère une liste des événements à traiter:
    for event in pygame.event.get():

        # On décide de quitter l'application si l'événements est du
        # type QUIT (lorsque l'utilisateur demande la fermeture de
        # l'application par la méthode normale de son OS), ou bien
        # lorsque l'événement correspond au relâchement d'une touche
        # du clavier est que celle-ci est la touche d'échappement.
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            continuer = False

        # Si une touche a été pressée
        if event.type == KEYDOWN:
            # et que cette touche est la flèche vers le haut
            if event.key == K_RIGHT:

                while pygame.key.get_pressed():
                    rotatedflipr = pygame.transform.rotate(imageflipr, -70)
                    rectr = rotatedflipr.get_rect(center = (494, 757) )
                rotatedflipr = pygame.transform.rotate(imageflipr, -70)
                rectr = rotatedflipr.get_rect(center = (494, 757) )




            elif event.key == K_LEFT:
                while pygame.key.get_pressed():
                    rotatedflipl = pygame.transform.rotate(imageflipl, 70)
                    rectl = rotatedflipl.get_rect(center = (162, 757) )
                rotatedflipl = pygame.transform.rotate(imageflipl, 70)
                rectl = rotatedflipl.get_rect(center = (162, 757) )








    clock.tick(60)



# On quitte proprement pygame
pygame.quit()