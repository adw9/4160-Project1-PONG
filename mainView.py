import pygame
import sys


class View():
   SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500,500
   surface = pygame.display.set_mode(SCREEN_SIZE)
   #colors
   screenColor = (50,50,50)

   #placeholder, will be replaced by paddle class
   #gameRect = pygame.Rect(50, 50, 50, 50)
   #rectColor = (255, 0, 0)


   def __init__(self):
      pygame.display.set_caption("PONG")
      SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600,600
      surface = pygame.display.set_mode(SCREEN_SIZE)

      #This will take paddle and ball as an arguement soon
   def viewUpdate(self, paddle):
      #background
      self.surface.fill(self.screenColor)
      
      #user paddle
      pygame.draw.rect(self.surface, paddle.rectColor, paddle.gameRect)
      
      
      pygame.display.update()


