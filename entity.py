import pygame
import math


class Entity:

    def __init__(self, settings):
        self.spawn_coords = (13, 23)
        self.settings = settings
        self.speed = settings.SIZE * 0.66

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

    def move(self):
        self.x_coordinate += self.speed * self.direction[0]
        self.y_coordinate += self.speed * self.direction[1]

        self.left = self.x_coordinate - self.settings.SIZE / 2
        self.top = self.y_coordinate - self.settings.SIZE / 2
        self.right = self.x_coordinate + self.settings.SIZE / 2
        self.bottom = self.y_coordinate + self.settings.SIZE / 2

    def rotate(self, direction):
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

    def get_coordinate(self):
        return (
            math.floor((self.x_coordinate) / self.settings.SIZE),
            math.floor((self.y_coordinate) / self.settings.SIZE),
        )
