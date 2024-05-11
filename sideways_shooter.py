import sys

import pygame

class SidewaysShooter:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 800))

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            pygame.display.flip()

if __name__ == '__main__':
    SidewaysShooter().run_game()