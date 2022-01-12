

import pygame

from Image import Image
from ImageFactory import ImageFactory

pygame.init()

screenWidth = 400
screenHeight = 1000

Image.screenWidth = screenWidth
Image.screenHeight = screenHeight

screen = pygame.display.set_mode((screenWidth, screenHeight))


imageAmount = 6


imageList = []

for i in range(imageAmount):
    factory = ImageFactory()
    image = factory.makeImage(screenWidth, screenHeight)
    imageList.append(image)




while True:
    screen.fill((0, 0, 0))

    for image in imageList:
        image.draw(screen)
    pygame.display.update()