import pygame

from entity import Entity


class Pacman(Entity):

    def __init__(self, settings, screen):
        super().__init__(settings)

        self.screen = screen
        self.speed = settings.SIZE
        self.size = 25

        self.direction = [1, 0]
        self.directionWord = "right"
        self.spawn_coords = (13, 23)

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
