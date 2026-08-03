from curses import window

import pygame
from wcwidth import width

class PygameView:

    def __init__(self,
                 windowWidth=1024,
                 windowHeight=1024,
                 resolution_x=2337,
                 resolution_y=2337):

        # self.background_image = pygame.image.load("spiral_circles.png")

        pygame.init()

        bg = pygame.image.load("spiral_circles.svg")
        # self.screen = pygame.display.set_mode(bg.get_size())

        self.screen = pygame.display.set_mode((resolution_x, resolution_y))
        self.window = pygame.display.set_mode((windowWidth, windowHeight))

        # Source - https://stackoverflow.com/a/51243689
        # Posted by Nipun Thennakoon, modified by community. See post 'Timeline' for change history
        # Retrieved 2026-05-19, License - CC BY-SA 4.0
        
        self.screen.blit(bg, (0, 0))

        self.screen = pygame.transform.scale(self.screen, (windowWidth, windowHeight)) 
        self.window.blit(self.screen, (0, 0))

        # bg = pygame.transform.scale(bg, (width, height))

        # self.background_image = pygame.transform.smoothscale(
        #     bg, (width, height))

        # pygame.init()

        # self.screen = pygame.display.set_mode((width, height))

        self.background_image = bg

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 20)

    def draw(self, state=None):
        self.window.fill("#FFFFFF")
        self.screen.blit(self.background_image, (0, 0))
        pygame.display.update()

        # self._draw_board(state)
        # self._draw_player(state)

        # pygame.display.flip()
        self.clock.tick(60)