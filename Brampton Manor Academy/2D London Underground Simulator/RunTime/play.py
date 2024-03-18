import sys
from os.path import abspath
from inspect import getsourcefile
import pygame
from shop import *
from button import *
from train import *
from tile import *
from game import *
import settings
import math
from pytmx.util_pygame import load_pygame
path = abspath(getsourcefile(lambda:0))[:-16]
sys.path.append(f"{path}\\Game Properties")
sys.path.append(f"{path}\\Fonts")
sys.path.append(f"{path}\\Maps")
sys.path.append(f"{path}\\RunTime")
sys.path.append(f"{path}\\Saves")
sys.path.append(f"{path}\\Trains")

from train import Station

class Play():

    def LoadMap(path, save_data, screen, run):
        map = Play.GetMap(save_data)
        map_data = load_pygame(f'{path}\\Maps\\{map}.tmx')
        sprite_group = pygame.sprite.Group()
        layers = map_data.visible_layers
        layers_group = []
        for layer in layers:
            if layer not in map_data.objectgroups:
                for x,y,surface in layer.tiles():
                    pos = (x*9,y*9) # size of tiles
                    Tile(pos, surface, sprite_group)
            else:
                layers_group.append(layer)
        sprite_group.draw(screen)
        run = 0
        return run, save_data, layers_group


    def LoadEntities(path, screen, location):
        Play.CreatePlayer(path, screen, location)
        return 0 #to be changed to a list of all trains, grouped based on lines

    def LoadIcons(path):
        settings_button_icon = pygame.image.load(f"{path}\\Icons\\cog.png")
        shop_button_icon = pygame.image.load(f"{path}\\icons\\shop_button.png")
        return settings_button_icon, shop_button_icon

    def LoadButtons(path, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
        settings_button_icon, shop_button_icon = Play.LoadIcons(path)
        settings_button = Button(screen, SCREEN_WIDTH/1.17 - 1325, SCREEN_HEIGHT/6-10, settings_button_icon, 1/(4.5)) #creates settings button
        #shop_button = button.Button(screen, 500, 1000, shop_button_icon, 1) #creates shop button
        return settings_button#, shop_button
    
    def CheckForRewards():
        pass

    def GetMap(save_data):
        if save_data["level"] == 1.0 or save_data["level"] == 0.0:
            map = "level_1"
        else:
            map = "level_" + str(int(save_data[3]))
    #     elif save_data[3] == 2.0:
    #         map = "level_2"
    #     elif save_data[3] == 3.0:
    #         map = "level_3"
    #     elif save_data[3] == 4.0:
    #         map = "level_4"
    #     elif save_data[3] == 5.0:
    #         map = "level_5"
    #     elif save_data[3] == 6.0:
    #         map = "level_6"
    #     elif save_data[3] == 7.0:
    #         map = "level_7"
    #     elif save_data[3] == 8.0:
    #         map = "level_8"
    #     elif save_data[3] == 9.0:
    #         map = "level_9"
    #     elif save_data[3] == 10.0:
    #         map = "level_10"
        return map

    def CheckButtons(buttons, screen, game_settings, path):
            if buttons[0].wasClicked():
                game_settings.InGameSettings(screen, game_settings, path)
            # if buttons[1].wasClicked():
            #     shop.Shop.UseShop()
            #     return True
        
    def CheckThreshold(save_data): #change, save_data variable has been changed as saves are now json files
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

    def LoadIcons(path):
        settings_button_icon = pygame.image.load(f"{path}\\Icons\\cog.png")
        shop_button_icon = pygame.image.load(f"{path}\\icons\\shop_button.png")
        return settings_button_icon, shop_button_icon

    def LoadButtons(path, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
        settings_button_icon, shop_button_icon = Play.LoadIcons(path)
        settings_button = Button(screen, SCREEN_WIDTH/20 - 70, SCREEN_HEIGHT/20 - 30, settings_button_icon, 1/(4.5)) #creates settings button
        #shop_button = button.Button(screen, 500, 1000, shop_button_icon, 1) #creates shop button
        return settings_button#, shop_button

    def Tutorial(screen, trains):
        pass

    def CreateObjects(save_data, trains, trainID, stationsTiled, validIDs):
        stations_objects = Play.CreateStations(stationsTiled)
        trains, trainID = Play.CreateTrains(save_data, trains, trainID, stations_objects, validIDs)
        # print(stations_objects[0][0])
        return trains, stations_objects, trainID

    def CreateTrains(save_data, trains, trainID, stations_objects, validIDs): #creates Train Objects
        t, r, d = 0, 0, 0 #to keep track of row & column and the order of lines for which "Train" objects are created
        level_matrix = Path.loadMatrix("level_1", path, [])
        # print(level_matrix)
        # print(len(level_matrix[0]))
        #about 26537 tiles
        # for row in level_matrix:
        #     # print(row)
        #     for tile in row:
        #         if tile == '130':
        #             print(row)
        #             print(tile == '130')
        if save_data["time"] == "00/00/0000":
            for counter in range(10): #inner loop 10 times for all lines; easier to keep track of all "Train" objets before appending
                tempList = [] #to keep track of all trains set to initlaly be loaded in at the start of the map
                for row in level_matrix:
                    r += 1
                    for tile in row:
                        t += 1
                        #Victoria line

                        """d value follows the pattern below;
                        
                        0, 1 for trains
                        2 for appending to list
                        """
                        if d < 2: #As long as both "Train" objects at either end of the Vict. line haven't been fully created
                            # if tile == '130':
                            #     print("is the problem here question mark")
                            #     print("nvm it does but it's just slow for some reason")
                            #     print(tile)
                            
                            
                            # if tile == '130':
                            # validIDs_temp = validIDs["victoria"]
                            # matrix = Path.loadMatrix("level_1", path, validIDs_temp)
                            #     station = stations_objects[0][1][-1] #default spawning point
                            #     train = Train(ID = trainID, direction = "SB", line = "victoria", customer_satisfaction = 100, image_location = f"{path}\\Icons\\victoria.png", location = (t * 9, r * 9), station = station, empty_path = [], speed = 1)
                            #     pathfinder = Path(matrix = matrix, train = train, path = [])
                            #     tempList.append([train, pathfinder, [t, r]]) #number of passengers, train object, (row, column (i.e. tile along row))) 
                            #     trainID += 1
                            #     d += 1

                            if tile == '480':
                                validIDs_temp = validIDs["victoria"]
                                matrix = Path.loadMatrix("level_1", path, validIDs_temp)
                                
                                # retrives station name, creates Train obj, appends to temporary list and increments trainID by 1
                                #validIDs to be changed for every line
                                station = stations_objects[0][1][0] #default spawning point
                                print(station)
                                train = Train(ID = trainID, direction = "NB", line = "victoria", customer_satisfaction = 100, image_location= f"{path}\\Icons\\victoria.png", location = (t * 9, r * 9), station = station, speed = 9, empty_path = [])
                                print(t*9, r*9)
                                pathfinder = Path(matrix = matrix, train = train, path = [])
                                tempList.append([train, pathfinder, [t, r]])
                                trainID += 1
                                d += 1
                                d += 1 #temp
                                

                        elif d == 2:
                            #adds the temp list to the 'victoria' key
                            trains["victoria"] = tempList
                            print("help")
                            d += 1

                        # #Hammersmith & City line
                        # elif d < 5:
                        #     if d == 2:
                        #         pass
                        #     elif d == 3:
                        #         pass
                        # elif d == 4:
                        #     trains["hammersmith & city"] = tempList
                        # elif tile == 0:
                        #     trains["victoria"] = tempList
                        #     #southbound
                        #     #...

                        # elif line[0] == "circle":
                        #     pass
                        # elif line[0] == "district":
                        #     pass
                        # elif line[0] == "jubilee":
                        #     pass
                        # elif line[0] == "metropolitan":
                        #     pass
                        # elif line[0] == "central":
                        #     pass
                        # elif line[0] == "picadilly":
                        #     pass
                        # elif line[0] == "northern":
                        #     pass
                        else:
                            pass
                    t = 0
                r = 0
                #print(stationsCoords)
        return trains, trainID
    
    def CreateStations(layers):
        # print(dir(layers))
        stations_objects = [["victoria", []]]
        for layer in layers:
            # print(layer.name)
            if layer.name == "Victoria Line":
                i = 0
                for station in layer:
                    id = station.id
                    location = [station.x, station.y] #tile, row
                    name = station.name
                    station_obj = Station(ID = id, name = name, location = location, line = layer.name, no_customers = 0, customer_satisfaction = 100, status = "open")
                    stations_objects[i][1].append(station_obj)
                    print(name)
        return stations_objects


    def MoveTrains(all_stations):
        for line in all_stations:
            stationIDs = all_stations[line]


    def Run(screen, path, save_data, SCREEN_WIDTH, SCREEN_HEIGHT, game):
        game_settings = settings.Settings(100, 3)

        trains = save_data["trainLocations"] #dictionary
        stations = save_data["stations"]
        # level_matrix = Path.loadMatrix("level_1", path, [])

        trackIDs = ['0','50','60','70','80','90','100','110','140','150','160','170','180','190','200','210','220','230','240','250','260','270','320','340','350','360','370','380','390','400','410','367','377','397','398', '480'] #Allowed IDs only; i.e. can only pass over these tiles
        stationIDs = ['130', '140','150','160','170','180','220','230','240','350']
        # startIDs = []
        validIDs = {"victoria": (stationIDs, trackIDs)} #[0] = line name, [1] = 1st 2 are starting IDs for trains, rest are station IDs, [2] = track ID's for line

        # # print(level_matrix)
        # print(len(level_matrix)) # number of rows
        # print(len(level_matrix[0])) #number of tiles per row

        run = 1
        trainID = 0
        run, save_data, layers = Play.LoadMap(path, save_data, screen, run)
        trains, stations_objects, trainID = Play.CreateObjects(save_data, trains, trainID, layers, validIDs) #save_data, trains, level_matrix, trainID, stationsTiled)

        # run = 1 #used to check if it the first time the loop is run in order to not load the player in their default position more than once (which is when first loading the map)
        count = 0
        constant = 0
        while game.state == 5:
            run, save_data, stations = Play.LoadMap(path, save_data, screen, run)
            settings_button = Play.LoadButtons(path, screen, SCREEN_WIDTH, SCREEN_HEIGHT)
            buttons = [settings_button] #, shop_button etc #list of buttons to loop through and proceed with their individual actions if clicked
            Play.CheckButtons(buttons, screen, game_settings, path)

            # if count % 40:
            #     Play.CreateTrains()
            #pathfinder.drawSelector(screen = screen, validIDs = validIDs)
            
                        # clicked = True

            #Display trains on screen
            for line in trains:
                for train in trains[line]:
                    train = train[0]
                    train.Display(screen)

            #to UPDATE validIDs with ID's of other lines, starting with H&C
            # print(stations_objects[0][1][0].GetName())
            for line in trains:
                if line == "victoria":        
                    for trainList in trains[line]:
                        train_path = trainList[1]
                        if train.getLine() == "victoria":
                            stations_temp = []
                            # print("Line: ", train.GetDirection())
                            if train.getDirection() == "NB":
                                stations_temp = stations_objects[0][1]
                            else:
                                a = stations_objects[0][1]
                                b = []
                                for i in reversed(range(len(a))):
                                    b.append(a[i])
                                stations_temp = b
                            current_station = train.GetStation()
                            next_station = ""
                            #finds index of current station
                            # for i in range(len(stations_temp)):
                            # try:
                            i = 0
                            o = 0
                            for i in range(len(stations_temp)):
                                print(i, train.getDirection() ,stations_temp[i].getName(), current_station.getName())
                                if (stations_temp[i].getName() == current_station.getName()) and train.getPath() == []:
                                    # print(i)
                                    next_station = stations_temp[i+1] #index error when at the last station
                                    
                                    print(o)
                                    o += 1
                                    break
                            # except:
                            #     print("Train has reached the end of the line", i)
                            #     print(stations_temp[i].getName())
                            #     print(current_station.getName())
                            #     # print(current_station.getName())
                            #     # exit()
                            #     #save data into a list of trains that have reached the end of their lines, sorted by line
                            #     #list will be used to determine if user has successfully completed the level.
                                

                            #if index not found, next_station doesn't change so train must be on default starting tile
                            if next_station == "":
                                next_station = stations_temp[0]
                            
                            temp_coords = next_station.getLocation()
                            coords =(temp_coords[0] + 4.5, temp_coords[1] + 4.5)
                            
                            # train_path.generate_path(next_station)
                            # if convertToTileCoords(train.getLocation()) != convertToTileCoords(next_station.getLocation()):
                            if train.getPath() == []:
                                train_path.generate_path(next_station)
                                print(train.get_direction_vector())

                                temp_path = []
                                # print(len(train_path.getPath()))
                                path_list = train_path.getPath()

                                """
                                train goes off screen to the right after going past a few stations
                                
                                train is not displayed appropriately for horizontal stretches of the line
                                however, it is shown as intended when on diagonal parts
                                """

                                
                                for coordinate_index in range(len(train_path.getPath()) - 1):
                                    # if coordinate_index != (len(self.__path)):
                                    delta_x_1 = path_list[coordinate_index][0] - train_path.getTrain().getLocation()[0]
                                    delta_y_1 = path_list[coordinate_index][1] - train_path.getTrain().getLocation()[1]
                                    distance_1 = math.sqrt((delta_x_1**2 + delta_y_1**2))

                                    delta_x_2 = path_list[coordinate_index+1][0] - train_path.getTrain().getLocation()[0]
                                    delta_y_2 = path_list[coordinate_index+1][1] - train_path.getTrain().getLocation()[1]
                                    distance_2 = math.sqrt(((delta_x_2)**2 + (delta_y_2)**2))
                                    
                                    # print("distance 1: ", distance_1, ", distance 2: ", distance_2)
                                    if distance_2 > distance_1:
                                        temp_path.append(path_list[coordinate_index])
                                    else:
                                        temp_path.append(path_list[coordinate_index + 1])
                                # print(temp_path)


                                train_sprite = train_path.getTrain()
                                train_sprite.setPath(temp_path)
                                    
                            train_path.update(screen, next_station)
                            pygame.draw.circle(screen, (200,200,250), coords, 5)

                            #if at next station:
                            #   don't move until some user input
                            # print(current_station.GetName(), next_station.GetName())
                            




                            
            #Simulation code
            #check to see if next threshold has been met;
            #Play.CheckLevel()
            #Check to see if any train has met the end of their line
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_settings.InGameSettings(screen, game_settings, path)
            count += 1
            pygame.display.update()