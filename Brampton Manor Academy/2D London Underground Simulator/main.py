# shortcut to run file is F5

import pygame
from inspect import getsourcefile
from os.path import abspath
import Button
import controls


def SetUpScreen():
    screen_width = 960
    screen_height = 540
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('2D London Underground Simulator')
    screen.fill((58,208,241))
    path = abspath(getsourcefile(lambda:0))[:-8]
    print(path)
    icon = pygame.image.load(f'{path}\\underground.png')
    pygame.display.set_icon(icon)
    return screen_width, screen_height, screen, path


def MainMenu(path):
    start_icon = pygame.image.load(f"{path}\\Icons\\play_button.png").convert_alpha()
    pygame.display.update()


def Play():
    pygame.display.update()
    

if __name__ == '__main__':
    pygame.init()
    run = True
    screen_width, screen_height, screen, path = SetUpScreen()
    #MainMenu(path)
    while run:
        Play()
    pygame.quit()