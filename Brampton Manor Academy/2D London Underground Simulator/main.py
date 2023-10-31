# shortcut to run file is F5
# create option to delete all progress
# __init__ means 'initialise'
# image = pygame.image.load(location) to load an image.
# screen.blit(image,(coordinates))
# text = pygame.font.Font(Font name, size)
# text_surface = text.render(text to be displayed, Anti-Aliase (T/F) (smooths edges of text), colour (RGB))
# screen.blit(text_surface, (coordinates))
# shift+tab to unindent blocks of code

import pygame, sys, button, tile, gameState, controls, settings, play, game
from inspect import getsourcefile
from os.path import abspath
from pytmx.util_pygame import load_pygame


def SetUpScreen():
    SCREEN_WIDTH = 1600
    SCREEN_HEIGHT = 1250
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # sets window width & length
    pygame.display.set_caption('2D London Underground Simulator') # sets window name
    screen.fill((58,208,241)) # sets window colour

    path = abspath(getsourcefile(lambda:0))[:-8] # obtains path of program
    icon = pygame.image.load(f'{path}\\underground.png') # opens program icon
    pygame.display.set_icon(icon) #sets window icon
    
    return SCREEN_WIDTH, SCREEN_HEIGHT, screen, path


def MainMenu(path, screen):
    start_button_icon = pygame.image.load(f"{path}\\Icons\\play_button.png")
    start_button = button.Button(screen, SCREEN_WIDTH/2.8, SCREEN_HEIGHT/2.4, start_button_icon, 9/20)

    quit_button_icon = pygame.image.load(f"{path}\\Icons\\quit_button.png")
    quit_button = button.Button(screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2.4, quit_button_icon, 9/20)

    return start_button, quit_button


def SavesMenu(path, screen):
    screen.fill((58,208,241))
    save_rect = pygame.image.load(f"{path}\\Icons\\save_rect.png") # loads the background for each button
    save_1_button = button.Button(screen, SCREEN_WIDTH/4, SCREEN_HEIGHT/3.2, save_rect, 1) # creates the first, second and third buttons respectivelly
    save_2_button = button.Button(screen, SCREEN_WIDTH/4, SCREEN_HEIGHT/2.4, save_rect, 1)
    save_3_button = button.Button(screen, SCREEN_WIDTH/4, SCREEN_HEIGHT/1.9, save_rect, 1)

    save_surface = pygame.font.Font(f"{path}\\Fonts\\Lora-VariableFont_wght.ttf", 40)
    save_1_surface = save_surface.render("Save 1", True, "black")
    save_2_surface = save_surface.render("Save 2", True, "black")
    save_3_surface = save_surface.render("Save 3", True, "black")

    screen.blit(save_1_surface, (SCREEN_WIDTH/4 + 10, SCREEN_HEIGHT/3))
    screen.blit(save_2_surface, (SCREEN_WIDTH/4 + 10, SCREEN_HEIGHT/3 + 120))
    screen.blit(save_3_surface, (SCREEN_WIDTH/4 + 10, SCREEN_HEIGHT/3 + 260))

    back_button_image = pygame.image.load(f"{path}\\Icons\\back_button.png") #CHANGE BUTTON
    back_button = button.Button(screen, x=SCREEN_WIDTH/5, y=SCREEN_HEIGHT/10, image=back_button_image, scale=1)
    while game.state == 3 or game.state == 4:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        if back_button.wasClicked():
            game.changeState(2)
        if save_1_button.wasClicked():
            game.changeState(5)
            game_levels = []
            game_file = open("save_1.txt", "r")
            line = game_file.readline()[:-1] #exclude \n at end of line
            level = line[-3]
            
            return map

        pygame.display.update()


def Quit():
    pygame.quit()
    exit()


def Play(path, gameState, screen, map, SCREEN_WIDTH, SCREEN_HEIGHT):
    play.Play.Load(path, screen, map)
    play.Play.Run(screen, path, SCREEN_WIDTH, SCREEN_HEIGHT, gameState)
    

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    gameState = game.Game(1) #states_dict = {"startUp":1,"returnToMain":2,"savesMenu":3,"returnToSaves":4,"playGame":5,"inSettings":6}
    SCREEN_WIDTH, SCREEN_HEIGHT, screen, path = SetUpScreen() # sets up screen & frame rate
    
    run = True
    first_run = True
    while run:
        if game.state == 1 or game.state == 2:
            if game.state == 2:
                screen.fill((58,208,241))
            start_button, quit_button = MainMenu(path, screen)
            if quit_button.wasClicked(): #shuts the game down if the quit button is clicked
                run = False
            elif start_button.wasClicked(): # changes game state so save menu is shown
                gameState.changeState(3)

        elif gameState.state == 3 or gameState.state == 4:
            map = SavesMenu(path, screen)

        elif game.state == 5:
            if first_run is True:
                map = "victoria line" # change so that the map is selected from the save file data
                Play(path, game.state, screen, map, SCREEN_WIDTH, SCREEN_HEIGHT)
            else:
                map = "victoria line" # change so that the map is selected from the save file data
                Play(path, game.state, screen, map, SCREEN_WIDTH, SCREEN_HEIGHT)
                pass
            first_run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()                
        pygame.display.update()
        clock.tick(60) # max framerate
    pygame.quit()