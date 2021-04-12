import pygame

from pysnake.game import Cell
from pysnake.settings import BLACK, GRAY, RED, WHITE


class PygameDisplay:
    def __call__(self):
        for x, column in enumerate(self.game.board):
            for y, cell in enumerate(column):
                if cell.status == Cell.EMPTY:
                    cell_color = BLACK
                elif cell.status == Cell.SNAKE:
                    cell_color = WHITE
                elif cell.status == Cell.APPLE:
                    cell_color = RED
                pygame.draw.rect(
                    self.pygame_display,
                    cell_color,
                    self.get_coordinates(x, y)
                )
        pygame.display.update()

    def __init__(self, width, height, game):
        pygame.init()
        self.pygame_display = pygame.display.set_mode((width, height))
        self.pygame_display.fill(GRAY)
        self.game = game

    @property
    def cell_w(self):
        """cell width"""
        return min(
            self.pygame_display.get_height() / self.game.height,
            self.pygame_display.get_width() / self.game.width,
        )

    def get_coordinates(self, x, y):
        return x * self.cell_w, y * self.cell_w, self.cell_w, self.cell_w
