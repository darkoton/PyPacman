import pygame

from pacman import Pacman
from map import Map
from devtools import Devtools


class Game:
    def __init__(self, settings, screen):
        self.settings = settings
        self.settings.font = {
            "6": pygame.font.Font("./resources/PressStart2P-Regular.ttf", 6),
            "15": pygame.font.Font("./resources/PressStart2P-Regular.ttf", 15),
        }

        self.screen = screen
        self.clock = pygame.time.Clock()
        self.score = 0

        self.pacman = Pacman(settings, screen)
        self.map = Map(settings, screen)

        self.devtools = Devtools(settings, screen)

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
                        self.settings.devtools = not self.settings.devtools
                    if event.key == pygame.K_F11:
                        self.settings.grid = not self.settings.grid
                    if event.key == pygame.K_SPACE:
                        self.pause = not self.pause

            self.draw_game()
            self.command_from_keyboard(pygame.key.get_pressed())
            # not self.collision_with_wall() and
            if not self.collision_with_wall() and not self.pause:
                self.pacman.move_pacman()

            if self.collision_with_dot():
                self.map.remove_item(self.pacman.get_coordinate_pacman())
                self.score += 1

            pygame.time.wait(self.settings.speed)
            self.clock.tick(self.settings.fps)

    def draw_game(self):
        self.screen.fill(self.settings.BG_COLOR)
        self.map.draw_map()
        self.pacman.draw_pacman()

        if self.settings.devtools:
            self.devtools.draw_info(
                [
                    f"Next element: {self.get_next_map_element()}",
                    f"Direction: {self.pacman.direction}",
                    f"Direction word: {self.pacman.directionWord}",
                    f"Pause: {self.pause}",
                    "Pacman:",
                    f"  coords: {self.pacman.get_coordinate_pacman()}",
                    f"  top: {self.pacman.top}",
                    f"  right: {self.pacman.right}",
                    f"  bottom: {self.pacman.bottom}",
                    f"  left: {self.pacman.left}",
                    f"Score: {self.score}",
                    f"Grid: {self.settings.grid}",
                    f"FPS: {self.settings.fps}",
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

        direction = self.pacman.directionWord

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            direction = "up"
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            direction = "down"
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            direction = "right"
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            direction = "left"

        if self.can_rotate(direction):
            self.pacman.rotate_pacman(direction)

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

        if (
            self.map.get_element_by_coords(pacman_coords) == "."
            or self.map.get_element_by_coords(pacman_coords) == "o"
        ):
            return True
        else:
            return False

    def can_rotate(self, direction):
        pacman_coords = self.pacman.get_coordinate_pacman()

        result = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
        }

        offsets = {
            "up": (0, -1),
            "down": (0, 1),
            "left": (-1, 0),
            "right": (1, 0),
        }

        for dir_name in result:
            dx, dy = offsets[dir_name]
            x, y = pacman_coords
            next_coords = (x + dx, y + dy)

            element = self.map.get_element_by_coords(next_coords)

            result[dir_name] = element != "#"

        return result[direction]
