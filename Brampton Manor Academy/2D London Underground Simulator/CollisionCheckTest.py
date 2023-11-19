import pygame
pygame.init()
screen = pygame.display.set_mode((1000,700))
screen.fill("white")
running = True

MoveLeft = False
MoveRight = False
MoveUp = False
MoveDown = False

img = pygame.image.load("C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Icons\\Train.png")
rect = img.get_rect()
rect.center = (500,400)


clock = pygame.time.Clock()

def collideLineLine(point_1, point_2, point_3, point_4):

    P  = pygame.math.Vector2(*point_1)
    line1_vec = pygame.math.Vector2(*point_2) - P
    R = line1_vec.normalize()
    Q  = pygame.math.Vector2(*point_3)
    line2_vec = pygame.math.Vector2(*point_4) - Q
    S = line2_vec.normalize()

    RNV = pygame.math.Vector2(R[1], -R[0])
    SNV = pygame.math.Vector2(S[1], -S[0])
    RdotSVN = R.dot(SNV)
    if RdotSVN == 0:
        return False

    QP  = Q - P
    t = QP.dot(SNV) / RdotSVN
    u = QP.dot(RNV) / RdotSVN

    return t > 0 and u > 0 and t*t < line1_vec.magnitude_squared() and u*u < line2_vec.magnitude_squared()

def CollideRectLine(rectangle, point_1, point_2):
    return (collideLineLine(point_1, point_2, rectangle.topleft, rectangle.bottomleft) or
            collideLineLine(point_1, point_2, rectangle.bottomleft, rectangle.bottomright) or
            collideLineLine(point_1, point_2, rectangle.bottomright, rectangle.topright) or
            collideLineLine(point_1, point_2, rectangle.topright, rectangle.topleft))

def CheckCollision(points_polygon, rectangle, line): #1+2, 2+3, 3+4, 4+5, 5+1
    if line == len(points_polygon):
        if CollideRectLine(rectangle, points_polygon[line-1], points_polygon[0]):
            return True
    else:
        if CollideRectLine(rectangle, points_polygon[line-1], points_polygon[line]):
            return True
    return False

while running:
    clock.tick(60)
    screen.fill("white")
    points_polygon = [(900,600), (500,600),(300, 400),(550,200),(900,200)]
    pygame.draw.polygon(screen, (100,100,100), points_polygon, 1)
    rectangle = rect
    if (not CheckCollision(points_polygon, rectangle, 2)) or (not CheckCollision(points_polygon, rectangle, 3)):
        if MoveLeft:
            rectangle.x -= 3
    if not CheckCollision(points_polygon, rectangle, 5):
        if MoveRight:
            rectangle.x += 3
    screen.blit(img, rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                MoveLeft = True
            if event.key == pygame.K_d:
                MoveRight = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                MoveLeft = False
            if event.key == pygame.K_d:
                MoveRight = False

    pygame.display.update()
    
pygame.quit()
