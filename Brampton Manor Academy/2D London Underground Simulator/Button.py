class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.shape = self.image.get_rect()
        self.shape.topleft = (x, y)

    def Draw(self):
        screen.blit(self.image, (self.shape.x, self.shape.y))