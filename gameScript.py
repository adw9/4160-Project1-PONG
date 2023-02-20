import pygame
import sys
from mainView import View
from paddle import Paddle
from controller import mainController

#Startup
pygame.init()
obj = View()
user = Paddle()
controller = mainController()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
    
    controller.userInput(user)
    obj.viewUpdate(user)   


