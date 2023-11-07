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
    def Load(path, screen, save_data):
        sprite_group = Play.LoadMap(path, save_data[0])
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
                game_settings.InGameSettings(screen, game_settings, path)
                return True
            else:
                return False
            

    def Run(screen, path, SCREEN_WIDTH, SCREEN_HEIGHT, game, map):
        game_settings = settings.Settings(100, 3)
        settings_button_icon = pygame.image.load(f"{path}\\Icons\\cog.png")
        while game.state == 5:
            settings_button = button.Button(screen, SCREEN_WIDTH/1.17 - 1325, SCREEN_HEIGHT/6-10, settings_button_icon, 1/(4.5))
            buttons = [settings_button]
            clicked = Play.CheckIfClicked(buttons, screen, game_settings, path)
            if clicked is True:
                Play.Load(path, screen, map)
                
            #Simulation code

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

            