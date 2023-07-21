# shortcut to run file is F5
# create option to delete all progress
# __init__ means 'initialise'
# image = pygame.image.load(location) to load an image.
# screen.blit(image,(coordinates))
# text = pygame.font.Font(Font name, size)
# text_surface = text.render(text to be displayed, Anti-Aliase (T/F) (smooths edges of text), colour (RGB))
# screen.blit(text_surface, (coordinates))


import pygame
from sys import exit
from inspect import getsourcefile
from os.path import abspath
import button
import controls


def SetUpScreen():
    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 540
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption('2D London Underground Simulator')
    screen.fill((58,208,241))
    path = abspath(getsourcefile(lambda:0))[:-8]
    icon = pygame.image.load(f'{path}\\underground.png')
    pygame.display.set_icon(icon)
    return SCREEN_WIDTH, SCREEN_HEIGHT, screen, path


def MainMenu(path, screen):
    start_button_icon = pygame.image.load(f"{path}\\Icons\\play_button.png")
    start_button = button.Button(screen, 180, 220, start_button_icon, 9/20)

    quit_button_icon = pygame.image.load(f"{path}\\Icons\\quit_button.png")
    quit_button = button.Button(screen, 560, 220, quit_button_icon, 9/20)
    return start_button, quit_button


def SavesMenu(path, screen, savesMenu):
    returnToSaves = False
    screen.fill((58,208,241))
    
    while savesMenu:
        pygame.display.update()
        save_1_surface = pygame.font.Font(f"{path}\\Fonts\\Lora-VariableFont_wght.ttf", 40)
        save_1_surface = save_1_surface.render("Save 1", True, "black")
        screen.blit(save_1_surface, (50,100))
        save_1_rect = pygame.Rect(50,70, 500, 100)
        save_1_button = button.Button(screen, 50, 100, image, 1)
        pygame.display.update()
    return savesMenu, returnToSaves


def Quit():
    pygame.quit()
    exit()


def Play():
    pygame.display.update()
    

if __name__ == '__main__':
    pygame.init()
    run = True
    # game states
    startUp = True
    savesMenu = False
    playGame = False
    inSettings = False
    returnToMenu = False
    returnToSaves = False

    # sets up screen & frame rate
    SCREEN_WIDTH, SCREEN_HEIGHT, screen, path = SetUpScreen()
    clock = pygame.time.Clock()
    
    # main game loop
    while run:
        if startUp == True or returnToMenu == True:
            start_button, quit_button = MainMenu(path, screen)
            if quit_button.wasClicked():
                run = False
            elif start_button.wasClicked():
                startUp = False
                savesMenu = True
        elif savesMenu == True or returnToSaves == True:
            savesMenu, returnToSaves = SavesMenu(path, screen, savesMenu)
        elif playGame == True:
            Play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        pygame.display.update()
        clock.tick(60) # max framerate
    pygame.quit()