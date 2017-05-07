# Créé par guyard, le 27/03/2017 en Python 3.2
# Créé par guyard, le 27/03/2017 en Python 3.2

# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import math

x=600
y=850

pygame.init()
# ***
# on crée une fenêtre de 800x600 pixels
fenetre = pygame.display.set_mode( (800,900) )
rectgame = pygame.rect.Rect( (0,0), (650,900))
wingame = rectgame
# ***
clock = pygame.time.Clock()

son = pygame.mixer.Sound('issou.wav')
son.play(loops=-1, maxtime=0, fade_ms=0)


# on charge une image dans la variable "image"

imageflipr = pygame.image.load("flippersR.png").convert_alpha()



#rectr = rotatedflipr.get_rect(center = (494, 757) )


imageball = pygame.image.load("voltball.png").convert_alpha()
bumper = pygame.image.load("bumperrage.png").convert_alpha()

rect = pygame.rect.Rect( (650,0), (280,900)   )
rect1 = pygame.rect.Rect( (660,10), (130,880) )

rotatingR = False
angleR = 0
rotatingL = False
angleL = 0






class Ball(pygame.sprite.Sprite):

    def __init__(self, position, speed):
        super().__init__()
        self.speed = (0,-5)
        self.image = pygame.image.load("voltball.png")
        self.rect = self.image.get_rect(center=position)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if not wingame.contains(self):
            rect = self.rect
            self.speed = rebound(self.speed, wingame.left > rect.left or wingame.right < rect.right, wingame.top > rect.top or wingame.bottom < rect.bottom )
        self.rect.move_ip(self.speed)

ballGroup = pygame.sprite.Group()
ballGroup.add( Ball ( (600,850), (0, -5)))

class FlipperL(pygame.sprite.Sprite):

    def __init__(self, position, angle):
        self.image = pygame.image.load("flippersL.png")
        self.rect = self.image.get_rect(center = (162, 757) )
        self.angle = 0

    def update(self):
        rectl = rotatedflipl.get_rect(center = (162, 757) )


    def rotate(self):
        self.angle += 15
        pygame.transform.rotate(imageflipl, angleL)
        if angleL >= 70:
            rotatingL = False







def lancement():
        global y
        Ball.speed = (0, -5)

continuer = True
while continuer:
    fenetre.fill( [0, 0, 0] )
    fenetre.fill( [175, 0, 0], rect )
    fenetre.fill( [0, 0, 0], rect1)

    # on l'affiche aux coordonnées (10,10)
    #fenetre.blit(rotatedflipl, rectl) (mis sous commentaire pour voir si le programme fonctionnait sans)
    #fenetre.blit(rotatedflipr, rectr)
    fenetre.blit(imageball, (590,840))
    fenetre.blit(bumper, (200, 100))
    fenetre.blit(bumper, (400, 300))
    fenetre.blit(bumper, (150, 450))


    pygame.display.flip()
    ballGroup.update()
    ballGroup.draw(fenetre)
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
            if event.key == K_SPACE:
                lancement()





    if rotatingR:
        angleR -= 15
        rotatedflipr = pygame.transform.rotate(imageflipr, angleR)
        rectr = rotatedflipr.get_rect(center = (494, 757) )
        if angleR <= -70:
            rotatingR = False

    if rotatingL:
        FlipperL.rotate()


    clock.tick(60)



# On quitte proprement pygame
pygame.quit()
