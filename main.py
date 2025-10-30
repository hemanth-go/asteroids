import pygame
from constants import *
from circleshape import *
from player import *
def main():
    pygame.init()
    screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    clock=pygame.time.Clock()
    player=Player(x,y)
    dt=0
    while True:
        dt=clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        



if __name__ == "__main__":
    main()
