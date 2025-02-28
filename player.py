import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)

        pygame.draw.polygon(
            self.image,
            'white',
            [(0, 0), (25, 50), (50, 0)],
            width=2
        )

        self.original_image = self.image

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(surface=screen, color="white", points=self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        # self.angle = PLAYER_TURN_SPEED * dt
        self.image = pygame.transform.rotate(self.original_image, self.rotation)
        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(-self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        self.rect.topleft = (int(self.position.x), int(self.position.y))

    def shoot(self):
        shot = Shot(self.rect.centerx, self.rect.centery, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(-self.rotation) * PLAYER_SHOT_SPEED

        