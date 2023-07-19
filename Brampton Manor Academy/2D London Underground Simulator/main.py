# shortcut to run file is F5

import pygame
import Button

pygame.init()

screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("2D London Underground Simulator")

run = True
while run:

    screen.fill((237,239,228))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()