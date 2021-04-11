import pygame

from pysnake.game import Cell, Game
from pysnake.display.pygame import PygameDisplay

game = Game(40, 30)
display = PygameDisplay(900, 600, game)

clock = pygame.time.Clock()
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.snake.step_left()
            elif event.key == pygame.K_RIGHT:
                game.snake.step_right()
            elif event.key == pygame.K_UP:
                game.snake.step_up()
            elif event.key == pygame.K_DOWN:
                game.snake.step_down()
        game.refresh_board()
        display()
    clock.tick(30)

pygame.quit()
