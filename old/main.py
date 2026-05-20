import pygame
from render.pygame_view import PygameView

view = PygameView()

# game = Game(n_players=1)
# state = game.reset()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                pass
                # state = game.step("draw")

            if event.key == pygame.K_s:
                pass
                # state = game.step("stop")

            if event.key == pygame.K_u:
                pass
                # state = game.step("undo")

    view.draw()