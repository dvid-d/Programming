# shortcut to run file is F5

import pygame
import Button

pygame.init()


def MainMenu():
    screen_width = 1920
    screen_height = 1080
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("2D London Underground Simulator")
    pygame.display.update()
    return screen_width, screen_height, screen


def Play():
    pygame.display.update()
    

if __name__ == '__main__':
    run = True
    screen_width, screen_height, screen = MainMenu()
    while run:
        Play()
    pygame.quit()