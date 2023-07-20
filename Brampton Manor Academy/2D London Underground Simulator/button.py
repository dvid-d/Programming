import pygame
#[0] - left mouse button
#[1] - middle mouse button
#[2] - right mouse button


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.shape = self.image.get_rect()
        self.shape.topleft = (x, y)
        self.isClicked = False

    def Draw(self, surface):

        mouse_position = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and self.isClicked == False:
                self.isClicked = True
        
        if pygame.mouse.get_pressed()[0]:
            self.isClicked = False

        surface.blit(self.image, (self.shape.x, self.shape.y))
