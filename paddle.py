import pygame


class Paddle():
    rectColor = (5, 0, 0)
    rectSize = rectWidth, rectHeight = 50, 100
    rectPos = rectX, rectY = 0, 0
    rectSpeed = 0

    gameRect = pygame.Rect(rectX, rectY, rectWidth, rectHeight)
    
    
    def __init__(self):
        self.rectY = 100
        self.rectSpeed = 2
    #X is unecesary as X never leaves the wall for Pong, but is kept for future adaptability.
    def updatePos(self,X,Y):
        self.rectX = X
        self.rectY = Y
        
