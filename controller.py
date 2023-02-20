import pygame
from paddle import Paddle


class mainController():
    #filler var, I have no idea what to put here.
    #rectSpeed = 0
    input = False

    def userInput(self, paddle):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            input = True
            paddle.move_rect(input)
        elif keys[pygame.K_DOWN]:
            input = False
            paddle.move_rect(input)

