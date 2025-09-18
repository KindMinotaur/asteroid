from constants import *
from player import *
import pygame

dt = 0
clock = pygame.time.Clock()
def main():
    global dt
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0,0,0)
    current = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        current.update(dt)
        pygame.Surface.fill(screen,color)
        current.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000



if __name__ == "__main__":
    main()
