import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))   # TO GET A NEW GUI WINDOW
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    dt = 0            
    game_loop = True
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(000)
        for thing in drawable:
            thing.draw(screen)

        for thing in updatable:
            thing.update(dt)    
        # updatable.update(dt)
        # drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


        




if __name__ == "__main__":
    main()