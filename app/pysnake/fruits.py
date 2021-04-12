from random import randint


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
