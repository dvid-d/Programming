import sys
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Game Properties")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Fonts")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Maps")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\RunTime")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Saves")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Trains")

import pygame, settings, main, button, gameState, tile, shop
from pytmx.util_pygame import load_pygame

class Play():
    def Load(path, screen, save_data, SCREEN_WIDTH, SCREEN_HEIGHT):
        sprite_group, map_data = Play.LoadMap(path, save_data, screen)
        sprite_group.draw(screen)
        objects = map_data.objects
        # track_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        for object in objects:
            if object.__class__ == "StationSouthbound":
                pass
            if object.type[:5] == "Track":
                track = object
                if track.type == "TrackSouthbound":
                    if track.name == "Southbound": #add to display NorthBound Track as well, add coordinates to a large list like [[victoria_line, [(coordtrack_1_x, coordtrack_1_y)], [(station_1_x, station_1,y)]],[central_line,[...]]]]
                        points = [(point.x, point.y) for point in track.points]
                        print(points)
                        pygame.draw.polygon(screen, (100,100,100), points, 1)
                        #points go clockwise from the bottom right
                        

        #also add Trains and other things

    def LoadMap(path, save_data, screen):
        map = Play.GetMap(save_data)
        map_data = load_pygame(f'{path}\\Maps\\{map}.tmx')
        sprite_group = pygame.sprite.Group()
        layers = map_data.visible_layers
        for layer in layers:
            if layer.name == "Tile Layer 1": #replace with layer name
                for x,y,surface in layer.tiles():
                    pos = (x*192,y*108) # size of tiles
                    tile.Tile(pos, surface, sprite_group)
        #for object in map_data.visible_object_groups():
            #print(object)
        return sprite_group, map_data
    
    def CheckForRewards():
        pass

    def GetMap(save_data):
        map = "level_" + str(int(save_data[3]))
        if save_data[3] == 1.0 or save_data[3] == 0.0:
            map = "level_1"
        elif save_data[3] == 2.0:
            map = "level_2"
        elif save_data[3] == 3.0:
            map = "level_3"
        elif save_data[3] == 4.0:
            map = "level_4"
        elif save_data[3] == 5.0:
            map = "level_5"
        elif save_data[3] == 6.0:
            map = "level_6"
        elif save_data[3] == 7.0:
            map = "level_7"
        elif save_data[3] == 8.0:
            map = "level_8"
        elif save_data[3] == 9.0:
            map = "level_9"
        elif save_data[3] == 10.0:
            map = "level_10"
        return map

    def CheckIfClicked(buttons, screen, game_settings, path):
            if buttons[0].wasClicked():
                game_settings.InGameSettings(screen, game_settings, path)
                return True
            # if buttons[1].wasClicked():
            #     shop.Shop.UseShop()
            #     return True
    
    def StartTutorial(save_data):
        pass
        save_data[3] = 2.0
        return save_data
        
    def CheckThreshold(save_data):
        money = save_data[-3]
        debt = save_data[-2]
        overall_money = money - debt
        if overall_money >= 50000000:
            save_data[3] = 10.0
        elif overall_money >= 40000000:
            save_data[3] = 9.0
        elif overall_money >= 20000000:
            save_data[3] = 8.0
        elif overall_money >= 10000000:
            save_data[3] = 7.0
        elif overall_money >= 5000000:
            save_data[3] = 6.0
        elif overall_money >= 1000000:
            save_data[3] = 5.0
        elif overall_money >= 500000:
            save_data[3] = 4.0
        elif overall_money >= 100000:
            save_data[3] = 3.0
        return save_data

    def Run(screen, path, save_data, SCREEN_WIDTH, SCREEN_HEIGHT, game):
        game_settings = settings.Settings(100, 3)
        settings_button_icon = pygame.image.load(f"{path}\\Icons\\cog.png")
        #shop_button_icon = pygame.image.load(f"{path}\\icons\\shop_button.png")
        run = 1
        while game.state == 5:
            settings_button = button.Button(screen, SCREEN_WIDTH/1.17 - 1325, SCREEN_HEIGHT/6-10, settings_button_icon, 1/(4.5))
            #shop_button = button.Button(screen, 500, 1000, shop_button_icon, 1)
            buttons = [settings_button] #, shop_button
            clicked = Play.CheckIfClicked(buttons, screen, game_settings, path)
            if run == 1:
                Play.Load(path, screen, save_data,SCREEN_WIDTH, SCREEN_HEIGHT)
            else:
                if clicked is True:
                    save_data = Play.CheckThreshold(save_data)
                    Play.Load(path, screen, save_data,SCREEN_WIDTH, SCREEN_HEIGHT)
                
            #Simulation code
            #check to see if next threshold has been met;
            #Play.CheckLevel()
            run = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
