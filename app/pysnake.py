import pygame

from pysnake.game import Cell, Game
from pysnake.display.pygame import PygameDisplay

game = Game(40, 30)
display = PygameDisplay(800, 600, game)

clock = pygame.time.Clock()
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.snake.head_x -= 1
            elif event.key == pygame.K_RIGHT:
                game.snake.head_x += 1
            elif event.key == pygame.K_UP:
                game.snake.head_y -= 1
            elif event.key == pygame.K_DOWN:
                game.snake.head_y += 1
        game.refresh_board()
        display()
    clock.tick(30)

pygame.quit()
