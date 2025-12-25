import pygame
import math

from entity import Entity


class Ghost(Entity):

    def __init__(self, settings, screen):
        super().__init__(settings, (13, 11))

        self.screen = screen
        self.speed = settings.SIZE
        self.size = 25

        self.direction = [1, 0]
        self.directionWord = "right"
        self.color = (1, 120, 1)

        self.aggressivePoint = (50, -5)

    def draw_ghost(self):
        ghost_color = self.color

        pygame.draw.circle(
            self.screen,
            ghost_color,
            (self.x_coordinate, self.y_coordinate),
            self.size / 2,
        )

        body_height = self.size * 0.5
        num_waves = 4
        wave_width = self.size / num_waves

        points = []
        for i in range(num_waves + 1):
            if i % 2 == 0:
                points.append(
                    (
                        self.x_coordinate - self.size / 2 + i * wave_width,
                        self.y_coordinate + body_height,
                    )
                )
            else:
                points.append(
                    (
                        self.x_coordinate - self.size / 2 + i * wave_width,
                        self.y_coordinate + body_height - wave_width / 2,
                    )
                )

        pygame.draw.polygon(
            self.screen,
            ghost_color,
            [(self.x_coordinate - self.size / 2, self.y_coordinate)]
            + points
            + [(self.x_coordinate + self.size / 2, self.y_coordinate)],
        )

        eye_radius = self.size / 6
        pygame.draw.circle(
            self.screen,
            (255, 255, 255),
            (self.x_coordinate - self.size / 4, self.y_coordinate - self.size / 8),
            eye_radius,
        )
        pygame.draw.circle(
            self.screen,
            (255, 255, 255),
            (self.x_coordinate + self.size / 4, self.y_coordinate - self.size / 8),
            eye_radius,
        )

        pupil_radius = self.size / 12
        pygame.draw.circle(
            self.screen,
            (0, 0, 0),
            (
                self.x_coordinate - self.size / 4 + self.direction[0] * 2,
                self.y_coordinate - self.size / 8 + self.direction[1] * 2,
            ),
            pupil_radius,
        )
        pygame.draw.circle(
            self.screen,
            (0, 0, 0),
            (
                self.x_coordinate + self.size / 4 + self.direction[0] * 2,
                self.y_coordinate - self.size / 8 + self.direction[1] * 2,
            ),
            pupil_radius,
        )

        pygame.draw.rect(
            self.screen,
            self.color,
            pygame.Rect(
                self.aggressivePoint[0] * self.settings.SIZE,
                self.aggressivePoint[1] * self.settings.SIZE,
                self.settings.SIZE,
                self.settings.SIZE,
            ),
        )

    def determine_directions(self):
        x, y = self.get_coordinate()
        target_x, target_y = self.aggressivePoint

        dx = target_x - x
        dy = target_y - y

        directions = []

        # Основное направление — по большей разнице
        if abs(dx) > abs(dy):
            if dx > 0:
                directions.append("right")
            else:
                directions.append("left")

            # Второстепенное направление
            if dy > 0:
                directions.append("down")
            elif dy < 0:
                directions.append("up")
        else:
            if dy > 0:
                directions.append("down")
            else:
                directions.append("up")

            # Второстепенное направление
            if dx > 0:
                directions.append("right")
            elif dx < 0:
                directions.append("left")

        return directions
