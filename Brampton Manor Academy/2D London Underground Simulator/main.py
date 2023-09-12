# shortcut to run file is F5
# create option to delete all progress
# __init__ means 'initialise'
# image = pygame.image.load(location) to load an image.
# screen.blit(image,(coordinates))
# text = pygame.font.Font(Font name, size)
# text_surface = text.render(text to be displayed, Anti-Aliase (T/F) (smooths edges of text), colour (RGB))
# screen.blit(text_surface, (coordinates))
# shift+tab to unindent blocks of code

import pygame
from sys import exit
from inspect import getsourcefile
from os.path import abspath
import button
import gameState
import controls


def SetUpScreen():
    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 540
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # sets window width & length
    pygame.display.set_caption('2D London Underground Simulator') # sets window name
    screen.fill((58,208,241)) # sets window colour
    path = abspath(getsourcefile(lambda:0))[:-8] # obtains path of program
    icon = pygame.image.load(f'{path}\\underground.png') # opens program icon
    pygame.display.set_icon(icon) #sets window icon
    return SCREEN_WIDTH, SCREEN_HEIGHT, screen, path


def MainMenu(path, screen):
    start_button_icon = pygame.image.load(f"{path}\\Icons\\play_button.png")
    start_button = button.Button(screen, 180, 220, start_button_icon, 9/20)

    quit_button_icon = pygame.image.load(f"{path}\\Icons\\quit_button.png")
    quit_button = button.Button(screen, 560, 220, quit_button_icon, 9/20)

    return start_button, quit_button


def SavesMenu(path, screen):
    screen.fill((58,208,241))
    
    save_rect = pygame.image.load(f"{path}\\Icons\\save_rect.png") # loads the background for each button
    save_1_button = button.Button(screen, 40, 90, save_rect, 1) # creates the first, second and third buttons respectivelly
    save_2_button = button.Button(screen, 40, 200, save_rect, 1)
    save_3_button = button.Button(screen, 40, 310, save_rect, 1)

    save_surface = pygame.font.Font(f"{path}\\Fonts\\Lora-VariableFont_wght.ttf", 40)
    save_1_surface = save_surface.render("Save 1", True, "black")
    save_2_surface = save_surface.render("Save 2", True, "black")
    save_3_surface = save_surface.render("Save 3", True, "black")

    screen.blit(save_1_surface, (50,110))
    screen.blit(save_2_surface, (50,220))
    screen.blit(save_3_surface, (50,330))
    return save_1_button, save_2_button, save_3_button

def Quit():
    pygame.quit()
    exit()


def Play():
    pygame.display.update()
    

if __name__ == '__main__':
    pygame.init()
    run = True
    #states = {"startUp":1,"savesMenu":2,"playGame":3,"inSettings":4,"returnToMenu":5,"returnToSaves":6}

    # sets up screen & frame rate
    SCREEN_WIDTH, SCREEN_HEIGHT, screen, path = SetUpScreen()
    clock = pygame.time.Clock()
    
    # main game loop
    while run:
        if startUp == True or gameState.state == True:
            start_button, quit_button = MainMenu(path, screen)
            if quit_button.wasClicked():
                run = False
            elif start_button.wasClicked():
                startUp = False
                savesMenu = True
        elif savesMenu == True or returnToSaves == True:
            save_1_button, save_2_button, save_3_button = SavesMenu(path, screen)
            if save_1_button.wasClicked():
                savesMenu = False
                returnToSaves = False
                print("00000000000000000000000000000000000000000")
                #load file and generate game map for all three save options
            elif save_2_button.wasClicked():
                savesMenu = False
                returnToSaves = False
            elif save_3_button.wasClicked():
                savesMenu = False
                returnToSaves = False
        elif playGame == True:
            Play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        pygame.display.update()
        clock.tick(60) # max framerate
    pygame.quit()