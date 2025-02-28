from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)

        pygame.draw.circle(
            self.image,
            'white',
            (radius, radius),
            radius=radius,
            width=2
        )

        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.rect.centerx, self.rect.centery, new_radius)
            new_asteroid2 = Asteroid(self.rect.centerx, self.rect.centery, new_radius)

            new_asteroid1.velocity = vector1 * 1.2 #scaling up speed
            new_asteroid2.velocity = vector2