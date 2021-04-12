from pysnake.fruits import Apple
from pysnake.snakes import Snake


class Cell:
    EMPTY = 0
    SNAKE = 1
    APPLE = 2

    def __init__(self):
        self.status = self.EMPTY


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = None
        self.clear_board()
        self.apples = []  # needed to instantiate Snake
        self.snake = Snake(self)
        self.apples = [Apple(self), Apple(self), Apple(self), Apple(self)]

    def get_apple(self, x, y):
        for apple in self.apples:
            if x == apple.x and y == apple.y:
                return apple
        return None

    def clear_board(self):
        self.board = [
            [Cell() for _ in range(self.height)] for _ in range(self.width)
        ]

    def refresh_board(self):
        self.clear_board()
        for apple in self.apples:
            self.board[apple.x][apple.y].status = Cell.APPLE
        for x, y in self.snake.coordinates:
            self.board[x][y].status = Cell.SNAKE
