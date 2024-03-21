import pygame

class Tile(pygame.sprite.Sprite):
    global temp 
    temp = []
    def __init__(self, pos, surface, groups):
        super().__init__(groups)
        self.image = surface
        #print(pos)
        self.rect = self.image.get_rect(topleft = pos)
        # except:
        #     temp.append(pos)

    def getCoords(self):
        return self.__pos