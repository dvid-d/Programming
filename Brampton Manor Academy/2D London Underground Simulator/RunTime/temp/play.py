import sys
from os.path import abspath
from inspect import getsourcefile
import pygame
from shop import *
from train import *
from tile import *
from game import *
from map import *
from settings import Settings
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
        map_data = load_pygame(f"{path}\\Maps\\{map}.tmx")
        sprite_group = pygame.sprite.Group()
        layers = map_data.visible_layers
        layers_group = []
        a  = 0
        for layer in layers:
            if layer not in map_data.objectgroups:
                for x,y,surface in layer.tiles():
                    pos = (x*9,y*9) # size of tiles
                    Tile(pos, surface, sprite_group)
                    if a  == 0:
                        coords_temp = pos
                        a += 1
            else:
                layers_group.append(layer)
        sprite_group.draw(screen)
        run = 0
        return run, save_data, layers_group, coords_temp
    
    def CheckForRewards():
        pass

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

    def CreateObjects(save_data, trains, trainID, stationsTiled):
        station_objects = Play.CreateStations(stationsTiled)
        trains, trainID = Play.CreateTrains(save_data, trains, trainID, station_objects)
        return trains, station_objects, trainID

    def CreateStations(layers):
            stations_objects = {"victoria": []}
            for layer in layers:
                line_objs = []
                if layer.name == "Victoria Line":
                    i = 0
                    default_station_obj = Station(ID = -1, name = "Default", location = (-1, -1), line = "N/A", no_customers = -1, customer_satisfaction = -1, status = "N/A")
                    line_objs.append(default_station_obj)
                    for station in layer:
                        id = station.id
                        location = [station.x, station.y] #tile, row
                        name = station.name
                        station_obj = Station(ID = id, name = name, location = location, line = layer.name, no_customers = 0, customer_satisfaction = 100, status = "open")
                        line_objs.append(station_obj)
                    stations_objects["victoria"] = line_objs
            return stations_objects
    
    def CreateTrains(save_data, trains, trainID, stations_objects): #creates Train Objects
        t, r, noTrainsCreated = 0, 0, 0 #to keep track of row & column and the order of lines for which "Train" objects are created
        level_matrix = Path.loadMatrix("level_1", path, [])
        if save_data["time"] == "00/00/0000":
            for counter in range(10): #loop 10x for all lines
                tempList = [] #trains for current line
                for row in level_matrix:
                    
                    for tile in row:
                        #Victoria line

                        # """d value follows the pattern below;
                        
                        # 0, 1 for trains
                        # 2 for appending to list
                        # """

                        if level_matrix[r][t] == "5":
                            print()
                        if noTrainsCreated < 2: #As long as both "Train" objects at either end of the Vict. line haven"t been fully created

                            if tile == "480":
                                validIDs = Train.getValidIDs(path = path, line = "victoria")
                                matrix = Path.loadMatrix("level_1", path, validIDs)
                                
                                # retrives station name, creates Train obj, appends to temporary list and increments trainID by 1
                                #validIDs to be changed for every line
                                station = stations_objects["victoria"][0] #default spawning point
                                train = Train(ID = trainID, direction = "NB", line = "victoria", customer_satisfaction = 100, image_location= f"{path}\\Icons\\victoria.png", location = (t * 9, r * 9), station = station, speed = 9, empty_path = [])
                                pathfinder = Path(matrix = matrix, train = train, path = [])
                                tempList.append([train, pathfinder, [t, r]])
                                trainID += 1
                                noTrainsCreated += 1
                                noTrainsCreated += 1 #temp
                                

                        elif noTrainsCreated == 2:
                            #adds the temp list to the "victoria" key
                            trains["victoria"] = tempList
                            noTrainsCreated += 1
                        t += 1
                    r += 1
                    t = 0
                r = 0
        return trains, trainID


    def MoveTrains(all_stations):
        for line in all_stations:
            stationIDs = all_stations[line]


    def Run(screen, path, save_data, SCREEN_WIDTH, SCREEN_HEIGHT, game):
        # game_settings = Settings.Settings(100, 3)

        map_data, layers, sprite_group = Map.LoadData(path, save_data)
        Map.Display(screen, sprite_group) 
        settings_button = Settings.loadButtons(path = path, surface = screen, SCREEN_WIDTH = SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_HEIGHT)
        buttons = [settings_button] #, shop_button etc #list of buttons to loop through and proceed with their individual actions if clicked
        trains = save_data["trainLocations"] #dictionary
        level_matrix = Path.loadMatrix("level_1", path, [])

        trainID = 0
        trains, stations_objects, trainID = Play.CreateObjects(save_data, trains, trainID, layers) #save_data, trains, level_matrix, trainID, stationsTiled)
        
        while game.state == 5:
            Settings.checkButtons(buttons, screen, path)
            Map.Display(screen, sprite_group)
            for button in buttons:
                button.display()
            
            # spawn trains periodically

            #to UPDATE validIDs with ID"s of other lines, starting with H&C
            for line in trains:
                if line == "victoria":        
                    for trainList in trains[line]:
                        train_path = trainList[1]
                        train = train_path.getTrain()

                        isAtEndOfLine = False
                        if train.getStation().getName() == "Default" or (convertToTileCoords(train.getStation().getLocation()) == convertToTileCoords(train.getLocation())):
                            next_station = train.findNextStation(stations_objects)
                            print("NEXT STATION: ", next_station.getName())
                            if type(next_station) == bool:
                                isAtEndOfLine = True
                            
                            if isAtEndOfLine:
                                # "Calculate stats, destroy train AND path obj"
                                pass
                            else:
                                train_path.generate_path(next_station)
                                # print(train_path.getPath())

                        train_path.update(screen)
                        print("This shit is pissing me off so much")
                        print(train.get_direction_vector())
                        # print(train.getPath())
                        # pygame.draw.circle(screen, (200, 200, 150), getCenterCoords(train.getLocation()) , 5)
                        print()
                        print()
                                #temp_path = []

                                #TO FIX TRAIN GOING THE WRONG WAY
                                # for coordinate_index in range(len(train_path.getPath()) - 1):
                                #     # if coordinate_index != (len(self.__path)):
                                #     delta_x_1 = path_list[coordinate_index][0] - train_path.getTrain().getLocation()[0]
                                #     delta_y_1 = path_list[coordinate_index][1] - train_path.getTrain().getLocation()[1]
                                #     distance_1 = math.sqrt((delta_x_1**2 + delta_y_1**2))

                                #     delta_x_2 = path_list[coordinate_index+1][0] - train_path.getTrain().getLocation()[0]
                                #     delta_y_2 = path_list[coordinate_index+1][1] - train_path.getTrain().getLocation()[1]
                                #     distance_2 = math.sqrt(((delta_x_2)**2 + (delta_y_2)**2))
                                    
                                #     # print("distance 1: ", distance_1, ", distance 2: ", distance_2)
                                #     if distance_2 > distance_1:
                                #         temp_path.append(path_list[coordinate_index])
                                #     else:
                                #         temp_path.append(path_list[coordinate_index + 1])
                                
                                # #TO FIX TRAIN NOT GOING THE RIGHT WAY VERTICALLY
                                # temp_path_2 = []
                                # for coordinate_index in range(len(train_path.getPath()) - 1):
                                #     x = temp_path[coordinate_index][0]
                                #     y = temp_path[coordinate_index][1]
                                #     tile = level_matrix[x][y]
                                #     print(tile, "BEFORE x: ", x)
                                #     # print(type(tile))
                                #     if tile == "9":
                                #         x -= 1
                                #     print("AFTER x", x)
                                #     temp_path_2.append([x, y])
                                # temp_path = temp_path_2
                                # train_path.setPath(temp_path)

                                # print(temp_path_2)

                                # if train.getPath() != []:
                                # train_sprite = train_path.getTrain()
                                # train_sprite.setPath(temp_path)
                            
                            # temp_coords = train.getLocation()
                            # coords =(temp_coords[0] + 4.5, temp_coords[1] + 4.5)

                            # train.display(screen)

                            # train_location = train.getLocation()

                            # print("Train path: ", train.getPath())
                            # print("Train direction: ", train.get_direction_vector())

                            # print("test 4")
                            # x = int(train_location[0] // 9)
                            # y = int(train_location[1] // 9)
                            # print("Tile: ", level_matrix[x][y])
                            # pygame.draw.circle(screen, (200,200,250), coords, 5)

                            #if at next station:
                            #   don"t move until some user input
                            # print(current_station.GetName(), next_station.GetName())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Settings.InGameSettings(screen, path)
                        Clicked = True                

                            
            #Simulation code
            #check to see if next threshold has been met;
            #Play.CheckLevel()
            pygame.display.update()