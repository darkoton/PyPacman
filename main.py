import pygame
from settings import Settings  # noqa: F403
from game import Game


def main():
    pygame.init()
    settings = Settings()
    pygame.display.set_caption("Pacman")
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    game = Game(settings, screen)
    game.run()


if __name__ == "__main__":
    main()
