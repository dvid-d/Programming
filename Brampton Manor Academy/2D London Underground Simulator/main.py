# shortcut to run file is F5

import pygame
import Button

pygame.init()


def MainMenu():
    screen_width = 960
    screen_height = 540
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("2D London Underground Simulator")
    pygame.display.update()
    return screen_width, screen_height, screen


def Play():
    pygame.display.update()
    

if __name__ == '__main__':
    run = True
    screen_width, screen_height, screen = MainMenu()
    pygame.display.set_caption('2D London Underground Simulator')
    screen.fill((58,208,241))
    pygame.display.set_icon(Icon_name)
    while run:
        Play()
    pygame.quit()