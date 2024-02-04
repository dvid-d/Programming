import pygame, sys, csv
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
 
from os.path import abspath
from inspect import getsourcefile

path = abspath(getsourcefile(lambda:0))[:-16] # obtains path of program
sys.path.append(f"{path}\\Icons")

class Train(pygame.sprite.Sprite):
    def __init__(self, direction, line, customer_satisfaction, image_location, location, speed, station, empty_path):
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
        self.__direction = direction
        self.__image = pygame.image.load(image_location).convert_alpha()
        self.__rect = self.__image.get_rect(topleft = location)
        self.__location = self.__rect.topleft
        self.__line = line
        self.__customerSatisfaction = customer_satisfaction
        self.__station = station
        self.__speed = speed
        self.__path = []
        self.__empty_path = empty_path
        self.__collisionRects = []
    

    def DrawTrain(self, surface, location):
        surface.blit(self.__image, location)

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
                rect = pygame.Rect((x - 4.5, y - 4.5), (9, 9))
                self.__collisionRects.append(rect)

    def getDirection(self):
        if self.__collisionRects:
            xy_1 = pygame.math.Vector2(self.__location)
            xy_2 = pygame.math.Vector2(self.__collisionRects[0].center)
            self.__direction = (xy_2 - xy_1).normalize()
        else:
            self.__direction = pygame.math.Vector2(0,0)
            self.__path = []

    def update(self):
        self.__location += self.__direction * self.__speed
        self.checkCollisions()
        self.__rect.center = self.__location

    def checkCollisions(self):
        if self.__collisionRects:
            for rect in self.__collisionRects:
                if rect.collidepoint(self.__location):
                    del self.__collisionRects[0]
                    self.getDirection()
        else:
            self.delPath()


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
    

    def CheckIfAtEndOfLine():
        #if at end of line, destroy
        pass

    def Clean(line):
        pass
    
    def Display(self, surface, icon_location):
        icon = pygame.image.load(icon_location) #location: f"{path}\\Icons\\Player.png"
        surface.blit(icon, self.__location)

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
        self.__select_surface = pygame.image.load(f"{path}\\Icons\\select.png").convert_alpha()


    def update(self, screen, validIDs):
        self.drawSelector(screen, validIDs)
        self.__train.update()
        self.__train.draw(screen)

    def getMatrix(self):
        return self.__matrix
    
    def getGrid(self):
        return self.__grid
    
    def generate(self):
        x_1, y_1 = self.__train.sprite.getCoords()
        start = self.__grid.note(x_1, y_1)
        mouse = pygame.mouse.get_pos()
        x_2, y_2 = mouse[0] // 9, mouse[1] // 9
        end = self.__grid.note(x_2, y_2)
        find = AStarFinder(diagonal_movement = DiagonalMovement.always)
        self.__path = find.find_path(start, end, self.__grid)
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


    # def drawSelector(self, screen, validIDs):
    #     mouse = pygame.mouse.get_pos() #gets position of the mouse
    #     row = mouse[1] // 9
    #     column = mouse[0] // 9
    #     cell = self.getMatrixCell(row, column)
    #     if (cell in validIDs[0][1]) or (cell in validIDs[0][2]) or (cell in validIDs[0][2]):
    #         selector = pygame.Rect((column * 9, row * 9), (9, 9)) #location, (width, height)
    #         screen.blit(self.__select_surface, selector)
    
    def loadMatrix(level, path):
        level_matrix = []
        with open(f"{path}\\Maps\\{level}.csv") as file:
            data = csv.reader(file, delimiter=",")
            next(data)
            for row in data:
                level_matrix.append(row)
        return level_matrix
    
    def getMatrixCell(self, row, column):
        return self.__matrix[row][column]
    
    class Station():
        def __init__(self, ID, name, line):
            self.__ID = ID
            self.__name = name
            self.__line = line