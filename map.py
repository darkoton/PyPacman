import pygame


class Map:
    # # - стена
    # . - точка (еда)
    # o - энерджайзер (большая точка)
    # ' ' (пробел) - пустой проход
    # - - дверь дома призраков

    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        self.map = [
            "############################",
            "#............##............#",
            "#.####.#####.##.#####.####.#",
            "#o####.#####.##.#####.####o#",
            "#.####.#####.##.#####.####.#",
            "#..........................#",
            "#.####.##.########.##.####.#",
            "#.####.##.########.##.####.#",
            "#......##....##....##......#",
            "######.##### ## #####.######",
            "######.##### ## #####.######",
            "######.##          ##.######",
            "######.## ###--### ##.######",
            "######.## #      # ##.######",
            "      .   #      #   .      ",
            "######.## #      # ##.######",
            "######.## ######## ##.######",
            "######.##          ##.######",
            "######.## ######## ##.######",
            "######.## ######## ##.######",
            "#............##............#",
            "#.####.#####.##.#####.####.#",
            "#.####.#####.##.#####.####.#",
            "#o..##.......  .......##..o#",
            "###.##.##.########.##.##.###",
            "###.##.##.########.##.##.###",
            "#......##....##....##......#",
            "#.##########.##.##########.#",
            "#.##########.##.##########.#",
            "#..........................#",
            "############################",
        ]

        self.elements = {
            "#": lambda x, y: pygame.draw.rect(
                self.screen,
                (25, 30, 255),
                pygame.Rect(
                    self.settings.SIZE * x,
                    self.settings.SIZE * y,
                    self.settings.SIZE,
                    self.settings.SIZE,
                ),
            ),
            ".": lambda x, y: pygame.draw.circle(
                self.screen,
                (220, 165, 190),
                (
                    x * self.settings.SIZE + self.settings.SIZE / 2,
                    y * self.settings.SIZE + self.settings.SIZE / 2,
                ),
                3,
            ),
            "o": lambda x, y: pygame.draw.circle(
                self.screen,
                (220, 165, 190),
                (
                    x * self.settings.SIZE + self.settings.SIZE / 2,
                    y * self.settings.SIZE + self.settings.SIZE / 2,
                ),
                8,
            ),
            "-": lambda x, y: pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                pygame.Rect(
                    self.settings.SIZE * x,
                    self.settings.SIZE * y + self.settings.SIZE / 4,
                    self.settings.SIZE,
                    self.settings.SIZE / 2,
                ),
            ),
        }

    def draw_map(self):

        for y, row in enumerate(self.map):
            for x, symbol in enumerate(row):
                if symbol in self.elements:
                    self.elements[symbol](x, y)

                if self.settings.grid:
                    pygame.draw.rect(
                        self.screen,
                        (255, 0, 50),
                        pygame.Rect(
                            x * self.settings.SIZE,
                            y * self.settings.SIZE,
                            self.settings.SIZE,
                            self.settings.SIZE,
                        ),
                        1,
                    )
                    order = self.settings.font["6"].render(
                        f"{x},{y}", 1, (255, 255, 255)
                    )
                    self.screen.blit(
                        order, (x * self.settings.SIZE, y * self.settings.SIZE)
                    )

    def get_element_by_coords(self, coords):
        return self.map[coords[1]][coords[0]]

    def remove_item(self, coords):
        y = coords[1]
        x = coords[0]

        current_row = self.map[y]

        new_row = current_row[:x] + " " + current_row[x + 1 :]

        self.map[y] = new_row
