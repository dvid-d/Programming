import sys
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Game Properties")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Fonts")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Maps")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\RunTime")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Saves")
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Trains")
PLAYER = 0
import pygame
from shop import *
from button import *
from train import *
from tile import *
from game import *
import settings
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
            if object.type[:5] == "Track":
                track = object
                direction = track.type[5:7]

        
        #trains.append(player)
        #also add Trains and other things
        return 0

    def LoadMap(path, save_data, screen):
        map = Play.GetMap(save_data)
        map_data = load_pygame(f'{path}\\Maps\\{map}.tmx')
        sprite_group = pygame.sprite.Group()
        layers = map_data.visible_layers
        for layer in layers:
            for x,y,surface in layer.tiles():
                pos = (x*9,y*9) # size of tiles
                Tile(pos, surface, sprite_group)
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
                Train.Display(screen, icon_location, train_location)

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

    def CreatePlayer(path, screen, location):
        image_location = f"{path}\\Icons\\train.png"
        player = PlayerTrain(screen, "NB", "Victoria", "Player", 100, image_location, location) 
        return player


    def LoadEntities(path, screen, location):
        Play.CreatePlayer(path, screen, location)
        return 0 #to be changed to a list of all trains, grouped based on lines


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
        trains[PLAYER].Move(screen)

    
    def Run(screen, path, save_data, SCREEN_WIDTH, SCREEN_HEIGHT, game):
        game_settings = settings.Settings(100, 3)        
        trains = []

        run = 1 #used to check if it the first time the loop is run in order to not load the player in their default position more than once (which is when first loading the map)
        while game.state == 5:
            stations = Play.Load(path, screen, save_data, SCREEN_WIDTH, SCREEN_HEIGHT, run)
            run = 0

            settings_button = Play.LoadButtons(path, screen, SCREEN_WIDTH, SCREEN_HEIGHT)
            buttons = [settings_button] #, shop_button etc #list of buttons to loop through and proceed with their individual actions if clicked
            Play.CheckButtons(buttons, screen, game_settings, path)

                        # clicked = True
            # for train in trains:
            #     for track in tracks:
            #         if tracks[track][0][:3] == train.GetLine() and tracks[track][1] == train.GetDirection():
            #             track_points = tracks[track][2]
            #if int(save_data["level"]) == 0 or int(save_data["level"]) == 1:
                #trains[PLAYER].Move(screen) #track_points

            # for train in trains:
            #     train.Move()
                                        
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
            pygame.display.update()
