import sys

from os.path import abspath
from inspect import getsourcefile
from button import *
path = abspath(getsourcefile(lambda:0))[:-16]

sys.path.append(f"{path}\\Game Properties")
sys.path.append(f"{path}\\Fonts")
sys.path.append(f"{path}\\Maps")
sys.path.append(f"{path}\\RunTime")
sys.path.append(f"{path}\\Saves")
sys.path.append(f"{path}\\Trains")


import pygame, main

class Settings():
    def __init__(self, volume, difficulty):
        self.__volume = volume
        self.__difficulty = difficulty

    def InGameSettings(screen, path, isInSettings):
        while isInSettings:
            quit_button, back_button = Settings.Display(screen, path) #add shop_button
            if back_button.wasClicked():
                isInSettings = False
            elif quit_button.wasClicked():
                #ask user if they want to save
                #save if they want to
                isInSettings = False
                main.Quit()
                pygame.display.update()
            # """
            # elif help_button.wasClicked():
            #     load help section
                
            # elif map_key.wasClicked():
            #     Load map key
            #     """
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        isInSettings = False
            pygame.display.update()
        pygame.display.update()
        return isInSettings
    
    def loadIcons(path):
        settings_button_icon = pygame.image.load(f"{path}\\Icons\\cog.png")
        return settings_button_icon

    def loadButtons(surface, path, SCREEN_WIDTH, SCREEN_HEIGHT):
        settings_button_icon = Settings.loadIcons(path)
        settings_button = Button(surface, SCREEN_WIDTH/20 - 70, SCREEN_HEIGHT/20 - 30, settings_button_icon, 1/(4.5)) #creates settings button
        return settings_button  

    def Display(screen, path):
        background = pygame.Rect(300,100,1000,700)
        pygame.draw.rect(screen, (255,255,255), background)

        border = pygame.Rect(300,100,1000,700)
        pygame.draw.rect(screen,(0,0,0),border,2)

        quit_button_icon = pygame.image.load(f'{path}\\icons\\quit_button.png')
        quit_button = Button(screen, 700, 700, quit_button_icon, 0.35)

        back_button_icon = pygame.image.load(f"{path}\\icons\\back_button.png")
        back_button = Button(screen, 1190, 110, back_button_icon, 0.2)
        return quit_button, back_button

    def checkButtons(buttons, surface, path):
        if buttons[0].wasClicked():
            isInSettings = True
            Settings.InGameSettings(surface, path, isInSettings)
            buttons[0].setClicked(False)

        #controls sub section
