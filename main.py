import pygame
import sys

from Services import DrawService


def main():

    # Initialization
    pygame.init()

    draw = DrawService.DrawService

    # Initialize Background
    background_color = draw.WHITE
    screen_size = (1004, 755)

    screen = pygame.display.set_mode(screen_size)

    # Set game title and icon
    pygame.display.set_caption("Tetris")
    tetris_icon = pygame.image.load("Images/Tetris_Icon.png")
    pygame.display.set_icon(tetris_icon)

    # Main Game Loop
    running = True

    while running:

        # Clear Screen
        screen.fill(background_color)

        # Draw Layout
        draw.draw_layout(screen)

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update Screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
