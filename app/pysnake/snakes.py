from pysnake.fruits import Apple
from pysnake.settings import WHITE


class Snake:
    COLOR = WHITE
    START_LENGTH = 3

    def __init__(self, game):
        self.length = self.START_LENGTH
        self.game = game
        self.head_x, self.head_y = None, None
        self.coordinates = []
        self.new_coordinates(*self._start_coordinates())

    def _start_coordinates(self):
        return int(self.game.width / 2), int(self.game.height / 2)

    def clean_head_coordinates(self, x, y):
        if x < 0:
            x = self.game.width - 1
        elif x >= self.game.width:
            x = 0
        if y < 0:
            y = self.game.height - 1
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
        x, y = self.clean_head_coordinates(self.head_x-1, self.head_y)
        self.new_coordinates(x, y)

    def step_right(self):
        x, y = self.clean_head_coordinates(self.head_x+1, self.head_y)
        self.new_coordinates(x, y)

    def step_up(self):
        x, y = self.clean_head_coordinates(self.head_x, self.head_y-1)
        self.new_coordinates(x, y)

    def step_down(self):
        x, y = self.clean_head_coordinates(self.head_x, self.head_y+1)
        self.new_coordinates(x, y)
