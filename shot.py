import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH


class Shot(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(surface=screen,color="RED",center=(self.position.x,self.position.y),radius=self.radius,width=LINE_WIDTH)


    def update(self,dt):
        self.position += self.velocity * dt