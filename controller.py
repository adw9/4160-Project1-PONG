import pygame


class mainController():
    #need a better solution for a var to pass than a bool
    #true = up, false = down
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

    def collisionDetection(self, u1, u2, ball):

        if(u1.gameRect.colliderect(ball.gameRect)):
            ball.moveLeft = False
        elif(u2.gameRect.colliderect(ball.gameRect)):
            ball.moveLeft = True

        #top/left/right/bottom screen bounds
        topWall = pygame.Rect(0, 0, 700, 1)
        botWall = pygame.Rect(0, 500, 700, 1)
        leftWall = pygame.Rect(0,0,1,700)
        rightWall = pygame.Rect(700,0,1,700)

        #collision detection between ball and outside walls
        if(ball.gameRect.colliderect(topWall)):
            ball.moveDown = True
        elif(ball.gameRect.colliderect(botWall)):
            ball.moveDown = False
        elif(ball.gameRect.colliderect(leftWall)):
            print("Player 2 Scores!")
            ball.moveLeft = False
            ball.ball_reset()
        elif(ball.gameRect.colliderect(rightWall)):
            print("Player 1 Scores!")
            ball.moveLeft = True
            ball.ball_reset()

        ball.move_ball()
