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

    def step_left(self):
        self.head_x -= 1
        if self.head_x < 0:
            self.head_x = self.game.width - 1

    def step_right(self):
        self.head_x += 1
        if self.head_x >= self.game.width:
            self.head_x = 0

    def step_up(self):
        self.head_y -= 1
        if self.head_y < 0:
            self.head_y = self.game.height - 1

    def step_down(self):
        self.head_y += 1
        if self.head_y >= self.game.height:
            self.head_y = 0
