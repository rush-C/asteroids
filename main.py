import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))   # TO GET A NEW GUI WINDOW
    clock = pygame.time.Clock()
    dt = 0            
    game_loop = True
    while game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(000)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


        




if __name__ == "__main__":
    main()