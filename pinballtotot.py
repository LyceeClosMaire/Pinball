# Créé par guyard, le 27/03/2017 en Python 3.2
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

son = pygame.mixer.Sound('issou.wav')
son.play(loops=-1, maxtime=0, fade_ms=0)


# on charge une image dans la variable "image"
imageflipl = pygame.image.load("flippersL.png").convert_alpha()
imageflipr = pygame.image.load("flippersR.png").convert_alpha()
rotatedflipl = imageflipl
rotatedflipr = imageflipr
rectl = rotatedflipl.get_rect(center = (162, 757) )
rectr = rotatedflipr.get_rect(center = (494, 757) )
imageball = pygame.image.load("voltball.png").convert_alpha()


degree = 0


continuer = True
while continuer:
    fenetre.fill( [0, 0 ,0] )

    # on l'affiche aux coordonnées (10,10)
    fenetre.blit(rotatedflipl, rectl)
    fenetre.blit(rotatedflipr, rectr)
    fenetre.blit(imageball, (740,840))

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
                rotatedflipr = pygame.transform.rotate(imageflipr, -70)
                rectr = rotatedflipr.get_rect(center = (494, 757) )


            if event.key == K_LEFT:
                rotatedflipl = pygame.transform.rotate(imageflipl, 70)
                rectl = rotatedflipl.get_rect(center = (162, 757) )


        if event.type == KEYUP:
            if event.key == K_RIGHT:
                rotatedflipr = imageflipr
                rectr = rotatedflipr.get_rect(center = (494, 757) )
            if event.key == K_LEFT:
                rotatedflipl = imageflipl
                rectl = rotatedflipl.get_rect(center = (162, 757) )








    clock.tick(60)



# On quitte proprement pygame
pygame.quit()