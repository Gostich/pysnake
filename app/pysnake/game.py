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
        self.snake = Snake(self)
        self.board = None
        self.clear_board()

    def clear_board(self):
        self.board = [
            [Cell() for _ in range(self.height)] for _ in range(self.width)
        ]

    def refresh_board(self):
        self.clear_board()
        self.board[self.snake.head_x][self.snake.head_y].status = Cell.SNAKE


class Snake:
    def __init__(self, game):
        self.game = game
        self.head_x, self.head_y = self._start_coordinates()

    def _start_coordinates(self):
        return int(self.game.width / 2), int(self.game.height / 2)
