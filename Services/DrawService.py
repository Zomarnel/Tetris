import pygame


class DrawService:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    @staticmethod
    def draw_layout(screen):
        # PLAYGROUND RECTANGLE
        playground_rect = pygame.Rect(331, 43, 325, 650)

        screen.fill(DrawService.BLACK, playground_rect)

        # Hold Rectangle
        hold_rectangle = pygame.Rect(90, 73, 160, 106)

        screen.fill(DrawService.BLACK, hold_rectangle)

        # Next Rectangle
        next_rectangle = pygame.Rect(732, 69, 158, 270)

        screen.fill(DrawService.BLACK, next_rectangle)

        # Score Rectangle
        next_rectangle = pygame.Rect(91, 425, 178, 256)

        screen.fill(DrawService.BLACK, next_rectangle)

