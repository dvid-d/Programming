# shortcut to run file is F5
# create option to delete all progress
# __init__ means 'initialise'
# image = pygame.image.load(location) to load an image.
# screen.blit(image,(coordinates))
# text = pygame.font.Font(Font name, size)
# text_surface = text.render(text to be displayed, Anti-Aliase (T/F) (smooths edges of text), colour (RGB))
# screen.blit(text_surface, (coordinates))
# shift+tab to unindent blocks of code

import pygame, sys, button, tile, gameState, controls
from inspect import getsourcefile
from os.path import abspath
from pytmx.util_pygame import load_pygame


def SetUpScreen():
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
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
    # save_2_button = button.Button(screen, SCREEN_WIDTH/4, SCREEN_HEIGHT/2.4, save_rect, 1)
    # save_3_button = button.Button(screen, SCREEN_WIDTH/4, SCREEN_HEIGHT/1.9, save_rect, 1)

    save_surface = pygame.font.Font(f"{path}\\Fonts\\Lora-VariableFont_wght.ttf", 40)
    save_1_surface = save_surface.render("Save 1", True, "black")
    # save_2_surface = save_surface.render("Save 2", True, "black")
    # save_3_surface = save_surface.render("Save 3", True, "black")

    screen.blit(save_1_surface, (SCREEN_WIDTH/4 + 10, SCREEN_HEIGHT/3))
    # screen.blit(save_2_surface, (SCREEN_WIDTH/4 + 10, SCREEN_HEIGHT/3 + 110))
    # screen.blit(save_3_surface, (SCREEN_WIDTH/4 + 10, SCREEN_HEIGHT/3 + 230))
    
    return save_1_button #, save_2_button, save_3_button

def Quit():
    pygame.quit()
    exit()

def LoadMap():
    map_data = load_pygame(f'{path}\\Maps\\tutorial.tmx', pixelalpha = True) #CHANGE THIS
    sprite_group = pygame.sprite.Group()
    for layer in map_data.visible_layers:
        if True:
            for x,y,surface in layer.tiles():
                pos = (x*126+200,y*72 + 50) #10x15 tiles
                tile.Tile(pos = pos, surface = surface, groups = sprite_group)
    return sprite_group

def InGameSettings(screen): #ONLY CONTAINS LEAVE BUTTON
    quit_button_icon = pygame.image.load(f"{path}\\Icons\\quit_button.png")
    leave_button = button.Button(screen, 0, 0, quit_button_icon, 0.5)
    return leave_button

def Play(path, gameState, screen):
    sprite_group = LoadMap()
    while gameState.state == 5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        sprite_group.draw(screen)
        #leave_button = InGameSettings(screen)
        #if leave_button.wasClicked():
        #    gameState.changeState(4)
        pygame.display.update()
    

if __name__ == '__main__':
    pygame.init()
    run = True
    gameState = gameState.GameState(1) #states_dict = {"startUp":1,"returnToMain":2,"savesMenu":3,"returnToSaves":4,"playGame":5,"inSettings":6}

    # sets up screen & frame rate
    SCREEN_WIDTH, SCREEN_HEIGHT, screen, path = SetUpScreen()
    clock = pygame.time.Clock()
    
    # main game loop
    while run:
        if gameState.state == 1 or gameState.state == 2:
            start_button, quit_button = MainMenu(path, screen)
            if quit_button.wasClicked():
                run = False
            elif start_button.wasClicked():
                gameState.changeState(3)
        elif gameState.state == 3 or gameState.state == 4:
            save_1_button = SavesMenu(path, screen)
            if save_1_button.wasClicked():
                gameState.changeState(5)
        elif gameState.state == 5:
            Play(path, gameState, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        pygame.display.update()
        clock.tick(60) # max framerate
    pygame.quit()