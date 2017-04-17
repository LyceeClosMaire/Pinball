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
bumper = pygame.image.load("bumperrage.png").convert_alpha()

rect = pygame.rect.Rect( (650,0), (280,900)   )
rect1 = pygame.rect.Rect( (660,10), (130,880) )

rotatingR = False
angleR = 0
rotatingL = False
angleL = 0


continuer = True
while continuer:
    fenetre.fill( [0, 0, 0] )
    fenetre.fill( [175, 0, 0], rect )
    fenetre.fill( [0, 0, 0], rect1)

    # on l'affiche aux coordonnées (10,10)
    fenetre.blit(rotatedflipl, rectl)
    fenetre.blit(rotatedflipr, rectr)
    fenetre.blit(imageball, (740,840))
    fenetre.blit(bumper, (200, 100))
    fenetre.blit(bumper, (400, 300))
    fenetre.blit(bumper, (150, 450))


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
                rotatingR = True

            elif event.key == K_LEFT:
                rotatingL = True


        if event.type == KEYUP:
            if event.key == K_RIGHT:
                rotatingR = False
                angleR = 0
                rotatedflipr = imageflipr
                rectr = rotatedflipr.get_rect(center = (494, 757) )
            if event.key == K_LEFT:
                rotatingL = False
                angleL = 0
                rotatedflipl = imageflipl
                rectl = rotatedflipl.get_rect(center = (162, 757) )



    if rotatingR:
        angleR -= 15
        rotatedflipr = pygame.transform.rotate(imageflipr, angleR)
        rectr = rotatedflipr.get_rect(center = (494, 757) )
        if angleR <= -70:
            rotatingR = False

    if rotatingL:
        angleL += 15
        rotatedflipl = pygame.transform.rotate(imageflipl, angleL)
        rectl = rotatedflipl.get_rect(center = (162, 757) )
        if angleL >= 70:
            rotatingL = False

    clock.tick(60)



# On quitte proprement pygame
pygame.quit()