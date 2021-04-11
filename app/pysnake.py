import pygame

pygame.init()
dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake game by Gosti (Edureka totorial)')

white = (255, 255, 255)
black = (0, 0, 0)

x1 = 300
y1 = 300

clock = pygame.time.Clock()

game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event)  # prints out all the actions that take place on the screen
        if event.type == pygame.QUIT:
            game_over = True

        x1_change = 0
        y1_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
        x1 += x1_change
        y1 += y1_change

        dis.fill(white)
        pygame.draw.rect(dis, black, [x1, y1, 10, 10])
        pygame.display.update()

        clock.tick(30)

pygame.quit()
