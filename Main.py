import pygame

from Image import Image

pygame.init()

screen = pygame.display.set_mode((800, 800))

imageX = 20
imageY = 20
imageWidth = 100
imageHeight = 100
imageImage = pygame.image.load('block.png')


image = Image(imageX, imageY, imageWidth, imageHeight, imageImage)


while True:
    screen.fill((0, 0, 0))

    image.draw(screen)
    pygame.display.update()