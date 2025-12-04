import pygame


class Pacman:
    spawn_coords = (13, 23)

    # pacman_coordinate: 0, map_coordinate: 0
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.speed = 2
        self.size = 25

        # self.map_coordinate = map_coordinate
        # self.pacman_coordinate = pacman_coordinate
        self.direction = "right"
        self.x_coordinate, self.y_coordinate = (
            self.spawn_coords[0] * settings.SIZE + settings.SIZE / 2,
            self.spawn_coords[1] * settings.SIZE + settings.SIZE / 2,
        )

    def draw_pacman(self):
        pygame.draw.circle(
            self.screen,
            (238, 210, 53),
            (self.x_coordinate, self.y_coordinate),
            self.size / 2,
        )

    def move_pacman(self):
        if self.direction == "right":
            self.x_coordinate += self.speed
        elif self.direction == "left":
            self.x_coordinate -= self.speed
        elif self.direction == "up":
            self.y_coordinate -= self.speed
        elif self.direction == "down":
            self.y_coordinate += self.speed

    def rotate_pacman(self, direction):
        self.direction = direction

    def get_coordinate_pacman():
        pass
