import pygame, sys

sys.path.append("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Icons")

class Train():
    def __init__(self, surface, direction, line, type, customer_satisfaction, icon_location, train_location):
        self.__type = type # Player or Non-player
        self.__direction = direction #Northbound/Southbound/Eastbound/Westbound - NB, SB, EB, WB - or Clockwise/Anitclockwise (CW/ACW) for the cirlce line
        self.__line = line #e.g. District, Victoria, Northern etc
        self.__customerSatisfaction = customer_satisfaction #as a percentage
        self.__train_location = train_location #Represents top right hand corner of train.

        self.__image = pygame.image.load(icon_location) #location: f"{path}\\Icons\\Player.png"
        dimensions = self.__image.get_rect()
        hitbox = pygame.Rect(train_location[0], train_location[1], dimensions[2], dimensions[3])
        self.__hitbox = hitbox
        surface.blit(self.__image, self.__train_location)

    def GetLine(self):
        return self.__line
    
    def GetDirection(self):
        return self.__direction
    
    def GetLocation(self):
        return self.__train_location
    
    def L():
        pass

    def CheckForCollision(point_1, point_2, point_3, point_4):
        P1  = pygame.math.Vector2(*point_1)
        P2 = pygame.math.Vector2(*point_2)
        Line1Vector = P2 - P1
        Line1UnitVector = Line1Vector.normalize()

        P3  = pygame.math.Vector2(*point_3)
        P4 = pygame.math.Vector2(*point_4)
        Line2Vector = P4 - P3
        Line2UnitVector = Line2Vector.normalize()

        NormalLine1 = pygame.math.Vector2(Line1UnitVector[1], -Line1UnitVector[0])
        NormalLine2 = pygame.math.Vector2(Line2UnitVector[1], -Line2UnitVector[0])
        Line1UnitVectordotSVN = Line1UnitVector.dot(NormalLine2)
        if Line1UnitVectordotSVN == 0: #if dot product = 0, line and normal of other line are perpendicular
            return False
        
        DirectionVector3_4  = P3 - P1
        a = DirectionVector3_4.dot(NormalLine2) / Line1UnitVectordotSVN
        b = DirectionVector3_4.dot(NormalLine1) / Line1UnitVectordotSVN

        return a > 0 and b > 0 and a**2 < Line1Vector.magnitude_squared() and b**2 < Line2Vector.magnitude_squared()
    
    def CollideTrainTrack(train, point_1_track, point_2_track):
        return (Train.CheckForCollision(point_1_track, point_2_track, train.topleft, train.bottomleft) or
                Train.CheckForCollision(point_1_track, point_2_track, train.bottomleft, train.bottomright) or
                Train.CheckForCollision(point_1_track, point_2_track, train.bottomright, train.topright) or
                Train.CheckForCollision(point_1_track, point_2_track, train.topright, train.topleft))

    def CheckOnTrack(self, track_points, line):
        if line == len(track_points):
            if Train.CollideTrainTrack(self.__hitbox, track_points[line-1], track_points[0]):
                return True
        else:
            if Train.CollideTrainTrack(self.__hitbox, track_points[line-1], track_points[line]):
                return True
        return False


    def UpdateTrainLocation(self, surface, train_location):
        self.__train_location = train_location
        surface.blit(self.__image, train_location)
    
    def IsOnTrack(self, track_points):
        collisionList = []
        for i in range(1, len(track_points)+1):
            collisionList.append(self.CheckOnTrack(track_points, i))
        return collisionList

    def Move(): #, track_points
        pass
        
    def CheckIfAtEndOfLine():
        #if at end of line, destroy
        pass

    def Clean(lines):
        pass
    
    # def DisplayTrain(surface, icon_location, train_location):
    #     icon = pygame.image.load(icon_location) #location: f"{path}\\Icons\\Player.png"
    #     hitbox = icon.icon.get_rect()
    #     hitbox.center = train_location ##sort this out
    #     surface.blit(icon, hitbox)

class PlayerTrain(Train):
    def __init__(self, surface, direction, line, type, customer_satisfaction, icon_location, train_location):
        super().__init__(surface, direction, line, type, customer_satisfaction, icon_location, train_location)

    def Move(self, surface): #track_points
        MOVERIGHT, MOVELEFT, MOVEUP, MOVEDOWN = 0, 0, 0, 0
        keys = pygame.key.get_pressed()
        # if event.type == pygame.KEYDOWN:
        if keys[pygame.K_d]:
            MOVERIGHT = 1
        if keys[pygame.K_a]:
            MOVELEFT = -1
        if keys[pygame.K_w]:
            MOVEUP = -1
        if keys[pygame.K_s]:
            MOVEDOWN = 1
            
        # surface.blit(self.__image, self.__train_location)

        # collisionList = self.IstOnTrack(track_points)

        # for checkedSide in collisionList:
        #     if checkedSide:
        #         MOVEDOWN, MOVEUP, MOVERIGHT, MOVELEFT = 0, 0, 0, 0
        
        train_location = self.GetLocation()
        self.UpdateTrainLocation(surface, (train_location[0] + MOVERIGHT + MOVELEFT, train_location[1] + MOVEUP + MOVEDOWN))