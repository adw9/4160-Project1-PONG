import pygame
import sys
from mainView import View
from paddle import Paddle

#Startup
pygame.init()
obj = View()
user = Paddle()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.quit()
    
    
    obj.viewUpdate(user)   


