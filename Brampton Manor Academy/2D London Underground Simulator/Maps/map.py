import sys
from os.path import abspath
from inspect import getsourcefile

import pygame
from shop import *
from tile import *
from pytmx.util_pygame import load_pygame


path = abspath(getsourcefile(lambda:0))[:-16]
sys.path.append(f"{path}\\Game Properties")
sys.path.append(f"{path}\\Fonts")
sys.path.append(f"{path}\\Maps")
sys.path.append(f"{path}\\RunTime")
sys.path.append(f"{path}\\Saves")
sys.path.append(f"{path}\\Trains")


class Map():
    def LoadData(path, save_data):
        map = Map.GetMap(save_data)
        map_data = load_pygame(f"{path}\\Maps\\{map}.tmx")
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
        return map_data, layers_group, sprite_group
    
    def Display(screen, sprite_group):
        sprite_group.draw(screen)
    
    def GetMap(save_data):
        if save_data["level"] == 1.0 or save_data["level"] == 0.0:
            map = "level_1"
        else:
            map = "level_" + str(int(save_data[3]))
        return map