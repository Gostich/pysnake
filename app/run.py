import pygame

from pysnake.game import Game
from pysnake.display.pygame import PygameDisplay

MOVE_KEYS = [
    pygame.K_LEFT,
    pygame.K_RIGHT,
    pygame.K_UP,
    pygame.K_DOWN
]

game = Game(40, 30)
display = PygameDisplay(1200, 900, game)

clock = pygame.time.Clock()
last_key = None

game.refresh_board()
display()

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            continue
        if event.type == pygame.KEYDOWN:
            if event.key in MOVE_KEYS:
                last_key = event.key
            if event.key == pygame.K_q:
                game_over = True
                continue

    if last_key:
        if last_key == pygame.K_LEFT:
            game.snake.step_left()
        elif last_key == pygame.K_RIGHT:
            game.snake.step_right()
        elif last_key == pygame.K_UP:
            game.snake.step_up()
        elif last_key == pygame.K_DOWN:
            game.snake.step_down()

        game.refresh_board()
        display()
    clock.tick(10)

pygame.quit()
