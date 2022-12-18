import pygame


class GameSession:

    def __init__(self):
        self.SCREEN_SIZE = (800, 800)
        self.BACKGROUND_COLOR = (255, 0, 0)

        pygame.init()

        self.SCREEN = pygame.display.set_mode