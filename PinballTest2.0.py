# CrÃƒÂ©ÃƒÂ© par guyard, le 27/03/2017 en Python 3.2
# CrÃƒÂ©ÃƒÂ© par guyard, le 27/03/2017 en Python 3.2

# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import math

x=600
y=850

pygame.init()
fenetre = pygame.display.set_mode( (800,900) )
rectgame = pygame.rect.Rect( (0,0), (650,900))
wingame = rectgame



clock = pygame.time.Clock()
son = pygame.mixer.Sound('issou.wav')
son.play(loops=-1, maxtime=0, fade_ms=0)





bumper = pygame.image.load("bumperrage.png").convert_alpha()
rect = pygame.rect.Rect( (650,0), (280,900)   )
rect1 = pygame.rect.Rect( (660,10), (130,880) )






class Ball(pygame.sprite.Sprite):

    def __init__(self, position, speed):
        super().__init__()
        self.speed = speed
        self.image = pygame.image.load("voltball.png")
        self.rect = self.image.get_rect(center=position)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if not wingame.contains(self):
            rect = self.rect
            self.speed = rebound(self.speed, wingame.left > rect.left or wingame.right < rect.right, wingame.top > rect.top or wingame.bottom < rect.bottom )
        self.rect.move_ip(self.speed)

    def draw(self,window):
        window.blit(self.image, self.rect)

ball = Ball( (600,850), (0, 0) )

class FlipperL(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("flippersL.png")
        self.image = self.original_image
        self.rect = self.image.get_rect(center = (162, 757) )
        self.angle = 0
        self.rotating = False
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.rotating:
            self.angle += 15
            if self.angle >= 70:
                self.rotating = False
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = (162, 757) )



class FlipperR(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("flippersR.png")
        self.image = self.original_image
        self.rect = self.image.get_rect(center = (494, 757) )
        self.angle = 0
        self.rotating = False
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.rotating:
            self.angle -= 15
            if self.angle <= -70:
                self.rotating = False
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = (494, 757) )


def rebound(speed, left_or_right, bottom_or_top):
   (x,y) = speed
   if left_or_right:
       x = -x
   if bottom_or_top:
       y = -y
   return (x,y)


flipperL = FlipperL()
flipperR = FlipperR()

flippers = pygame.sprite.Group( flipperL, flipperR )



def lancement():
    global ball
    ball = Ball( (600,850), (-25,-5) )


continuer = True
while continuer:
    fenetre.fill( [0, 0, 0] )
    fenetre.fill( [175, 0, 0], rect )
    fenetre.fill( [0, 0, 0], rect1)


    fenetre.blit(bumper, (200, 100))
    fenetre.blit(bumper, (400, 300))
    fenetre.blit(bumper, (150, 450))
    flippers.draw(fenetre)
    ball.draw(fenetre)


    pygame.display.flip()




    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            continuer = False


        if event.type == KEYDOWN:

            if event.key == K_RIGHT:
                flipperR.rotating = True

            elif event.key == K_LEFT:
                flipperL.rotating = True

            elif event.key == K_SPACE:
                lancement()



        if event.type == KEYUP:
            if event.key == K_RIGHT:
                flipperR.rotating = False
                flipperR.angle = 0
            if event.key == K_LEFT:
                flipperL.rotating = False
                flipperL.angle = 0



    ball.update()
    flippers.update()



    clock.tick(60)




pygame.quit()
