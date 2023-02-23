import pygame
from paddle import Paddle


class mainController():
    #need a better solution for a var to pass than a bool
    input = False

    def userInput(self, u1, u2):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            input = True
            u2.move_rect(input)
        elif keys[pygame.K_DOWN]:
            input = False
            u2.move_rect(input)
        elif keys[pygame.K_w]:
            input = True
            u1.move_rect(input)
        elif keys[pygame.K_s]:
            input = False
            u1.move_rect(input)

