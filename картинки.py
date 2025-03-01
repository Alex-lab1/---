import pygame
import sys

pygame.init()

screen_width = 600
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Over")

fon = (0, 0, 255)

game_over = pygame.image.load('data/game_over.png').convert_alpha()

x = -game_over.get_width()
y = (screen_height - game_over.get_height())

speed = 200

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if x + game_over.get_width() < screen_width:
        dt = clock.tick(60) / 1000.0
        x += speed * dt

    screen.fill(fon)
    screen.blit(game_over, (x, y))
    pygame.display.flip()

# Завершение Pygame
pygame.quit()
sys.exit()
