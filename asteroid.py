import pygame
import random
from constants import *
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, width=2)    

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand = random.uniform(20, 50)
            vector1 = self.velocity.rotate(rand)
            vector2 = self.velocity.rotate(-rand)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            newAst1 = Asteroid(self.position.x, self.position.y, new_radius)
            newAst2 = Asteroid(self.position.x,self.position.y, new_radius)

            newAst1.velocity = vector1 * 1.2
            newAst2.velocity = vector2 * 1.2