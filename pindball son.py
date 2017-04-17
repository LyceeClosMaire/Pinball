import pygame
from pygame.locals import *



pygame.init()
# ***
# on crée une fenêtre de 800x600 pixels
fenetre = pygame.display.set_mode( (800,900) )
# ***

son = pygame.mixer.Sound('issou.wav')
son.play(loops=-1, maxtime=0, fade_ms=0)

# on charge une image dans la variable "image"
imageflipl = pygame.image.load("flippersL.png").convert_alpha()
imageflipr = pygame.image.load("flippersR.png").convert_alpha()

continuer = True
while continuer:


    # on l'affiche aux coordonnées (10,10)
    fenetre.blit(imageflipl, (162,720))
    fenetre.blit(imageflipr, (395,720))

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



# On quitte proprement pygame
pygame.quit()