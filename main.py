import pygame

from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state
from player import Player


def main():
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            screen.fill((0, 0, 0))
            player.draw(screen)
            if event.type == pygame.QUIT:
                return
            pass
        pygame.display.flip()
        dt = clock.tick(60)/1000
        # print(f"dt:{dt}")



if __name__ == "__main__":
    main()
