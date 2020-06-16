import pygame
import sys

pygame.init()

size=(800,600)
ventana=pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill((0,0,0))

    pygame.display.flip()
