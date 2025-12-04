from math import log
import pygame

from pacman import Pacman

from map import Map


class Game:
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.score = 0

        self.pacman = Pacman(settings, screen)
        self.map = Map(settings, screen)

    def run(self):
        running = True
        while running:
            # if self.collision_with_ghost():
            # self.game_over()
            #     break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_game()
            self.command_from_keyboard(pygame.key.get_pressed())
            self.pacman.move_pacman()
            # time.sleep(0.1)
            self.clock.tick(60)

    def draw_game(self):
        self.screen.fill(self.settings.BG_COLOR)
        self.map.draw_map()
        self.pacman.draw_pacman()

        pygame.display.update()

    def new_game(self):
        self.score = 0

    def command_from_keyboard(self, keys):
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.pacman.rotate_pacman("up")
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.pacman.rotate_pacman("down")
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.pacman.rotate_pacman("right")
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.pacman.rotate_pacman("left")

    def game_over(self):
        self.score = 0

    def pause(self):
        pass

    def collision_with_wall(self):
        pass
