import pygame

from constants import *

def main():
    # Initialize all pygame modules.
    pygame.init()

    # Set screen boundaries.
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    # Begin game loop
    while True:
        # Set the background.
        screen.fill('black')
        
        # Exit logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Refresh display
        pygame.display.flip()
    



if __name__ == "__main__":
    main()
