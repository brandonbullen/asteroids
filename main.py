import pygame

from constants import *
from player import Player

def main():
    # Initialize all pygame modules.
    pygame.init()

    # Set screen boundaries.
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    # Create our game clock.
    clock = pygame.time.Clock()
    dt = 0

    # Create our player.
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Begin game loop
    while True:
        # Exit logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Set the background.
        screen.fill('black')
    
        # Draw our player every frame.
        player.draw(screen)

        # Refresh display
        pygame.display.flip()

        # limit framerate to 60 fps.
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
