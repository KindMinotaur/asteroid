from asteroidfield import *
from constants import *
from player import *
import pygame

dt = 0
clock = pygame.time.Clock()
def main():
    global dt
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0,0,0)
    AsteroidField()
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print(len(updatable))
    print(len(drawable))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        pygame.Surface.fill(screen,color)
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        clock.tick(60)



if __name__ == "__main__":
    main()
