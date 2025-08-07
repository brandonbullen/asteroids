import pygame
import random

from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Generate random angle to send asteroids in.
        random_angle = random.uniform(20, 50)

        # Create vectors our new asteroids will travel along.
        a1_vector = self.velocity.rotate(random_angle)
        a2_vector = self.velocity.rotate(-random_angle)

        # Generate smaller size.
        smaller_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create the new asteroids.
        a1 = Asteroid(self.position.x, self.position.y, smaller_radius)
        a2 = Asteroid(self.position.x, self.position.y, smaller_radius)

        # Set velocity for new asteroids.
        a1.velocity = a1_vector * 1.2
        a2.velocity = a2_vector * 1.2
        

