import pygame
import sys
from mainView import View
from paddle import Paddle
from controller import mainController
from ball import Ball

#Startup
pygame.init()
obj = View()

u1 = Paddle()
u2 = Paddle()
u2.setPlayer2()

controller = mainController()
ball = Ball()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
    
    controller.userInput(u1,u2)
    obj.viewUpdate(u1,u2, ball)   


