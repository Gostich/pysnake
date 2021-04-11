from random import randint


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
        self.apples = [Apple(self)]

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


class Snake:
    START_LENGTH = 3

    def __init__(self, game):
        self.length = self.START_LENGTH
        self.game = game
        self.head_x, self.head_y = None, None
        self.coordinates = []
        self.new_coordinates(*self._start_coordinates())

    def _start_coordinates(self):
        return int(self.game.width / 2), int(self.game.height / 2)

    def clean_head(self, x, y):
        if x < 0:
            x = self.game.width - 1
        elif x >= self.game.width:
            x = 0
        if y < 0:
            y = self.game.height -1
        elif y >= self.game.height:
            y = 0
        return x, y

    def new_coordinates(self, x, y):
        if x == self.head_x and y == self.head_y:
            return
        self.head_x, self.head_y = x, y
        self.coordinates.append((x, y))
        if len(self.coordinates) > self.length:
            self.coordinates.pop(0)

        # check if there is an apple and if exists, eat it
        apple = self.game.get_apple(x, y)
        if apple:
            self.game.apples.remove(apple)
            self.length += 1
            self.game.apples.append(Apple(self.game))

    def step_left(self):
        x, y = self.clean_head(self.head_x-1, self.head_y)
        self.new_coordinates(x, y)

    def step_right(self):
        x, y = self.clean_head(self.head_x+1, self.head_y)
        self.new_coordinates(x, y)

    def step_up(self):
        x, y = self.clean_head(self.head_x, self.head_y-1)
        self.new_coordinates(x, y)

    def step_down(self):
        x, y = self.clean_head(self.head_x, self.head_y+1)
        self.new_coordinates(x, y)


class Apple:
    def __init__(self, game):
        self.game = game
        self.x, self.y = None, None
        self.set_coordinates()

    def set_coordinates(self):
        while True:
            x = randint(0, self.game.width-1)
            y = randint(0, self.game.height-1)
            if (x, y) not in self.game.snake.coordinates:
                self.x, self.y = x, y
                break
