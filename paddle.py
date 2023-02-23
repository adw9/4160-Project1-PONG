import pygame


class Paddle():
    rectColor = (5, 0, 0)
    rectSize = rectWidth, rectHeight = 50, 100
    rectPos = rectX, rectY = 0, 0
    rectSpeed = 0

    #I want a solution to barrers outside of this
    SCREEN_HEIGHT = 0

    gameRect = pygame.Rect(rectX, rectY, rectWidth, rectHeight)
    
    
    def __init__(self):
        self.rectY = 300
        self.rectSpeed = .5
        self.SCREEN_HEIGHT = 500
        self.gameRect = pygame.Rect(self.rectX, self.rectY, self.rectWidth, self.rectHeight)
    #X is unecesary as X never leaves the wall for Pong, but is kept for future adaptability.

    #this function does nothing except move this paddle to the right side of the map
    def setPlayer2(self):
        self.rectX = 550
        self.gameRect = pygame.Rect(self.rectX, self.rectY, self.rectWidth, self.rectHeight)


    def move_rect(self,input):
        if(input and self.rectY > 0):
            self.rectY -= self.rectSpeed
        elif(not input and self.rectY < (self.SCREEN_HEIGHT)):
            self.rectY += self.rectSpeed
            

        #update gameRect with new var
        self.gameRect = pygame.Rect(self.rectX, self.rectY, self.rectWidth, self.rectHeight)