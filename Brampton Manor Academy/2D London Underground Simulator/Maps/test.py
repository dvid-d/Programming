import pygame, sys
from pytmx.util_pygame import load_pygame

#Sprite - Objects with different properties like height width, colour, etc and methods like mnoving right, left, up and down, jump etc

class TIle(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.getrect(topleft = pos)

pygame.init()
screen = pygame.display.set_mode((1920,1080))
map_data = load_pygame('C:\\Users\\ddobr\\Desktop\\Sixth Form\\Computer Science\\Github\\Programming\\Brampton Manor Academy\\2D London Underground Simulator\\Maps\\tutorial.tmx')
print(map_data.layernames)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")
    pygame.display.update()