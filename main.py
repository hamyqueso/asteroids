import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroid, updateable, drawable)
    AsteroidField.containers = (updateable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    


    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        # player.draw(screen)
        
        drawable.draw(screen)
        updateable.update(dt)
        # asteroid_field.update(dt)
        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()