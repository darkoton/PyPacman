from random import random
import pygame
import math

from pacman import Pacman
from ghost import Ghost
from map import Map
from devtools import Devtools
from menu import Menu

ghosts_data = [
    {
        "name": "Blinky",
        "color": (255, 0, 0),
        "spawn_coords": (15, 11),
        "aggressive_point": (24, -5),
    },
    {
        "name": "Pinky",
        "color": (255, 185, 255),
        "spawn_coords": (12, 11),
        "aggressive_point": (4, -5),
    },
    {
        "name": "Clyde",
        "color": (255, 185, 81),
        "spawn_coords": (13, 11),
        "aggressive_point": (0, 31),
    },
    {
        "name": "Inky",
        "color": (0, 255, 255),
        "spawn_coords": (12, 11),
        "aggressive_point": (27, 31),
    },
]


class Game:
    def __init__(self, settings, screen):
        self.settings = settings
        self.settings.font = {
            "6": pygame.font.Font("./resources/PressStart2P-Regular.ttf", 6),
            "15": pygame.font.Font("./resources/PressStart2P-Regular.ttf", 15),
            "20": pygame.font.Font("./resources/PressStart2P-Regular.ttf", 20),
            "40": pygame.font.Font("./resources/PressStart2P-Regular.ttf", 40),
        }

        self.screen = screen
        self.clock = pygame.time.Clock()
        self.score = 0

        self.pacman = Pacman(settings, screen)
        self.map = Map(settings, screen)

        self.ghosts = []

        self.state = "menu"
        self.menu = Menu(settings, screen)

        for ghost in ghosts_data:
            self.ghosts.append(
                Ghost(
                    self.settings,
                    self.screen,
                    ghost["color"],
                    ghost["spawn_coords"],
                    ghost["aggressive_point"],
                    ghost["name"],
                )
            )

        self.devtools = Devtools(settings, screen)

        self.pause = False

    def run(self):
        running = True
        while running:

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

            if self.collision_with_ghost():
                self.game_over()
                break

            if not self.pause and self.state == "play":
                if not self.collision_with_wall(self.pacman):
                    self.pacman.move()

                for ghost in self.ghosts:
                    check_rotate = self.can_rotate(ghost, True)
                    available_directions = [
                        dir for dir, can_move in check_rotate.items() if can_move
                    ]

                    if any(check_rotate.values()):

                        if ghost.see_pacman:
                            ghost_next_directions = ghost.determine_directions(
                                self.pacman.get_coordinate()
                            )
                        else:
                            ghost_next_directions = ghost.determine_directions()

                        if int(random() * 100) < self.settings.ghost_brain_power:
                            if check_rotate[ghost_next_directions[0]]:
                                ghost.rotate(ghost_next_directions[0])
                            elif check_rotate[ghost_next_directions[1]]:
                                ghost.rotate(ghost_next_directions[1])
                            else:
                                ghost.rotate(available_directions[0])

                        else:
                            ghost.rotate(
                                available_directions[
                                    math.floor(len(available_directions) * random())
                                ]
                            )

                    if not self.collision_with_wall(ghost):
                        ghost.move()

                    if self.collision_with_visor(ghost):
                        ghost.see_pacman = True
                    else:
                        ghost.see_pacman = False

                if self.collision_pacman_with_dot():
                    self.map.remove_item(self.pacman.get_coordinate())
                    self.score += 1

            pygame.time.wait(self.settings.speed)
            self.clock.tick(self.settings.fps)

    def draw_game(self):
        self.screen.fill(self.settings.BG_COLOR)

        if self.state == "menu":
            self.menu.draw()
        elif self.state == "play":
            self.map.draw_map()
            self.pacman.draw_pacman()

            for ghost in self.ghosts:
                ghost.draw_ghost()

            if self.settings.devtools:
                self.devtools.draw_info(
                    [
                        f"Next element: {self.get_next_map_element(self.pacman)}",
                        f"Direction: {self.pacman.direction}",
                        f"Direction word: {self.pacman.directionWord}",
                        f"Pause: {self.pause}",
                        "Pacman:",
                        f"  coords: {self.pacman.get_coordinate()}",
                        f"  top: {self.pacman.top}",
                        f"  right: {self.pacman.right}",
                        f"  bottom: {self.pacman.bottom}",
                        f"  left: {self.pacman.left}",
                        f"Score: {self.score}",
                        f"Grid: {self.settings.grid}",
                        f"FPS: {self.settings.fps}",
                    ]
                )

            score_surf = self.settings.font["15"].render(
                f"Score: {self.score}", False, (0, 0, 0)
            )
            self.screen.blit(
                score_surf, (1 * self.settings.SIZE, 10 * self.settings.SIZE)
            )

        pygame.display.update()

    def new_game(self):
        self.score = 0

    def command_from_keyboard(self, keys):
        if self.state == "play":
            direction = self.pacman.directionWord
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                direction = "up"
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                direction = "down"
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                direction = "right"
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                direction = "left"

            if self.can_rotate(self.pacman, False, direction):
                self.pacman.rotate(direction)

        elif self.state == "menu":
            if keys[pygame.K_RETURN]:
                self.state = "play"

        if keys[pygame.K_ESCAPE]:
            if self.state == "play" or self.state == "lose":
                self.state = "menu"
            else:
                self.state = "play"

    def game_over(self):
        self.score = 0

    def pause(self):
        pass

    def get_next_map_element(self, entity=None):
        if entity is None:
            entity = self.pacman

        pacman_coords = entity.get_coordinate()

        next_coords = (
            pacman_coords[0] + 1 * entity.direction[0],
            pacman_coords[1] + 1 * entity.direction[1],
        )
        next_element_map = self.map.get_element_by_coords(next_coords)
        return next_element_map

    def collision_with_wall(self, entity=None):
        next_el = self.get_next_map_element(entity)
        if next_el == "#" or next_el == "-":
            return True
        else:
            return False

    def collision_pacman_with_dot(self):
        pacman_coords = self.pacman.get_coordinate()

        if (
            self.map.get_element_by_coords(pacman_coords) == "."
            or self.map.get_element_by_coords(pacman_coords) == "o"
        ):
            return True
        else:
            return False

    def can_rotate(self, entity=None, isGhost=False, direction=None):
        if entity is None:
            entity = self.pacman

        entity_coords = entity.get_coordinate()

        alternate = {
            "up": "down",
            "down": "up",
            "left": "right",
            "right": "left",
        }

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
            x, y = entity_coords
            next_coords = (x + dx, y + dy)

            element = self.map.get_element_by_coords(next_coords)

            result[dir_name] = element != "#" and element != "-"

        if isGhost:
            if direction is not None:
                if direction == "up" or direction == "down":
                    result["down"] = False
                    result["up"] = False
                elif direction == "left" or direction == "right":
                    result["right"] = False
                    result["left"] = False
            else:
                # result[entity.directionWord] = False
                result[alternate[entity.directionWord]] = False

        if direction is None:
            return result
        else:
            return result[direction]

    def collision_with_visor(self, ghost):
        pacman_coords = (self.pacman.x_coordinate, self.pacman.y_coordinate)

        ghost_coords = (ghost.x_coordinate, ghost.y_coordinate)

        visor_left = round(
            ghost_coords[0]
            - self.settings.SIZE / 2
            - math.floor(self.settings.ghost_overview / 2) * self.settings.SIZE
        )
        visor_right = visor_left + self.settings.ghost_overview * self.settings.SIZE
        visor_top = round(
            ghost_coords[1]
            - self.settings.SIZE / 2
            - math.floor(self.settings.ghost_overview / 2) * self.settings.SIZE
        )
        visor_down = visor_top + self.settings.ghost_overview * self.settings.SIZE

        if (
            pacman_coords[0] > visor_left
            and pacman_coords[0] < visor_right
            and pacman_coords[1] > visor_top
            and pacman_coords[1] < visor_down
        ):
            return True
        else:
            return False

    def collision_with_ghost(self):
        px, py = self.pacman.get_coordinate()

        if any(
            abs(gx - px) + abs(gy - py) <= 1
            for ghost in self.ghosts
            for gx, gy in [ghost.get_coordinate()]
        ):
            return True
        else:
            return False
