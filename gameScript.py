import pygame
import os
import mainView
pygame.init()
obj = mainView()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    


