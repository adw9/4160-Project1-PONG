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
            print("ball hit left")
            ball.moveLeft = False
        elif(u2.gameRect.colliderect(ball.gameRect)):
            print("ball hit right")
            ball.moveLeft = True


        #self.gameRect = pygame.Rect(self.rectX, self.rectY, self.rectWidth, self.rectHeight)

        #top/left/right/bottom screen bounds for ball
        topWall = pygame.Rect(0, 0, 600, 5)
        botWall = pygame.Rect(0, 600, 600, 5)
        leftWall = pygame.Rect(0,0,5,600)
        rightWall = pygame.Rect(600,0,5,600)

        if(ball.gameRect.colliderect(topWall)):
            ball.moveDown = True
        elif(ball.gameRect.colliderect(botWall)):
            ball.moveDown = False
        elif(ball.gameRect.colliderect(leftWall)):
            print("Player2 Scores!")
            ball.moveLeft = False
        elif(ball.gameRect.colliderect(rightWall)):
            print("Player 1 Scores!")
            ball.moveLeft = True

        ball.move_ball()
