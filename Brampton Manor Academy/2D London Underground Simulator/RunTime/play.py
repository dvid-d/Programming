
import sys
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Game Properties")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Fonts")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Maps")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\RunTime")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Saves")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Trains")

import pygame, settings, main, button, gameState, tile
from pytmx.util_pygame import load_pygame

class Play():
    def Load(path, screen, map):
        sprite_group = Play.LoadMap(path, map)
        sprite_group.draw(screen)

    def LoadMap(path, map):
        map_data = load_pygame(f'{path}\\Maps\\{map}.tmx') #CHANGE THIS
        sprite_group = pygame.sprite.Group()
        for layer in map_data.visible_layers:
            for x,y,surface in layer.tiles():
                pos = (x*192,y*108) # size of tiles
                tile.Tile(pos = pos, surface = surface, groups = sprite_group)
        #for object in map_data.visible_object_groups():
            #print(object)
        return sprite_group
        
    def CheckIfClicked(buttons, screen, game_settings, path):
            if buttons[0].wasClicked():
                main.Quit()
            if buttons[1].wasClicked():
                game_settings.InGameSettings(screen, game_settings, path)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def Run(screen, path, SCREEN_WIDTH, SCREEN_HEIGHT, game):
        while game.state == 5:
            settings_button_icon = pygame.image.load(f"{path}\\Icons\\cog.png")
            settings_button = button.Button(screen, SCREEN_WIDTH/1.17 - 200, SCREEN_HEIGHT/6, settings_button_icon, 1/(4.5))
            game_settings = settings.Settings(100, 3)

            quit_button_icon = pygame.image.load(f"{path}\\Icons\\quit_button.png")
            quit_button = button.Button(screen, SCREEN_WIDTH/1.11, SCREEN_HEIGHT/6, quit_button_icon, 1/4)

            buttons = [quit_button, settings_button]
            Play.CheckIfClicked(buttons, screen, game_settings, path)
            
            pygame.display.update()

            