import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # The Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        ms_dt = game_clock.tick(60)
        dt = ms_dt / 1000   # track dt in seconds

if __name__ == "__main__":
    main()
