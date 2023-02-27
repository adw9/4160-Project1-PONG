import pygame
import sys
from mainView import View
from paddle import Paddle
from controller import mainController
from ball import Ball
from model import Model

#Startup, create objects
pygame.init()
obj = View()
u1 = Paddle()
u2 = Paddle()
controller = mainController()
ball = Ball()
model = Model()

#move player2 to right side
u2.setPlayer2()


#game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
    
    controller.userInput(u1,u2)
    controller.collisionDetection(u1,u2,ball,model)
    obj.viewUpdate(u1,u2, ball)   

    if(model.detWinner()):
        pygame.quit() 
        sys.exit()


