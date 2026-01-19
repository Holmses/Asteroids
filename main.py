import sys

import pygame

from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state,log_event
from player import Player


def main():
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable,drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("shot_hit")
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000


        # print(f"dt:{dt}")



if __name__ == "__main__":
    main()
