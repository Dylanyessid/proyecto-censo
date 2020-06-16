import pygame
pygame.init()

size=(800,600)
screen=pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
