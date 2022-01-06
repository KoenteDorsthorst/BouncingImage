import random

class Image:

    screenWidth = 800
    screenHeight = 800
    xSpeed = 0.1
    ySpeed = 0.1

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

    def bounce(self):

        # changedX = self.changeAngle(self.xSpeed)
        # changedY = self.changeAngle(self.ySpeed)
        # Bounce right side
        if self.x >= self.screenWidth - self.width:
            changedX = self.changeAngle(self.xSpeed)
            self.xSpeed = -changedX


            makeMin = False
            if self.ySpeed < 0:
                makeMin = True
            self.ySpeed = 0.2 - abs(self.xSpeed)
            if makeMin:
                self.ySpeed *= -1

        # Bounce left side
        if self.x <= 0:
            changedX = self.changeAngle(self.xSpeed)
            self.xSpeed = -changedX

            makeMin = False
            if self.ySpeed < 0:
                makeMin = True
            self.ySpeed = 0.2 - abs(self.xSpeed)
            if makeMin:
                self.ySpeed *= -1

        # Bounce bottom side
        if self.y >= self.screenHeight - self.height:
            changedY = self.changeAngle(self.ySpeed)
            self.ySpeed = -changedY

            makeMin = False
            if self.xSpeed < 0:
                makeMin = True
            self.xSpeed = 0.2 - abs(self.ySpeed)
            if makeMin:
                self.xSpeed *= -1

        # Bounce top side
        if self.y <= 0:
            changedY = self.changeAngle(self.ySpeed)
            self.ySpeed = -changedY

            makeMin = False
            if self.xSpeed < 0:
                makeMin = True
            self.xSpeed = 0.2 - abs(self.ySpeed)
            if makeMin:
                self.xSpeed *= -1

    def changeAngle(self, angle):
        randomNumber = random.randrange(-100, 100)
        randomNumber *= 0.0001
        print("-------------")
        print(randomNumber)
        print(abs(self.xSpeed) + abs(self.ySpeed))
        angle += randomNumber
        return angle

