import pygame, sys, csv
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
import math
 
from os.path import abspath
from inspect import getsourcefile

path = abspath(getsourcefile(lambda:0))[:-16] # obtains path of program
sys.path.append(f"{path}\\Icons")

def convertToTileCoords(coords):
    x = int(coords[0] // 9)
    y = int(coords[1] // 9)
    return [x, y]


class Train(pygame.sprite.Sprite):
    def __init__(self, ID, direction, line, customer_satisfaction, image_location, location, speed, station, empty_path):
        #ID of train
        #Northbound/Southbound/Eastbound/Westbound - NB, SB, EB, WB - or Clockwise/Anitclockwise (CW/ACW) for the cirlce line
        #e.g. District, Victoria, Northern etc
        #as a percentage
        #as in Matrix
        #speed of train
        #most recent station
        #most recent path of train
        #loads image

        super().__init__()
        # self.__type = type
        self.__ID = ID
        self.__direction = direction
        self.__vector_direction = pygame.math.Vector2(0,0)
        self.__image = pygame.image.load(image_location).convert_alpha()
        self.__rect = self.__image.get_rect(topleft = location)
        self.__location = [self.__rect.topleft[0], self.__rect.topleft[1]]
        self.__line = line
        self.__customerSatisfaction = customer_satisfaction
        self.__station = station
        self.__speed = speed
        self.__path = []
        self.__empty_path = empty_path
        self.__collisionRects = []

        self.image = pygame.image.load(image_location).convert_alpha()
        self.rect = self.image.get_rect(topleft = location)
    

    def setPath(self, path):
        self.__path = path
        self.createCollisionRects()
        self.get_direction()

    def delPath(self):
        self.__path = []

    def createCollisionRects(self):
        if self.__path:
            self.__collisionRects = []
            for point in self.__path:
                x = point[0] * 9 + 4.5
                y = point[1] * 9 + 4.5
                rect = pygame.Rect((x, y), (9, 9)) #before: x - 4.5, y - 4.5
                self.__collisionRects.append(rect)

    def get_direction(self):
        if self.__collisionRects:
            xy_1 = pygame.math.Vector2(self.__location)
            xy_2 = pygame.math.Vector2(self.__collisionRects[0].center)
            self.__vector_direction = (xy_2 - xy_1).normalize()
        else:
            # self.__vector_direction = pygame.math.Vector2(0,0)
            self.__path = []

    def update(self, next_station):
        self.__location += self.__vector_direction * self.__speed
        self.checkCollisions()
        self.__rect.center = (self.__location[0], self.__location[1])
        self.__station = next_station
        


    def checkCollisions(self):
        if self.__collisionRects:
            for rect in self.__collisionRects:
                if rect.collidepoint(self.__location):
                    del self.__collisionRects[0]
                    self.get_direction()
        else:
            self.delPath()

    #Getters
    def getLine(self):
        return self.__line
    
    def getDirection(self):
        return self.__direction
    
    def get_direction_vector(self):
        return self.__vector_direction

    def getLocation(self):
        return self.__location
    
    def GetStation(self):
        return self.__station

    def getPath(self):
        return self.__path


    def UpdateTrainLocation(self, surface, train_location):
        pass

    def CheckIfAtEndOfLine():
        #if at end of line, destroy
        pass

    def Clean(line):
        pass
    
    def Display(self, surface, ):
        surface.blit(self.__image, self.__location)


    #at Station
    def leaveStation():
        pass

    def openDoors():
        pass

    def shutDoors():
        pass





class Path():
    def __init__(self, matrix, train, path):
        # "train" is an object
        self.__matrix = matrix
        self.__grid = Grid(matrix = matrix)
        self.__path = []
        self.__empty_path = []
        self.__train = pygame.sprite.GroupSingle(train)
        # self.__select_surface = pygame.image.load(f"{path}\\Icons\\select.png").convert_alpha()


    def update(self, screen, validIDs):
        # self.drawSelector(screen, validIDs)
        self.__train.update(validIDs)
        self.__train.draw(screen)

    def getMatrix(self):
        return self.__matrix
    
    def getGrid(self):
        return self.__grid
    
    def getPath(self):
        return self.__path
    
    def getTrain(self):
        return self.__train.sprite

    def generate_path(self, next_station):
        temp = self.__train.sprite.getLocation()
        x_1, y_1 = (int(temp[0]//9)), (int(temp[1]//9))
        start = self.__grid.node(x_1, y_1)

        
        next_location = next_station.getLocation()
        # print("Station Name: ", next_station.getName(), "Station Location", next_station.getLocation())
        x_2, y_2 = int(int(next_location[0]) // 9), int(int(next_location[1]) // 9)
        print()
        print("Current location: ", self.__train.sprite.getLocation())
        print("end: ", x_2, y_2)
        print("next station: ", next_station.getName(), next_station.getLocation())
        end = self.__grid.node(x_2, y_2)

        find = AStarFinder(diagonal_movement = DiagonalMovement.always)
        self.__path,_ = find.find_path(start, end, self.__grid)
        self.__path = [*map(lambda  gridnode: (gridnode.x, gridnode.y), self.__path)]
        
        self.__grid.cleanup()
        self.__train.sprite.setPath(self.__path)

    def getCoords(self):
        column = self.__rect.topleftx // 9
        row = self.__rect.toplefty // 9
        return column, row
    

    def loadPath(self, screen):
        if self.__path:
            coords = []
            for point in self.__path:
                x = point.x * 9 + 4.5
                y = point.y * 9 + 4.5
                coords.append((x, y))
            pygame.draw.lines(screen, '#4a4a4a', False, coords, 5)

    def loadMatrix(level, path, validIDs, z = 0):
        level_matrix = []
        with open(f"{path}\\Maps\\{level}.csv") as file:
            data = csv.reader(file, delimiter=",")
            next(data)
            for row in data:
                level_matrix.append(row)

        if len(validIDs) > 0:
            temp_matrix = []
            for row in range(len(level_matrix)):
                temp_row = []
                for cell in range(len(level_matrix[row])):
                    if (level_matrix[row][cell] in validIDs[0]) or (level_matrix[row][cell] in validIDs[1]) and level_matrix[row][cell] != 9:
                        temp_row.append(1)
                    else:
                        temp_row.append(0)
                temp_matrix.append(temp_row)
            return temp_matrix
        return level_matrix
    
    def getMatrixCell(self, row, column):
        return self.__matrix[row][column]


class Station():
    def __init__(self, ID, name, location, line, status, no_customers, customer_satisfaction):
        # ID of station
        # name on Station
        # line station belong to
        # Open/Shut/Emergency
        # Number of customers at station
        # customer satisfaction for the station

        self.__ID = ID
        self.__name = name
        self.__location = location
        self.__line = line
        self.__status = status
        self.__customerNumber  = no_customers
        self.__customerSatisfaction = customer_satisfaction

    def getLocation(self):
        return self.__location
    
    def getName(self):
        return self.__name
    
    def Open():
        pass
    
    def Shut():
        pass