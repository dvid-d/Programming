import pygame, sys, csv
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
import math
 
from os.path import abspath
from inspect import getsourcefile
import json

path = abspath(getsourcefile(lambda:0))[:-16] # obtains path of program
sys.path.append(f"{path}\\Icons")

def convertToTileCoords(coords):
    x = int(int(coords[0]) // 9)
    y = int(int(coords[1]) // 9)
    return [x, y]

def convertToTuple(coords): #converts a list with two items to a tuple
    x = coords[0]
    y = coords[1]
    new_coords = (x, y)
    return new_coords

def getCenterCoords(coords):
    #assuming coods given are top left
    x = coords[0] + 4.5
    y = coords[1] + 4.5
    new_coords = (x, y)
    return new_coords


class Train(pygame.sprite.Sprite):
    def __init__(self, ID, direction, line, customer_satisfaction, image_location, location, speed, station, empty_path):
        #ID of train
        #Northbound/Southbound/Eastbound/Westbound - NB, SB, EB, WB - or Clockwise/Anitclockwise (CW/ACW) for the circle line
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
        self.__location = self.__rect.center
        self.__tile_location = [int(self.__rect.topleft[0] // 9), int(self.__rect.topleft[1] // 9)]

        self.__line = line
        self.__customerSatisfaction = customer_satisfaction
        self.__station = station
        self.__speed = speed
        self.__isAtStation = False
        self.__stop_time = False
        self.__capacity = 0

        self.__path = []
        self.__empty_path = empty_path
        self.__collisionRects = []

        self.image = pygame.image.load(image_location).convert_alpha()
        self.rect = self.image.get_rect(topleft = location)
    


    def display(self, surface):
        surface.blit(self.__image, self.__rect.topleft)

    def setPath(self, path):
        self.__path = path
        self.createCollisionRects()
        self.get_direction()

    def setStation(self, station):
        self.__station = station

    def setIsAtStation(self, isAtStation):
        self.__isAtStation = isAtStation
    
    def increaseStop_time(self, value):
        self.__stop_time += value

    def delPath(self):
        self.__path = []


    #pathing
    def createCollisionRects(self):
        if self.__path:
            self.__collisionRects = []
            for point in self.__path:
                x = point[0] * 9 + 4.5
                y = point[1] * 9 + 4.5
                rect = pygame.Rect((x-1, y-1), (2, 2)) #before: x - 4.5, y - 4.5
                self.__collisionRects.append(rect)
            # print(self.__path)
            # print(self.__collisionRects)

    def get_direction(self):
        if self.__collisionRects:
            xy_1 = pygame.math.Vector2(self.__location)
            xy_2 = pygame.math.Vector2(self.__collisionRects[0].center)
            # print(xy_1, xy_2)
            # print("Collision rect: ", xy_2, "Train: ", self.__location)
            self.__vector_direction = (xy_2 - xy_1).normalize()
        else:
            self.__vector_direction = pygame.math.Vector2(0,0)
            self.__path = []

    def update(self):
        self.__location += self.__vector_direction * self.__speed
        self.checkCollisions()
        self.__rect.center = self.__location

    def checkCollisions(self):
        if self.__collisionRects:
            for rect in self.__collisionRects:
                if rect.collidepoint(self.__location):
                    del self.__collisionRects[0]
                    self.get_direction()
        else:
            self.delPath()

    def setStation(self, station):
        self.__station = station

    def findNextStation(self, stations):
        #station IDs from east to west or south to north (or clockwise for circle line) by default
        current_station = self.getStation()
        if self.__direction == "SB" or self.__direction == "EB" or self.__direction == "ACW":
            a = stations[self.__line]
            b = []
            for i in reversed(range(len(a))):
                b.append(a[i])
            stations = b
        else:
            stations = stations[self.__line]

        next_station = ""
        if current_station.getName() == "Default":
            next_station = stations[1] #index 0 is the default station obj
            return next_station
        else:
            for i in range(1, len(stations) - 1):
                if stations[i].getName() == current_station.getName():
                    next_station = stations[i+1]
                    return next_station
            if next_station == "":
                isAtEndOfLine = True
                return isAtEndOfLine
            
    #Pathing Getters
    def getValidIDs(path, line):
        file_name = "IDs.json"

        with open(f"{path}\\Maps\\{file_name}", 'r') as IDs_file:
            IDs = json.load(IDs_file)
        validIDs = IDs[line]
        return validIDs

    def get_coords(self):
        x = self.__rect.centerx // 9
        y = self.__rect.centery // 9
        return (x, y)
    
    #Other Getters
    def getLine(self):
        return self.__line
    
    def getDirection(self):
        return self.__direction
    
    def get_direction_vector(self):
        return self.__vector_direction

    def getLocation(self):
        return self.__location
    
    def getStation(self):
        return self.__station

    def getPath(self):
        return self.__path

    def getID(self):
        return self.__ID

    def getIsAtStation(self):
        return self.__isAtStation

    def getStopTime(self):
        return self.__stop_time
        
    #Managing the train in-game
    def Clean(line):
        pass
    
    def wasLate(self):
        pass

    #at Station
    def leaveStation():
        pass

    def openDoors():
        pass

    def shutDoors():
        pass

    #at end of line
    def RemoveTrain(self, trains):
        #appends all trains which do not have the ID as the train being removed to a list
        #list is set as the new list with all train obj's for that line
        line = self.getLine()
        current_line_trains = trains[line]
        temporary = []
        for obj in current_line_trains:
            if obj[0].getID() != self.getID():
                temporary.append(obj)
        trains[line] = temporary

    def AddToStats(self, stats):
        stats.append(self)



class Path():
    def __init__(self, matrix, train, path):
        # "train" is an object
        self.__matrix = matrix
        self.__grid = Grid(matrix = matrix)
        self.__path = []
        self.__empty_path = []
        self.__train = pygame.sprite.GroupSingle(train)
        # self.__select_surface = pygame.image.load(f"{path}\\Icons\\select.png").convert_alpha()


    def update(self, surface):
        self.draw_path(surface)
        self.__train.update()
        self.__train.draw(surface)
        # print("test 101")

    def getMatrix(self):
        return self.__matrix
    
    def getTrain(self):
        return self.__train.sprite
    
    def getGrid(self):
        return self.__grid
    
    def getPath(self):
        return self.__path
    
    def getTrain(self):
        return self.__train.sprite

    def setPath(self, new_path):
        self.__path = new_path

        
    def generate_path(self, next_station):
        x_1, y_1 = self.__train.sprite.get_coords()
        start = self.__grid.node(x_1, y_1)

        
        next_location = next_station.getLocation()
        x_2, y_2 = int(next_location[0] // 9), int(next_location[1] // 9)
        end = self.__grid.node(x_2, y_2)

        find = AStarFinder(diagonal_movement = DiagonalMovement.always)
        self.__path,_ = find.find_path(start, end, self.__grid)
        self.__path = [*map(lambda  gridnode: (gridnode.x, gridnode.y), self.__path)]
        
        self.__grid.cleanup()
        self.getTrain().setStation(next_station)

        self.__train.sprite.setPath(self.__path)

    def getCoords(self):
        column = self.__rect.topleftx // 9
        row = self.__rect.toplefty // 9
        return column, row
    

    def draw_path(self, screen):
        if self.__path:
            coords = []
            for point in self.__path:
                x = point[0] * 9 + 4.5
                y = point[1] * 9 + 4.5
                coords.append((x, y))
            pygame.draw.lines(screen, '#ff80ff', False, coords, 5)

    def loadMatrix(level, path, validIDs):
        level_matrix = []
        with open(f"{path}\\Maps\\{level}.csv") as file:
            data = csv.reader(file, delimiter=",")
            # next(data)
            for row in data:
                level_matrix.append(row)

        if len(validIDs) > 0:
            temp_matrix = []
            for row in range(len(level_matrix)):
                temp_row = []
                for cell in range(len(level_matrix[row])):
                    if (level_matrix[row][cell] in validIDs["track_IDs"]) or (level_matrix[row][cell] in validIDs["station_IDs"]):
                        # print(level_matrix[row][cell])
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