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


class Play():

    def LoadMap(path, save_data, screen):
        map = Play.GetMap(save_data)
        map_data = load_pygame(f'{path}\\Maps\\{map}.tmx')
        sprite_group = pygame.sprite.Group()
        layers = map_data.visible_layers
        for layer in layers:
            for x,y,surface in layer.tiles():
                pos = (x*9,y*9) # size of tiles
                Tile(pos, surface, sprite_group)
        #Tile.test()
        #for object in map_data.visible_object_groups():
            #print(object)
        sprite_group.draw(screen)
        return map_data

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
    
    # def LoadTrains(path, screen, lines):
    #     #lines[Line][Train]
    #     #lines[Line][Train][NewCoords]
    #     for line in lines:
    #         trains = line[1]
    #         icon_location = f"{path}\\Icons\\{line}.png"
    #         for obj in trains:
    #             train_location = trains[obj]
    #             Train.Display(screen, icon_location, train_location)

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

    def CreateObjects(save_data, stations, trains, level_matrix): #creates Train Objects
        t, r, trainID = 0, 0, 0 #to keep track of row & column and the order of lines for which "Train" objects are created
        if save_data["time"] == "00/00/0000":
            for counter in range(10): #does inner loop 10 times for all 10 lines. it's easier to keep track of all "Train" objets before appending each group to its corresponding line.
                tempList = [] #to keep track of all trains set to initlaly be loaded in at the start of the map
                stationsCoords = [] #create station object and add to stations list
                for row in level_matrix:
                    r += 1
                    for tile in row:
                        t += 1

                        #Victoria line
                        if trainID < 2: #As long as both "Train" objects at either end of the Vict. line haven't been created
                            #stations
                            if tile in ['140','150','160','170','180','220','230','240','350']: #station tiles
                                stationsCoords.append((t, r))

                            #train
                            if trainID == 0 and tile == '130':
                                # retrives station name, creates Train obj, appends to temporary list and increments trainID by 1
                                print("(NB) Tile number is: " + tile)
                                station = stations["victoria line"] #default spawning point
                                train = Train(ID = trainID, direction = "NB", line = "victoria", customer_satisfaction = 100, image_location= f"{path}\\Icons\\victoria.png", location = (t * 9, r * 9), station = station, speed = 1, empty_path = [])
                                pathfinder = Path(matrix = level_matrix, train = train, path = path)
                                tempList.append([train, pathfinder, [t, r]])
                                trainID += 1
                            elif trainID == 1 and tile == '130':
                                print("(SB) Tile number is: " + tile)
                                station = stations["victoria line"] #default spawning point
                                train = Train(ID = trainID, direction = "SB", line = "victoria", customer_satisfaction = 100, image_location = f"{path}\\Icons\\victoria.png", location = (t * 9, r * 9), station = station, empty_path = [], speed = 1)
                                pathfinder = Path(matrix = level_matrix, train = train, path = path)
                                tempList.append([train, pathfinder, [t, r]]) #number of passengers, train object, (row, column (i.e. tile along row))) 
                                trainID += 1

                                #adds the temp list to the 'victoria' key, increments trainID by 1 as vic line doesn't need more trains at the start (1 for NB, 1 for SB)
                                trains["victoria"] = tempList
                                trainID += 1

                        #Hammersmith & City line
                        elif trainID < 4:
                            pass
                        elif trainID == 4:
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
                    t = 0
                r = 0
                print(stationsCoords)
        print(trains)
        return trains
    
    def CreateStations():
        pass
    def MoveTrains(all_stations):
        for line in all_stations:
            stationIDs = all_stations[line]


    def Run(screen, path, save_data, SCREEN_WIDTH, SCREEN_HEIGHT, game):
        game_settings = settings.Settings(100, 3)

        trains = save_data["trainLocations"] #dictionary
        stations = save_data["stations"]
        level_matrix = Path.loadMatrix("level_1", path)

        trackIDs = ['0','50','60','70','80','90','100','110','140','150','160','170','180','190','200','210','220','230','240','250','260','270','320','340','350','360','370','380','390','400','410','367','377','397','398'] #Allowed IDs only; i.e. can only pass over these tiles
        stationIDs = ['140','150','160','170','180','220','230','240','350']
        startIDs = ['120', '130']
        validIDs = [["victoria", startIDs, trackIDs, stationIDs]] #[0] = line name, [1] = starting IDs for trains on a specific line, [2] = track ID's for line, [2] = station ID's for line

        # # print(level_matrix)
        # print(len(level_matrix)) # number of rows
        # print(len(level_matrix[0])) #number of tiles per row

        trains = Play.CreateObjects(save_data, stations, trains, level_matrix)
        # print(trains)

        # run = 1 #used to check if it the first time the loop is run in order to not load the player in their default position more than once (which is when first loading the map)
        count = 0
        while game.state == 5:
            # run = 0
            Play.LoadMap(path, save_data, screen)
            settings_button = Play.LoadButtons(path, screen, SCREEN_WIDTH, SCREEN_HEIGHT)
            buttons = [settings_button] #, shop_button etc #list of buttons to loop through and proceed with their individual actions if clicked
            Play.CheckButtons(buttons, screen, game_settings, path)
            # if count % 40:
            #     Play.CreateTrains()
            #pathfinder.drawSelector(screen = screen, validIDs = validIDs)
            
                        # clicked = True
            # for train in trains:
            #     train.Move()

            for line in trains:
                for trainList in trains[line]:
                    train = trainList[1]
                    train.Display(screen, f"{path}\\Icons\\{line}.png")
                                        
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
