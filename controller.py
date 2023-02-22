import pygame
from paddle import Paddle


class mainController():
    #need a better solution for a var to pass than a bool
    input = False

    def userInput(self, paddle):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            input = True
            paddle.move_rect(input)
        elif keys[pygame.K_DOWN]:
            input = False
            paddle.move_rect(input)

