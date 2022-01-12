import random

class Image:

    screenWidth = 0
    screenHeight = 0
    totalSpeed = 1
    xSpeed = totalSpeed / 2
    ySpeed = totalSpeed / 2

    def __init__(self, xStart, yStart, width, height, image):
        self.x = xStart
        self.y = yStart
        self.width = width
        self.height = height
        self.image = image


    def draw(self, screen):
        self.bounce()
        self.move()
        screen.blit(self.image, (self.x, self.y))



    def move(self):
        self.x += self.xSpeed
        self.y += self.ySpeed

        if self.x < 0:
            self.x = 0
        if self.x > self.screenWidth - self.width:
            self.x = self.screenWidth - self.width
        if self.y < 0:
            self.y = 0
        if self.y > self.screenHeight - self.height:
            self.y = self.screenHeight - self.height

    def bounce(self):

        # Bounce horizontal
        if self.x >= self.screenWidth - self.width or self.x <= 0:
            changedX = self.changeAngle(self.xSpeed)
            self.xSpeed = -changedX

            makeMin = False
            if self.ySpeed < 0:
                makeMin = True
            self.ySpeed = self.totalSpeed - abs(self.xSpeed)
            if makeMin:
                self.ySpeed *= -1


        # Bounce vertical
        if self.y >= self.screenHeight - self.height or self.y <= 0:
            changedY = self.changeAngle(self.ySpeed)
            self.ySpeed = -changedY

            makeMin = False
            if self.xSpeed < 0:
                makeMin = True
            self.xSpeed = self.totalSpeed - abs(self.ySpeed)
            if makeMin:
                self.xSpeed *= -1


    def changeAngle(self, angle):
        randomizerLimit = 100
        randomNumberMultiplier = 0.0002
        randomNumber = random.randrange(-randomizerLimit, randomizerLimit)
        randomNumber *= randomNumberMultiplier
        angle += randomNumber

        if abs(angle) <= self.totalSpeed/10 or abs(angle) >= self.totalSpeed/10 * 9:
            if angle < 0:
                angle = -(self.totalSpeed/2)
            else:
                angle = self.totalSpeed/2
        return angle

