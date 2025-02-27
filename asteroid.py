from circleshape import CircleShape
import pygame

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