import pygame

#hit top wall, reverse y velocity. hit paddle, reverse x velocity. 


class Ball():
    #storage vars
    diameter = 0
    color = (0,0,0)
    ballPos = ballX, ballY = 0, 0
    speedX = 0
    speedY = 0

    def __init__(self):
        self.ballPos = self.ballX, self.ballY = 250, 250
        self.diameter = 10
        self.color = (255,0,0)
        self.speedX = 2
        self.speedY = 2
        