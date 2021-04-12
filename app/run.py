import pygame

from pysnake.game import Game
from pysnake.display.pygame import PygameDisplay

MOVE_KEYS = [
    pygame.K_LEFT,
    pygame.K_RIGHT,
    pygame.K_UP,
    pygame.K_DOWN
]


def move_from_key(key):
    if key == pygame.K_LEFT:
        game.snake.step_left()
    elif key == pygame.K_RIGHT:
        game.snake.step_right()
    elif key == pygame.K_UP:
        game.snake.step_up()
    elif key == pygame.K_DOWN:
        game.snake.step_down()


game = Game(40, 30)
display = PygameDisplay(1200, 900, game)

clock = pygame.time.Clock()
last_key = None

game.refresh_board()
display()

game_over = False
while not game_over:
    move_keys = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            continue
        if event.type == pygame.KEYDOWN:
            if event.key in MOVE_KEYS:
                move_keys.append(event.key)
            if event.key == pygame.K_q:
                game_over = True
                continue

    if move_keys or last_key:
        if move_keys:
            for key in move_keys:
                move_from_key(key)
            last_key = move_keys[-1]
        else:
            move_from_key(last_key)

        game.refresh_board()
        display()
    clock.tick(10)

pygame.quit()
