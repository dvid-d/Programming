import sys
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Game Properties")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Fonts")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Maps")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\RunTime")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Saves")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Trains")

import pygame, settings, main, button, gameState, tile, shop, train
from pytmx.util_pygame import load_pygame

class Play():
    def Load(path, screen, save_data, SCREEN_WIDTH, SCREEN_HEIGHT, run):
        map_data = Play.LoadMap(path, save_data, screen)
        objects = map_data.objects

        tracks = []
        lines = ["Vic", "H&C", "Cir", "Dis", "Jub", "Met", "Cen", "Pic", "Nor"]
        stations = [["Vic",[],[]], ["H&C",[],[]], ["Cir",[],[]], ["Dis",[],[]], ["Jub",[],[]], ["Met",[],[]], ["Cen",[],[]], ["Pic",[],[]], ["Nor",[],[]]]
        
        # track_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        for object in objects:
            print()
            if object.type[:5] == "Track":
                track = object
                direction = track.type[5:7]
                points = [(point.x, point.y) for point in track.points]  #points go clockwise from the bottom right
                pygame.draw.polygon(screen, (100,100,100), points, 1)
                if direction == "SB":
                    tracks.append([track.type[-3:], "SB", points])
                elif direction == "NB":
                    tracks.append([track.type[-3:], "NB", points])
                print()

            if object.type[:7] == "Station":
                station = object
                direction = station.type[7:9]
                pygame.draw.polygon(screen, (100,100,100), station.points, 1)
                
                for i in range(len(lines)):
                    if lines[i] == station.type[-3:]:
                        stations = Play.AddStationsToList(stations, direction, i, station) #must line up with order of stations in trainLocations in save file
        trains = [] #temp
        if run == 1:
            location = (650,1000)                      
            player = Play.CreatePlayer(path, screen, location)
            return player, trains #, track_surface
        #also add Trains and other things
        else:
            return trains #, track_surface

    def AddStationsToList(stations, direction, line_no, station):
        if direction == "NB":
            stations[line_no][1].append(station.points)
        elif direction == "SB":
            stations[line_no][2].append(station.points)
        return stations

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
        sprite_group.draw(screen)
        return map_data
    
    def LoadTrains(path, screen, lines):
        #lines[Line][Train]
        #lines[Line][Train][NewCoords]
        for line in lines:
            trains = line[1]
            icon_location = f"{path}\\Icons\\{line}.png"
            for obj in trains:
                train_location = trains[obj]
                train.Train.Display(screen, icon_location, train_location)

    def CheckForRewards():
        pass

    def GetMap(save_data):
        if save_data["level"] == 1.0 or save_data["level"] == 0.0:
            map = "level_1"
        else:
            map = "level_" + str(int(save_data[3]))
        # elif save_data[3] == 2.0:
        #     map = "level_2"
        # elif save_data[3] == 3.0:
        #     map = "level_3"
        # elif save_data[3] == 4.0:
        #     map = "level_4"
        # elif save_data[3] == 5.0:
        #     map = "level_5"
        # elif save_data[3] == 6.0:
        #     map = "level_6"
        # elif save_data[3] == 7.0:
        #     map = "level_7"
        # elif save_data[3] == 8.0:
        #     map = "level_8"
        # elif save_data[3] == 9.0:
        #     map = "level_9"
        # elif save_data[3] == 10.0:
        #     map = "level_10"
        return map

    def CheckIfClicked(buttons, screen, game_settings, path):
            if buttons[0].wasClicked():
                game_settings.InGameSettings(screen, game_settings, path)
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

    def CreatePlayer(path, screen, location):
        image_location = f"{path}\\Icons\\train.png"
        player = train.PlayerTrain(screen, "NB", "Victoria", "Player", 100, image_location, location) 
        return player

    def LoadEntities(path, screen, location):
        Play.CreatePlayer(path, screen, location)
        return 0 #to be changed to a list of all trains, grouped based on lines

    def Run(screen, path, save_data, SCREEN_WIDTH, SCREEN_HEIGHT, game):
        game_settings = settings.Settings(100, 3)
        settings_button_icon = pygame.image.load(f"{path}\\Icons\\cog.png")
        #shop_button_icon = pygame.image.load(f"{path}\\icons\\shop_button.png")

        run = 1 #used to check if it the first time the loop is run in order to not load the player in their default position more than once (which is when first loading the map)
        while game.state == 5:
            #shop_button = button.Button(screen, 500, 1000, shop_button_icon, 1) #creates shop button
            if run == 1:
                player, trains = Play.Load(path, screen, save_data, SCREEN_WIDTH, SCREEN_HEIGHT, run)
                run = 0
            else:
                trains = Play.Load(path, screen, save_data, SCREEN_WIDTH, SCREEN_HEIGHT, run)
            settings_button = button.Button(screen, SCREEN_WIDTH/1.17 - 1325, SCREEN_HEIGHT/6-10, settings_button_icon, 1/(4.5)) #creates settings button
            buttons = [settings_button] #, shop_button etc #list of buttons to loop through and proceed with their individual actions if clicked
            Play.CheckIfClicked(buttons, screen, game_settings, path)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_settings.InGameSettings(screen, game_settings, path)
                        clicked = True
            player.Move(screen)

            # for train in trains:
            #     train.Move()
                                        
            #Simulation code
            #check to see if next threshold has been met;
            #Play.CheckLevel()
            #Check to see if any train has met the end of their line
            pygame.display.update()
