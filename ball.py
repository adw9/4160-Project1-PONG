import pygame

#hit top wall, reverse y velocity. hit paddle, reverse x velocity. 


class Ball():
    #storage vars
    diameter = 0
    color = (0,0,0)
    ballPos = ballX, ballY = 0, 0
    speedX = 0
    speedY = 0

    moveLeft = True
    moveDown = True


    #collision detection vars
    rectWidth = 0
    rectHeight = 0
    gameRect = pygame.Rect(ballX, ballY, rectWidth, rectHeight)

    def __init__(self):
        self.ballPos = self.ballX, self.ballY = 250, 250
        self.diameter = 10
        self.color = (255,0,0)
        self.speedX = .08
        self.speedY = .08


        self.rectWidth = 10
        self.rectHeight = 10

    def move_ball(self):            

        if(self.moveLeft):
            self.ballX -= self.speedX
        else:
            self.ballX += self.speedX
        
        if(self.moveDown):
            self.ballY += self.speedY
        else:
            self.ballY -= self.speedY    
        #update gameRect with new var
        print("ballX = ",self.ballX)
        self.ballPos = self.ballX, self.ballY
        self.gameRect = pygame.Rect(self.ballX, self.ballY, self.rectWidth, self.rectHeight)
        