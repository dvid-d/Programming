import pygame, sys, csv
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
 
sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Icons")

class Train():
    def __init__(self, direction, line, customer_satisfaction, image_location, coordinates, station):
        # Player or Non-player
        #Northbound/Southbound/Eastbound/Westbound - NB, SB, EB, WB - or Clockwise/Anitclockwise (CW/ACW) for the cirlce line
        #e.g. District, Victoria, Northern etc
        #as a percentage
        #as in Matrix
        #most recent station
        #loads image

        # self.__type = type
        self.__direction = direction
        self.__line = line
        self.__customerSatisfaction = customer_satisfaction
        self.__tileCoords = coordinates
        self.__station = station
        self.__image = pygame.image.load(image_location)

    def DrawTrain(self, surface, location):
        surface.blit(self.__image, location)

    def GetLine(self):
        return self.__line
    
    def GetDirection(self):
        return self.__direction
    
    def GetLocation(self):
        pass
    
    def L():
        pass

    def UpdateTrainLocation(self, surface, train_location):
        pass

    def Move(): #, track_points
        pass
        
    def CheckIfAtEndOfLine():
        #if at end of line, destroy
        pass

    def Clean(line):
        pass
    
    # def DisplayTrain(surface, icon_location, train_location):
    #     icon = pygame.image.load(icon_location) #location: f"{path}\\Icons\\Player.png"
    #     hitbox = icon.icon.get_rect()
    #     hitbox.center = train_location ##sort this out
    #     surface.blit(icon, hitbox)

class PlayerTrain(Train):
    pass

class Path():
    def __init__(self, matrix):
        self.__matrix = matrix
        self.__grid = Grid(matrix = matrix)
        self.select_surface = pygame.image.load("select.png").convert_alpha()

    def Update(self):
        self.DrawSelector()

    def GetMatrix(self):
        return self.__matrix
    
    def GetGrid(self):
        return self.__grid
    
    def DrawSelector(self):
        mouse = pygame.mouse.get_pos() #gets position of the mouse
        row = mouse[1] // 9
        column = mouse[0] // 9
        selector = pygame.Rect((column * 9, row * 9), (9, 9)) #location, (width, height)
    
    def LoadMatrix(level, path):
        level_matrix = []
        with open(f"{path}\\Maps\\{level}.csv") as file:
            data = csv.reader(file, delimiter=",")
            next(data)
            for row in data:
                level_matrix.append(row)
        return level_matrix