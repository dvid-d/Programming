import sys

from os.path import abspath
from inspect import getsourcefile
path = abspath(getsourcefile(lambda:0))[:-16]

sys.path.append(f"{path}\\Game Properties")
sys.path.append(f"{path}\\Fonts")
sys.path.append(f"{path}\\Maps")
sys.path.append(f"{path}\\RunTime")
sys.path.append(f"{path}\\Saves")
sys.path.append(f"{path}\\Trains")


import pygame, button, main, shop

class Settings():
    def __init__(self, volume, difficulty):
        self.__volume = volume
        self.__difficulty = difficulty

    def InGameSettings(self, screen, game_settings, path):
        inSettings = True
        while inSettings is True:
            quit_button, back_button = game_settings.Display(screen, path) #add shop_button
            if back_button.wasClicked():
                inSettings = False
            elif quit_button.wasClicked():
                #ask user if they want to save
                #save if they want to
                main.Quit()
                pygame.display.update()
            """
            elif help_button.wasClicked():
                load help section
                
            elif map_key.wasClicked():
                Load map key
                """
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        inSettings = False
                    
            pygame.display.update()

    def Display(self,screen, path):
        background = pygame.Rect(300,100,1000,700)
        pygame.draw.rect(screen, (255,255,255), background)

        border = pygame.Rect(300,100,1000,700)
        pygame.draw.rect(screen,(0,0,0),border,2)

        quit_button_icon = pygame.image.load(f'{path}\\icons\\quit_button.png')
        quit_button = button.Button(screen, 700, 700, quit_button_icon, 0.35)

        back_button_icon = pygame.image.load(f"{path}\\icons\\back_button.png")
        back_button = button.Button(screen, 1190, 110, back_button_icon, 0.2)



        #controls sub section
        return quit_button, back_button
