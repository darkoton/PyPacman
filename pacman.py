import pygame

from entity import Entity
import math


class Pacman(Entity):

    def __init__(self, settings, screen):
        super().__init__(settings, (13, 23))

        self.screen = screen
        self.speed = settings.SIZE
        self.size = 25

        self.direction = [1, 0]

        self.mouth_max = math.pi / 4  # максимум — 45°
        self.mouth_min = math.pi / 16  # минимум — 11°
        self.mouth_angle = self.mouth_max
        self.mouth_speed = 0.03
        self.mouth_opening = False

    # Тут я зробив з допомогою ИИ
    def draw_pacman(self):
        r = self.size / 2
        self.mouth_angle = self.mouth_min + (self.mouth_max - self.mouth_min) * (
            0.5 + 0.5 * math.sin(pygame.time.get_ticks() * 0.01)
        )

        dx, dy = self.direction
        angle_center = math.atan2(dy, dx)

        # Создаём поверхность для Pac-Man с прозрачным фоном
        pacman_surf = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        center = (r, r)

        # Рисуем тело (жёлтый круг)
        pygame.draw.circle(pacman_surf, (238, 210, 53), center, r)

        # Рисуем рот как черный сектор (мягко)
        points = [center]
        num_points = 20  # больше точек = плавнее
        for i in range(num_points + 1):
            angle = (
                angle_center
                - self.mouth_angle
                + i * (2 * self.mouth_angle) / num_points
            )
            x = center[0] + r * math.cos(angle)
            y = center[1] + r * math.sin(angle)
            points.append((x, y))
        pygame.draw.polygon(pacman_surf, (0, 0, 0), points)

        # Рисуем на основном экране
        self.screen.blit(pacman_surf, (self.x_coordinate - r, self.y_coordinate - r))
