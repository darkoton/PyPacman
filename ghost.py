import pygame
import math

from entity import Entity
import settings


class Ghost(Entity):

    def __init__(self, settings, screen):
        super().__init__(settings, (25, 5))

        self.screen = screen
        self.speed = settings.SIZE
        self.size = 25

        self.direction = [1, 0]
        self.color = (1, 120, 1)

        self.aggressivePoint = [21, 20]

        self.see_pacman = False
        self.see_pacman_color = (20, 200, 200, 100)

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

        # pygame.draw.circle(
        #     self.screen, "green", (self.x_coordinate, self.y_coordinate), 10
        # )

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

        visor_surf = pygame.Surface(
            (self.settings.WIDTH, self.settings.HEIGHT), pygame.SRCALPHA
        )

        pygame.draw.rect(
            visor_surf,
            self.see_pacman_color if self.see_pacman else (255, 0, 0, 100),
            pygame.Rect(
                round(
                    self.x_coordinate
                    - self.settings.SIZE / 2
                    - math.floor(self.settings.ghost_overview / 2) * self.settings.SIZE
                ),
                round(
                    self.y_coordinate
                    - self.settings.SIZE / 2
                    - math.floor(self.settings.ghost_overview / 2) * self.settings.SIZE
                ),
                self.settings.ghost_overview * self.settings.SIZE,
                self.settings.ghost_overview * self.settings.SIZE,
            ),
        )
        self.screen.blit(
            visor_surf,
            (0, 0),
        )

    def determine_directions(
        self,
        coords=None,
    ):
        if coords is None:
            coords = self.aggressivePoint

        x, y = self.get_coordinate()
        target_x, target_y = coords

        dx = target_x - x
        dy = target_y - y

        directions = []

        if abs(dx) > abs(dy):
            if dx >= 0:
                directions.append("right")
            else:
                directions.append("left")

            if dy >= 0:
                directions.append("down")
            elif dy < 0:
                directions.append("up")
        else:
            if dy >= 0:
                directions.append("down")
            else:
                directions.append("up")

            if dx >= 0:
                directions.append("right")
            elif dx < 0:
                directions.append("left")

        return directions
