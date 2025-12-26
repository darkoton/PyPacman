import pygame


class Menu:
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.surface = pygame.Surface(
            (self.settings.WIDTH, self.settings.HEIGHT), pygame.SRCALPHA
        )

    def draw(self):
        self.surface.fill((0, 0, 0))
        rect_body = pygame.Rect(0, 0, self.settings.WIDTH, self.settings.HEIGHT)

        pygame.draw.rect(self.surface, pygame.Color(0, 0, 0, 255), rect_body)

        title_surface = self.settings.font["40"].render(
            "Pacman", False, (255, 255, 255)
        )
        title_size = title_surface.get_size()
        self.surface.blit(
            title_surface,
            (
                self.settings.WIDTH / 2 - title_size[0] / 2,
                self.settings.HEIGHT / 2 - title_size[1] * 3,
            ),
        )

        desc_surface = self.settings.font["20"].render(
            "Press Enter to play", False, (255, 255, 255)
        )
        desc_size = desc_surface.get_size()

        self.surface.blit(
            desc_surface,
            (
                self.settings.WIDTH / 2 - desc_size[0] / 2,
                self.settings.HEIGHT / 2 - desc_size[1],
            ),
        )

        pygame.draw.rect(
            self.surface, (255, 255, 255), pygame.Rect(100, 660, 80, 80), 4
        )
        pygame.draw.rect(
            self.surface, (255, 255, 255), pygame.Rect(100, 750, 80, 80), 4
        )
        pygame.draw.rect(self.surface, (255, 255, 255), pygame.Rect(10, 750, 80, 80), 4)
        pygame.draw.rect(
            self.surface, (255, 255, 255), pygame.Rect(190, 750, 80, 80), 4
        )

        self.surface.blit(
            self.settings.font["20"].render("w/↑", False, (255, 255, 255)),
            (110, 690),
        )

        self.surface.blit(
            self.settings.font["20"].render("←/a", False, (255, 255, 255)),
            (20, 780),
        )

        self.surface.blit(
            self.settings.font["20"].render("s/↓", False, (255, 255, 255)),
            (110, 780),
        )

        self.surface.blit(
            self.settings.font["20"].render("d/→", False, (255, 255, 255)),
            (200, 780),
        )

        self.surface.blit(
            self.settings.font["20"].render("Move", False, (255, 255, 255)),
            (100, 625),
        )

        pygame.draw.rect(
            self.surface, (255, 255, 255), pygame.Rect(300, 750, 260, 60), 4
        )

        self.surface.blit(
            self.settings.font["20"].render("Space", False, (255, 255, 255)),
            (375, 770),
        )

        self.surface.blit(
            self.settings.font["20"].render("Pause", False, (255, 255, 255)),
            (375, 720),
        )

        pygame.draw.rect(
            self.surface, (255, 255, 255), pygame.Rect(600, 750, 80, 80), 4
        )

        self.surface.blit(
            self.settings.font["20"].render("Esc", False, (255, 255, 255)),
            (610, 780),
        )

        self.surface.blit(
            self.settings.font["20"].render("Menu", False, (255, 255, 255)),
            (600, 720),
        )

        # title_surface = self.settings.font["40"].render(
        #     "Pacman", False, (255, 255, 255)
        # )
        # title_size = title_surface.get_size()
        # self.surface.blit(
        #     title_surface,
        #     (
        #         self.settings.WIDTH / 2 - title_size[0] / 2,
        #         self.settings.HEIGHT / 2 - title_size[1] * 3,
        #     ),
        # )

        self.screen.blit(self.surface, (0, 0))
