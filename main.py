import sys
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
def main():
    pygame.init()
    screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    clock=pygame.time.Clock()
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers=(updatable,drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers=(updatable,)
    player=Player(x,y)
    asteroidfield=AsteroidField()
    dt=0
    while True:
        dt=clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)
        game_over=False
        for obj in asteroids:
            for shot in shots:
                if shot.detectCollision(obj):
                    shot.kill()
                    obj.split()
                    
        for obj in asteroids:
            if obj.detectCollision(player):
                game_over=True
                break
        if game_over:
            print("Game over!")
            sys.exit()
        

        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        



if __name__ == "__main__":
    main()
