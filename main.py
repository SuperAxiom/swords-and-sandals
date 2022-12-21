import os
import pygame

ptint("A little change")
pygame.display.init()
pygame.display.set_caption("Swords And Sandals")
screen = pygame.display.set_mode((1280, 720))
screen.fill(pygame.Color(255, 0, 0))
pygame.display.flip()

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(60)

pygame.quit()