import random

import pygame

from Image import Image


class ImageFactory:
    imageWidth = 100
    imageHeight = 100
    imageImage = pygame.image.load('block.png')



    def makeImage(self, screenWidth, screenHeight):
        imageX = random.randrange(0, screenWidth - self.imageWidth)
        imageY = random.randrange(0, screenHeight - self.imageHeight)

        image = Image(imageX, imageY, self.imageWidth, self.imageHeight, self.imageImage)

        return image
