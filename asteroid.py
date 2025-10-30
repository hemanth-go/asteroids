import pygame
import random
from circleshape import *
from constants import *
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width=2)

    def update(self,dt):
        self.position+=self.velocity*dt

    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle=random.uniform(20,50)
            ast_v1=self.velocity.rotate(random_angle)
            ast_v2=self.velocity.rotate(-random_angle)
            new_radius=self.radius-ASTEROID_MIN_RADIUS
            ast1=Asteroid(self.position.x,self.position.y,new_radius)
            ast2=Asteroid(self.position.x,self.position.y,new_radius)
            ast1.velocity=ast_v1*1.2
            ast2.velocity=ast_v2*1.2

