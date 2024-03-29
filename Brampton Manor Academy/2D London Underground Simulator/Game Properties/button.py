import pygame
#[0] left mouse button
#[1] middle mouse button
#[2] right mouse button


class Button():
    def __init__(self, surface, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.__isClicked = False
        self.__surface = surface
        surface.blit(self.image, (x, y))
    
    def display(self):
        self.__surface.blit(self.image, self.rect.topleft)

    def setClicked(self, clicked):
        self.__isClicked = False

    def wasClicked(self):
        mouse_position = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and self.__isClicked == False:
                self.__isClicked = True
            elif pygame.mouse.get_pressed()[0] == 0:
                self.__isClicked = False
        return self.__isClicked
    