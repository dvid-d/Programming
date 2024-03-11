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
        trains[0].Move(screen)

    def CreateObjects(save_data, trains, level_matrix, trainID, stationsTiled):
        trains, trainID = Play.CreateTrains(save_data, trains, level_matrix, trainID)
        stations = Play.CreateStations(stationsTiled)
        return trains, stations, trainID

    def CreateTrains(save_data, trains, level_matrix, trainID): #creates Train Objects
        t, r, d = 0, 0, 0 #to keep track of row & column and the order of lines for which "Train" objects are created
        if save_data["time"] == "00/00/0000":
            for counter in range(10): #inner loop 10 times for all lines; easier to keep track of all "Train" objets before appending
                tempList = [] #to keep track of all trains set to initlaly be loaded in at the start of the map
                for row in level_matrix:
                    r += 1
                    for tile in row:
                        t += 1
                        #Victoria line
                        if d < 2: #As long as both "Train" objects at either end of the Vict. line haven't been created

                            #Victoria Line
                            if tile == '130':
                                if d == 0:
                                    # retrives station name, creates Train obj, appends to temporary list and increments trainID by 1
                                    station = "default" #default spawning point
                                    train = Train(ID = trainID, direction = "NB", line = "victoria", customer_satisfaction = 100, image_location= f"{path}\\Icons\\victoria.png", location = (t * 9, r * 9), station = station, speed = 1, empty_path = [])
                                    pathfinder = Path(matrix = level_matrix, train = train, path = path)
                                    tempList.append([train, pathfinder, [t, r]])
                                    trainID += 1
                                    d += 1
                                elif d == 1:
                                    station = "default" #default spawning point
                                    train = Train(ID = trainID, direction = "SB", line = "victoria", customer_satisfaction = 100, image_location = f"{path}\\Icons\\victoria.png", location = (t * 9, r * 9), station = station, empty_path = [], speed = 1)
                                    pathfinder = Path(matrix = level_matrix, train = train, path = path)
                                    tempList.append([train, pathfinder, [t, r]]) #number of passengers, train object, (row, column (i.e. tile along row))) 
                                    trainID += 1
                                    d += 1

                                    #adds the temp list to the 'victoria' key
                                    trains["victoria"] = tempList

                            #Hammersmith & City line
                            elif tile == 0:
                                if d == 2:
                                    pass
                                elif d == 3:
                                    #code
                                    trains["hammersmith & city"] = tempList
                            elif tile == 0:
                                trains["victoria"] = tempList
                                #southbound
                                #...

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
        print(dir(layers))
        stations_objects = [["Victoria Line", []]]
        for layer in layers:
            print("yes, and?")
            print(layer.name)
            if layer.name == "Victoria Line":
                i = 0
                for station in layer:
                    id = station.id
                    location = [station.x, station.y] #tile, row
                    name = station.name
                    station_obj = Station(ID = id, name = name, location = location, line = layer.name, no_customers = 0, customer_satisfaction = 100, status = "open")
                    stations_objects[i][1].append(station_obj)
        return stations_objects


    def MoveTrains(all_stations):
        for line in all_stations:
            stationIDs = all_stations[line]


    def Run(screen, path, save_data, SCREEN_WIDTH, SCREEN_HEIGHT, game):
        game_settings = settings.Settings(100, 3)

        trains = save_data["trainLocations"] #dictionary
        stations = save_data["stations"]
        level_matrix = Path.loadMatrix("level_1", path)

        trackIDs = ['0','50','60','70','80','90','100','110','140','150','160','170','180','190','200','210','220','230','240','250','260','270','320','340','350','360','370','380','390','400','410','367','377','397','398'] #Allowed IDs only; i.e. can only pass over these tiles
        stationIDs = ['130', '140','150','160','170','180','220','230','240','350']
        # startIDs = []
        validIDs = {"victoria": (stationIDs, trackIDs)} #[0] = line name, [1] = 1st 2 are starting IDs for trains, rest are station IDs, [2] = track ID's for line

        # # print(level_matrix)
        # print(len(level_matrix)) # number of rows
        # print(len(level_matrix[0])) #number of tiles per row

        run = 1
        trainID = 0
        run, save_data, layers = Play.LoadMap(path, save_data, screen, run)
        trains, stations_objects, trainID = Play.CreateObjects(save_data, trains, level_matrix, trainID, layers) #save_data, trains, level_matrix, trainID, stationsTiled)

        # run = 1 #used to check if it the first time the loop is run in order to not load the player in their default position more than once (which is when first loading the map)
        count = 0
        while game.state == 5:
            run, save_data, stations = Play.LoadMap(path, save_data, screen, run)
            settings_button = Play.LoadButtons(path, screen, SCREEN_WIDTH, SCREEN_HEIGHT)
            buttons = [settings_button] #, shop_button etc #list of buttons to loop through and proceed with their individual actions if clicked
            Play.CheckButtons(buttons, screen, game_settings, path)

            # if count % 40:
            #     Play.CreateTrains()
            #pathfinder.drawSelector(screen = screen, validIDs = validIDs)
            
                        # clicked = True
            # for train in trains:
            #     train.Move()

            #Display trains on screen
            for line in trains:
                for train in trains[line]:
                    train = train[0]
                    train.Display(screen)

            #to UPDATE validIDs with ID's of other lines, starting with H&C
            print(stations)
            for line in trains:
                if line == "victoria":
                    validIDs_temp = validIDs[line]
                    for trainList in trains[line]:
                        train_path = trainList[1]
                        if train.GetLine() == "victoria":
                            stations_temp = []
                            if train.GetDirection() == "NB":
                                print("aaaaaaaaaaa")
                                stations_temp = stations_objects[0][1]
                            else:
                                print("bbbbbbbbbb")
                                a = stations_objects[0][1]
                                b = []
                                for i in reversed(range(len(a))):
                                    b.append(a[i])
                                stations_temp = b
                                print("bye byeeee ", a)
                                print("awfqwrq", b)

                            current_station = train.GetStation()
                            next_station = ""

                            #finds index of current station
                            for i in range(len(stations_temp)):
                                print(current_station)
                                if stations_temp[i].GetName() == current_station:
                                    next_station = stations_temp[i+1]

                            #if index not found, next_station doesn't change so train must be on default starting tile
                            if next_station == "":
                                next_station = stations_temp[0]
                            print("Next station: ", next_station)
                            coords = next_station.GetLocation()
                            train_path.generate_path(next_station)
                            train_path.update(screen, validIDs)
                            
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
