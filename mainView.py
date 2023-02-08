class mainView(gameScript):
    surface
    
    def startUp():
        pygame.display.set_caption("I have no idea what im doing")
        SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500,500
        surface = pygame.display.set_mode(SCREEN_SIZE)

