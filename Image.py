class Image:

    def __init__(self, xStart, yStart, width, length, image):
        self.x = xStart
        self.y = yStart
        self.width = width
        self.length = length
        self.image = image


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


