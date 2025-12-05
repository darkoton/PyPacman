import pygame

from pacman import Pacman
from map import Map
from devtools import Devtools


class Game:
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.score = 0

        self.pacman = Pacman(settings, screen)
        self.map = Map(settings, screen)
        self.font = pygame.font.Font("./resources/PressStart2P-Regular.ttf", 15)

        self.devtools = Devtools(settings, screen, self.font)
        self.showDevtools = False

        self.pause = False

    def run(self):
        running = True
        while running:
            # if self.collision_with_ghost():
            # self.game_over()
            #     break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_F12:
                        self.showDevtools = not self.showDevtools
                    if event.key == pygame.K_SPACE:
                        self.pause = not self.pause

            self.draw_game()
            self.command_from_keyboard(pygame.key.get_pressed())
            self.collision_with_wall()
            if not self.collision_with_wall() and not self.pause:
                self.pacman.move_pacman()

            if self.collision_with_dot():
                self.map.remove_item(self.pacman.get_coordinate_pacman())
                self.score += 1

            # time.sleep(0.1)
            self.clock.tick(60)

    def draw_game(self):
        self.screen.fill(self.settings.BG_COLOR)
        self.map.draw_map()
        self.pacman.draw_pacman()

        if self.showDevtools:
            self.devtools.draw_info(
                [
                    f"Next element: {self.get_next_map_element()}",
                    f"Direction: {self.pacman.direction}",
                    f"Pause: {self.pause}",
                    f"Pacman coords: {self.pacman.get_coordinate_pacman()}",
                    f"Score: {self.score}",
                ]
            )

        pygame.display.update()

    def new_game(self):
        self.score = 0

    def command_from_keyboard(self, keys):
        # if (
        #     abs(
        #         self.pacman.x_coordinate / self.settings.SIZE
        #         - self.pacman.get_coordinate_pacman()[0]
        #     )
        #     != 0.5
        #     or abs(
        #         self.pacman.y_coordinate / self.settings.SIZE
        #         - self.pacman.get_coordinate_pacman()[1]
        #     )
        #     != 0.5
        # ):
        #     return

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

    def get_next_map_element(self):
        pacman_coords = self.pacman.get_coordinate_pacman()

        next_coords = (
            pacman_coords[0] + 1 * self.pacman.direction[0],
            pacman_coords[1] + 1 * self.pacman.direction[1],
        )
        next_element_map = self.map.get_element_by_coords(next_coords)
        return next_element_map

    def collision_with_wall(self):
        if self.get_next_map_element() == "#":
            return True
        else:
            return False

    def collision_with_dot(self):
        pacman_coords = self.pacman.get_coordinate_pacman()

        if self.map.get_element_by_coords(pacman_coords) == ".":
            return True
        else:
            return False
