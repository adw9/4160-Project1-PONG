import pygame
import sys
from mainView import View

#Startup
pygame.init()
obj = View()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.quit()
    
    
    obj.viewUpdate()   


