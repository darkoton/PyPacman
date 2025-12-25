import math


class Entity:

    def __init__(self, settings, spawn_coords=(13, 23)):
        self.spawn_coords = spawn_coords
        self.settings = settings
        self.speed = settings.SIZE

        self.direction = [1, 0]
        self.directionWord = "right"
        self.x_coordinate, self.y_coordinate = (
            self.spawn_coords[0] * settings.SIZE + settings.SIZE / 2,
            self.spawn_coords[1] * settings.SIZE + settings.SIZE / 2,
        )

        self.left = self.x_coordinate - self.settings.SIZE / 2
        self.top = self.y_coordinate - self.settings.SIZE / 2
        self.right = self.settings.WIDTH - self.left - self.settings.SIZE
        self.bottom = self.settings.HEIGHT - self.top - self.settings.SIZE

    def move(self):
        self.x_coordinate += self.speed * self.direction[0]
        self.y_coordinate += self.speed * self.direction[1]

        self.left = self.x_coordinate - self.settings.SIZE / 2
        self.top = self.y_coordinate - self.settings.SIZE / 2
        self.right = self.settings.WIDTH - self.left - self.settings.SIZE
        self.bottom = self.settings.HEIGHT - self.top - self.settings.SIZE

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
