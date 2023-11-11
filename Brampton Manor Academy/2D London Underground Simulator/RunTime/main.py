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
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Game Properties")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Fonts")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Maps")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\RunTime")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Saves")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Trains")


import pygame, os
import button, controls, settings, play, game, saves, time
from inspect import getsourcefile
from os.path import abspath
from pytmx.util_pygame import load_pygame


def SetUpScreen():
    SCREEN_WIDTH = 1600
    SCREEN_HEIGHT = 1250
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # sets window width & length
    pygame.display.set_caption('2D London Underground Simulator') # sets window name
    screen.fill((58,208,241)) # sets window colour

    path = abspath(getsourcefile(lambda:0))[:-16] # obtains path of program
    icon = pygame.image.load(f'{path}\\RunTime\\underground.png') # opens program icon
    pygame.display.set_icon(icon) #sets window icon
    
    return SCREEN_WIDTH, SCREEN_HEIGHT, screen, path


def MainMenu(path, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    start_button_icon = pygame.image.load(f"{path}\\Icons\\play_button.png")
    start_button = button.Button(screen, SCREEN_WIDTH/2.8, SCREEN_HEIGHT/2.4, start_button_icon, 9/20)

    quit_button_icon = pygame.image.load(f"{path}\\Icons\\quit_button.png")
    quit_button = button.Button(screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2.4, quit_button_icon, 9/20)

    return start_button, quit_button


def SavesMenu(path, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    back_button, save_1_button, save_2_button, save_3_button = saves.Saves.LoadMenu(screen, SCREEN_WIDTH, SCREEN_HEIGHT, path)
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
                if lines[0][9:][:-1] == "False":
                    save_name = saves.Saves.ChangeFileName(screen, path, "save_1.txt")
                    file_1.close()
                    file = open(f"{path}\\Saves\\check_saves.txt","w")
                    file.write("save_1 = True" +"\n")
                    file.write(lines[1][:-1] + "\n")
                    file.write(lines[2])
                    file.close()
                else:
                    save_name = saves.Saves.GetSaveName(path, "1")
                save_data = saves.Saves.GetSaveInfo(screen, path, save_name)
                return save_data
            elif save_2_button.wasClicked():
                if lines[1][9:] == "False":
                    save_name = saves.Saves.ChangeFileName(screen, path,"save_2.txt")
                    file = open(f"{path}\\Saves\\check_saves.txt","w")
                    file_1.close()
                    file.write(lines[0])
                    file.write("save_2 = True")
                    file.write(lines[2])
                    file.close()
                else:
                    save_name = saves.Saves.GetSaveName(path, "2")
                save_data = saves.Saves.GetSaveInfo(save_name+".txt")
                return save_data
            elif save_3_button.wasClicked():
                if lines[2][9:] == "False":
                    save_name = saves.Saves.ChangeFileName(screen, path,"save_3.txt")
                    file_1.close()
                    file = open(f"{path}\\Saves\\check_saves.txt","w")
                    file.write(lines[0])
                    file.write(lines[1])
                    file.write("save_3 = True")
                    file.close()
                else:
                    save_name = saves.Saves.GetSaveName(path, "3")
                save_data = saves.Saves.GetSaveInfo(save_name+".txt")
                return save_data

        pygame.display.update()


def Quit():
    pygame.quit()
    exit()

def Reset():
    #to reset game files to default
    pass


def Play(path, game, screen, map, SCREEN_WIDTH, SCREEN_HEIGHT):
    play.Play.Load(path, screen, map)
    play.Play.Run(screen, path, SCREEN_WIDTH, SCREEN_HEIGHT, game, map)
    

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    game = game.Game(1) #states_dict = {"startUp":1,"returnToMain":2,"savesMenu":3,"returnToSaves":4,"playGame":5,"inSettings":6}
    SCREEN_WIDTH, SCREEN_HEIGHT, screen, path = SetUpScreen() # sets up screen & frame rate
    run = True
    while run:
        if game.state == 1 or game.state == 2:
            if game.state == 2:
                screen.fill((58,208,241))
            start_button, quit_button = MainMenu(path, screen, SCREEN_WIDTH, SCREEN_HEIGHT)
            if quit_button.wasClicked(): #shuts the game down if the quit button is clicked
                run = False
            elif start_button.wasClicked(): # changes game state so save menu is shown
                time.sleep(1)
                game.changeState(3)

        elif game.state == 3 or game.state == 4:
            map_data = SavesMenu(path, screen, SCREEN_WIDTH, SCREEN_HEIGHT)

        elif game.state == 5:
            Play(path, game, screen, map_data, SCREEN_WIDTH, SCREEN_HEIGHT)
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()                
        pygame.display.update()
        clock.tick(60) # max framerate
    pygame.quit()