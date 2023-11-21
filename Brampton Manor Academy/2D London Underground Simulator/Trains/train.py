import pygame, controls

class Train():
    def __init__(self, direction, type, customer_satisfaction, icon_location, train_location, onTrack):
        self.type = type # #Automatic or user train
        self.direction = direction #Northbound/Southbound/Eastbound/Westbound
        self.customerSatisfaction = customer_satisfaction #on a scale
        self.icon = pygame.image.load(icon_location) #location: f"{path}\\Icons\\Player.png"
        rectangle = self.icon.get_rect()
        self.train_location = train_location #Represents top right hand corner of train.
        rectangle.center = [train_location[0]+50, train_location[1]-50] #change depending on southbound/northbounding intially or when loading| Should be a tuple
        self.OnTrack = onTrack

    def L():
        pass

    def CheckTrain_SideOfTrack(point_1, point_2, point_3, point_4):
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
    
    def CollideTrainTrack(train, point_1, point_2):
        return (Train.CheckTrain_SideOfTrack(point_1, point_2, train.topleft, train.bottomleft) or
                Train.CheckTrain_SideOfTrack(point_1, point_2, train.bottomleft, train.bottomright) or
                Train.CheckTrain_SideOfTrack(point_1, point_2, train.bottomright, train.topright) or
                Train.CheckTrain_SideOfTrack(point_1, point_2, train.topright, train.topleft))

    def NotOnTrack(self, track_points, line):
        if line == len(track_points):
            if Train.CollideTrainTrack(self.icon.get_rect(), track_points[line-1], track_points[0]):
                return True
        else:
            if Train.CollideTrainTrack(self.icon.get_rect(), track_points[line-1], track_points[line]):
                return True
        return False


    def UpdateTrainLocation(self, train_location):
        self.train_location = train_location

    def Move(self, screen, MoveLeft, MoveRight, MoveUp, MoveDown, track, icon_location):
        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_a:
        #             MoveLeft = True
        #         if event.key == pygame.K_d:
        #             MoveRight = True
        #     if event.type == pygame.KEYUP:
        #         if event.key == pygame.K_a:
        #             MoveLeft = False
        #         if event.key == pygame.K_d:
        #             MoveRight = False |||||Should be executed before calling Move()


        if (not Train.NotOnTrack(self, track, 2)) or (not Train.NotOnTrack(self, track, 3)):
            if MoveLeft:
                self.train_location[0] -= 3
        if not Train.NotOnTrack(self, track, 5):
            if MoveRight:
                self.train_location[0] += 3
        #need to:
        #           check which line the train is on (different for each line)
        #           check where train's bottom right hand corner is
        #           if corner within range (needs to be calculated for each line), check for keys, then allow player to move accordingly
        #           add should also add for other sides of line
        Train.DisplayTrain(self, screen, icon_location, self.train_location)

    def CheckIfAtEndOfLine():
        pass

    def Clean(lines):
        pass

    def Move(train):
        train.

    def DisplayTrain(screen, icon_location, train_location):
        icon = pygame.image.load(icon_location) #location: f"{path}\\Icons\\Player.png"
        hitbox = icon.icon.get_rect()
        hitbox.center = train_location
        screen.blit(icon, hitbox)