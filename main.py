import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Initialize all pygame modules.
    pygame.init()

    # Set screen boundaries.
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    # Create our game clock.
    clock = pygame.time.Clock()

    # Create our groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Asteroid groups
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidField = AsteroidField()

    # Create our player.
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    # Begin game loop
    while True:
        # Exit logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # First this we want to do is update the player?
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_for_collisions(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.check_for_collisions(shot):
                    shot.kill()
                    asteroid.split()

        
        # Set the background.
        screen.fill('black')
        # Draw our player every frame.
        for obj in drawable:
            obj.draw(screen)

        # Refresh display
        pygame.display.flip()

        # limit framerate to 60 fps.
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
