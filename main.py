import pygame
import sys
from constants import *
from player import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))   # TO GET A NEW GUI WINDOW
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    a_field = AsteroidField()

    
    
    dt = 0            
    game_loop = True
    
    while game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for thing in asteroids:
            if thing.collision(player):
                print("Game Over!")
                sys.exit()     
            for bullet in shots:
                if thing.collision(bullet):
                    thing.split()
                    bullet.kill()      

        screen.fill(000)

        for thing in drawable:
            thing.draw(screen) 


        pygame.display.flip()
        dt = clock.tick(60) / 1000


        




if __name__ == "__main__":
    main()