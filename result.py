import pygame


class Result:
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.surface = pygame.Surface(
            (self.settings.WIDTH, self.settings.HEIGHT), pygame.SRCALPHA
        )

    def draw(self, state="lose"):
        self.surface.fill((0, 0, 0))
        rect_body = pygame.Rect(0, 0, self.settings.WIDTH, self.settings.HEIGHT)

        pygame.draw.rect(self.surface, pygame.Color(0, 0, 0, 255), rect_body)

        result_surface = self.settings.font["40"].render(
            "Winner" if state == "win" else "Lose", False, (255, 255, 255)
        )
        result_size = result_surface.get_size()
        self.surface.blit(
            result_surface,
            (
                self.settings.WIDTH / 2 - result_size[0] / 2,
                self.settings.HEIGHT / 2 - result_size[1] * 3,
            ),
        )

        desc_surface = self.settings.font["20"].render(
            "Press Enter to restart", False, (255, 255, 255)
        )
        desc_size = desc_surface.get_size()

        self.surface.blit(
            desc_surface,
            (
                self.settings.WIDTH / 2 - desc_size[0] / 2,
                self.settings.HEIGHT / 2 - desc_size[1],
            ),
        )

        self.screen.blit(self.surface, (0, 0))
