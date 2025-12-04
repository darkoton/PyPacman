import pygame


class Devtools:
    def __init__(self, settings, screen, font):
        self.settings = settings
        self.screen = screen
        self.font = font
        self.surface = pygame.Surface((400, 200), pygame.SRCALPHA)

    def draw_info(self, items: list):
        self.surface.fill((0, 0, 0, 0))
        rect_body = pygame.Rect(0, 0, 400, 200)

        pygame.draw.rect(self.surface, pygame.Color(255, 255, 255, 150), rect_body)

        for index, item in enumerate(items):
            text_surface = self.font.render(item, True, (255, 0, 0))
            self.surface.blit(text_surface, (10, 10 + self.settings.FONT_SIZE * index))

        self.screen.blit(self.surface, (0, 0))
