# shortcut to run file is F5
# create option to delete all progress
# __init__ means 'initialise'
# image = pygame.image.load(location) to load an image.
# screen.blit(image,(coordinates))
# text = pygame.font.Font(Font name, size)
# text_surface = text.render(text to be displayed, Anti-Aliase (T/F) (smooths edges of text), colour (RGB))
# screen.blit(text_surface, (coordinates))
# shift+tab to unindent blocks of code

import sys
from os.path import abspath
from inspect import getsourcefile

path = abspath(getsourcefile(lambda:0))[:-16] # obtains path of program
sys.path.append(f"{path}\\Game Properties")
sys.path.append(f"{path}\\Fonts")
sys.path.append(f"{path}\\Maps")
sys.path.append(f"{path}\\RunTime")
sys.path.append(f"{path}\\Saves")
sys.path.append(f"{path}\\Trains")


import pygame
import time
import pyautogui
from pytmx.util_pygame import load_pygame
from button import *
from controls import *
from settings import *
from play import *
from game import *
from saves import *


def SetUpScreen():
    screen_dimensions = pyautogui.size()
    SCREEN_WIDTH = screen_dimensions[0]
    SCREEN_HEIGHT = screen_dimensions[1]
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # sets window width & length
    pygame.display.set_caption('2D London Underground Simulator') # sets window name
    screen.fill((58,208,241)) # sets window colour

    path = abspath(getsourcefile(lambda:0))[:-16] # obtains path of program
    icon = pygame.image.load(f'{path}\\RunTime\\underground.png') # opens program icon
    pygame.display.set_icon(icon) #sets window icon
    
    return SCREEN_WIDTH, SCREEN_HEIGHT, screen, path


def MainMenu(path, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    start_button_icon = pygame.image.load(f"{path}\\Icons\\play_button.png")
    start_button = Button(screen, SCREEN_WIDTH/2.8, SCREEN_HEIGHT/2.4, start_button_icon, 9/20)

    quit_button_icon = pygame.image.load(f"{path}\\Icons\\quit_button.png")
    quit_button = Button(screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2.4, quit_button_icon, 9/20)

    quick_load_icon = pygame.image.load(f"{path}\\Icons\\quick_button.png")
    quick_load_button = Button(screen, SCREEN_WIDTH/1.5, SCREEN_HEIGHT/2.4, quick_load_icon, 9/20)
    return start_button, quit_button, quick_load_button


def SavesMenu(path, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    back_button, save_1_button, save_2_button, save_3_button = Saves.LoadMenu(screen, SCREEN_WIDTH, SCREEN_HEIGHT, path)
    while game.state == 3 or game.state == 4:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        if back_button.wasClicked():
            game.changeState(2)

        elif save_1_button.wasClicked() or save_2_button.wasClicked() or save_3_button.wasClicked():
            game.changeState(5)
            file_1 = open(f"{path}\\Saves\\check_saves.txt","r")
            lines = file_1.readlines()
            if save_1_button.wasClicked():
                save_data = Saves.GetSaveInfo("save_1.json", path)
                if lines[0][9:][:-1] == "False":
                    Saves.ChangeSaveName(screen, path, "save_1.txt", save_data)
                    file_1.close()
                    file = open(f"{path}\\Saves\\check_saves.txt","w")
                    file.write("save_1 = True" +"\n")
                    file.write(lines[1][:-1] + "\n")
                    file.write(lines[2])
                    file.close()                
            elif save_2_button.wasClicked():
                save_data = Saves.GetSaveInfo("save_2.txt", path)
                if lines[1][9:] == "False":
                    Saves.ChangeSaveName(screen, path,"save_2.txt")
                    file = open(f"{path}\\Saves\\check_saves.txt","w")
                    file_1.close()
                    file.write(lines[0][:-1] + "\n")
                    file.write("save_2 = True" +"\n")
                    file.write(lines[2])
                    file.close()
            elif save_3_button.wasClicked():
                save_data = Saves.GetSaveInfo("save_3.txt", path)
                if lines[2][9:] == "False":
                    Saves.ChangeSaveName(screen, path,"save_3.txt")
                    file_1.close()
                    file = open(f"{path}\\Saves\\check_saves.txt","w")
                    file.write(lines[0] + "\n")
                    file.write(lines[1] + "\n")
                    file.write("save_3 = True")
                    file.close()
            return save_data

        pygame.display.update()


def Quit():
    pygame.quit()
    exit()

def ResetFiles():
    #to reset game files to default
    pass


def StartGame(path, game, screen, save_data, SCREEN_WIDTH, SCREEN_HEIGHT):
    Play.Run(screen, path, save_data, SCREEN_WIDTH, SCREEN_HEIGHT, game)

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()

    game = Game(1) #states_dict = {"startUp":1,"returnToMain":2,"savesMenu":3,"returnToSaves":4,"playGame":5,"inSettings":6}
    SCREEN_WIDTH, SCREEN_HEIGHT, screen, path = SetUpScreen() # sets up screen & frame rate
    
    run = True
    while run:
        if game.state == 1 or game.state == 2:
            if game.state == 2:
                screen.fill((58,208,241))
            start_button, quit_button, quick_load_button = MainMenu(path, screen, SCREEN_WIDTH, SCREEN_HEIGHT)
            if quit_button.wasClicked(): #shuts the game down if the quit button is clicked
                run = False
            elif start_button.wasClicked(): # changes game state so save menu is shown
                time.sleep(1)
                game.changeState(3)
            elif quick_load_button.wasClicked():
                save_data = Saves.GetSaveInfo(f"{path}\\Saves\\save_1.json")
                game.changeState(5)

        elif game.state == 3 or game.state == 4:
            save_data = SavesMenu(path, screen, SCREEN_WIDTH, SCREEN_HEIGHT)

        elif game.state == 5:
            StartGame(path, game, screen, save_data, SCREEN_WIDTH, SCREEN_HEIGHT)
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()                
        pygame.display.update()
        clock.tick(60) # max framerate
    pygame.quit()