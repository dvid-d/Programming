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

    def MoveTrains(all_stations):
        for line in all_stations:
            stationIDs = all_stations[line]

    def CreateTrains(layers, stations_objects, trains_to_make):
        trainID = 0

        validIDs = Train.getValidIDs(path = path, line = "victoria")
        victoria_matrix = Path.loadMatrix("level_1", path, validIDs)
        station = stations_objects["victoria"][0]

        victoria_temp = []
        if trains_to_make["victoria"]["SB"] is True:
            train = Train(ID = trainID, direction = "NB", line = "victoria", capacity = 864, customer_satisfaction = 100, image_location= f"{path}\\Icons\\victoria.png", location = (79* 9, 75 * 9), station = station, speed = 1, empty_path = [])
            pathfinder = Path(matrix = victoria_matrix, train = train, path = [])   
            victoria_temp.append([train, pathfinder])
            trainID += 1

        # if trains_to_make["victoria"]["NB"] is True:
        #     train_2 = Train(ID = trainID + 1, direction = "SB", line = "victoria", customer_satisfaction = 100, image_location= f"{path}\\Icons\\victoria.png", location = (125 * 9, 19 * 9), station = station, speed = 1, empty_path = [])
        #     pathfinder_2 = Path(matrix = victoria_matrix, train = train_2, path = [])   
        #     victoria_temp.append([train_2, pathfinder_2])
        #     trainID += 1

        trains = {"victoria": victoria_temp, "h&c" : []}
        return trains


    def Run(screen, path, save_data, SCREEN_WIDTH, SCREEN_HEIGHT, game):
        # game_settings = Settings.Settings(100, 3)
        frames = 30
        clock = pygame.time.Clock()

        map_data, layers, sprite_group = Map.LoadData(path, save_data)
        stats = save_data["Stats"]
        Map.Display(screen, sprite_group) 
        level_matrix = Path.loadMatrix("level_1", path, [])
        trainID = 0


        stations_objects = Play.CreateStations(layers)
        trains = save_data["trainLocations"]
        if save_data["time"] == "00/00/0000":
            #Northern line needs to be sorted out
            trains_to_make = {"victoria": {"NB": True, "SB" : True}, "h&c": {"WB": False, "EB" : False}, "circle": {"CW": False, "ACW": False}, "district":{"WB": False, "EB": True}, "jubilee": {"WB": False, "EB": False}, "metropolitan": {"WB": False, "EB": False}, "central": {"WB": False, "EB": False}, "picadilly": {"WB": False, "EB": False}, "northern": {"NB" : False, "SB": False}}
        else:
            trains_to_make = {"victoria": {"NB": False, "SB" : False}, "h&c": {}, "circle": {}, "district":{}, "jubilee": {}, "metropolitan": {}, "central": {}, "picadilly": {}, "northern": {}}

        trains = Play.CreateTrains(layers, stations_objects, trains_to_make)
        settings_button = Settings.loadButtons(path = path, surface = screen, SCREEN_WIDTH = SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_HEIGHT)
        buttons = [settings_button] #, shop_button etc #list of buttons to loop through and proceed with their individual actions if clicked
        
        while game.state == 5:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        isInSettings = True
                        Settings.InGameSettings(screen, path, isInSettings)
                    
            Map.Display(screen, sprite_group)
            for button in buttons:
                button.display()

            #generate random event at a randm time
            #generate line-specific event before FOR loop
            
            for line in trains:
                for group in trains[line]:
                    if len(group) > 0:
                        train = group[0]
                        pathfinder = group[1]
                        station = train.getStation()

                        if convertToTileCoords(train.getLocation()) == convertToTileCoords(station.getLocation()):
                            train.setIsAtStation(True)
                        
                        # if train.getIsAtStation():
                        #     train.increaseStop_time(1)
                        #     new_customers = 0 #no. getting on
                        #     leaving_customers = 0 #no. getting off

                        #     wasLate = station.wasLate(train.getID())

                        #if train.getTimeToComplete() != 0:
                            # stop_time = train.getStop_time()
                            # new_stop_time = stop_time + value
                            # if new_stop_time == train.get_time_to_complete():
                            #     train.setStop_time(0)
                            # else:
                            #     train.setStop_time(stop_time + value)

                        #generate train-related event here
                        if train.getStation().getName() == "Default" or len(train.getPath()) == 0:
                            next_station = train.findNextStation(stations_objects)
                            if type(next_station) == bool:
                                train.AddToStats(stats)
                                train.RemoveTrain(trains)
                            else:
                                pathfinder.generate_path(next_station)

                        if type(next_station) != bool:
                            pathfinder.update(screen)   
                            train.display(screen)
            clock.tick(frames)
            pygame.display.update()
