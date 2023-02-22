import pygame
import sys
from mainView import View
from paddle import Paddle
from controller import mainController
from ball import Ball

#Startup
pygame.init()
obj = View()
user = Paddle()
controller = mainController()
ball = Ball()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
    
    controller.userInput(user)
    obj.viewUpdate(user, ball)   


