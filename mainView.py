import pygame
import sys

class View():
   SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500,500
   surface = pygame.display.set_mode(SCREEN_SIZE)
   #colors
   screenColor = (50,50,50)

   #placeholder, will be replaced by paddle class
   gameRect = pygame.Rect(50, 50, 50, 50)
   rectColor = (255, 0, 0)


   def __init__(self):
      pygame.display.set_caption("I have no idea what im doing")
      SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500,500
      surface = pygame.display.set_mode(SCREEN_SIZE)

      #This will take paddle and ball as an arguement soon
   def viewUpdate(self):
      
      self.surface.fill(self.screenColor)
      pygame.draw.rect(self.surface, self.rectColor, self.gameRect)
      
      pygame.display.update()


