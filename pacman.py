import pygame
import math


class Pacman:
    spawn_coords = (13, 23)

    # pacman_coordinate: 0, map_coordinate: 0
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.speed = settings.SIZE
        self.size = 25

        # self.map_coordinate = map_coordinate
        # self.pacman_coordinate = pacman_coordinate
        self.direction = [1, 0]
        self.directionWord = "right"
        self.x_coordinate, self.y_coordinate = (
            self.spawn_coords[0] * settings.SIZE + settings.SIZE / 2,
            self.spawn_coords[1] * settings.SIZE + settings.SIZE / 2,
        )

        self.left = self.x_coordinate - self.settings.SIZE / 2
        self.top = self.y_coordinate - self.settings.SIZE / 2
        self.right = settings.WIDTH - self.x_coordinate + self.settings.SIZE / 2
        self.bottom = self.y_coordinate + self.settings.SIZE / 2

    def draw_pacman(self):
        pygame.draw.circle(
            self.screen,
            (238, 210, 53),
            (self.x_coordinate, self.y_coordinate),
            self.size / 2,
        )

        pygame.draw.circle(
            self.screen,
            (0, 0, 0),
            (
                self.x_coordinate + self.size / 4 * self.direction[0],
                self.y_coordinate + self.size / 4 * self.direction[1],
            ),
            4,
        )

    def move_pacman(self):
        self.x_coordinate += self.speed * self.direction[0]
        self.y_coordinate += self.speed * self.direction[1]

        self.left = self.x_coordinate - self.settings.SIZE / 2
        self.top = self.y_coordinate - self.settings.SIZE / 2
        self.right = self.x_coordinate + self.settings.SIZE / 2
        self.bottom = self.y_coordinate + self.settings.SIZE / 2

    def rotate_pacman(self, direction):
        self.directionWord = direction
        if direction == "right":
            self.direction[0] = 1
            self.direction[1] = 0
        elif direction == "left":
            self.direction[0] = -1
            self.direction[1] = 0
        elif direction == "up":
            self.direction[1] = -1
            self.direction[0] = 0
        elif direction == "down":
            self.direction[1] = 1
            self.direction[0] = 0

    def get_coordinate_pacman(self):
        return (
            math.floor((self.x_coordinate) / self.settings.SIZE),
            math.floor((self.y_coordinate) / self.settings.SIZE),
        )
