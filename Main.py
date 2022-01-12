import random

import pygame

from Image import Image

pygame.init()

screenWidth = 400
screenHeight = 1000

Image.screenWidth = screenWidth
Image.screenHeight = screenHeight

screen = pygame.display.set_mode((screenWidth, screenHeight))

imageX = 10
imageY = 60
imageWidth = 100
imageHeight = 100
imageImage = pygame.image.load('block.png')


imageList = []

for i in range(6):
    imageX = random.randrange(0, screenWidth - imageWidth)
    imageY = random.randrange(0, screenHeight - imageHeight)

    image = Image(imageX, imageY, imageWidth, imageHeight, imageImage)
    imageList.append(image)




while True:
    screen.fill((0, 0, 0))

    for image in imageList:
        image.draw(screen)
    pygame.display.update()