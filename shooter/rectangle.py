import pygame
import sys

clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption("My Pygame")

screen_width = 800
screen_height = 600

rect_width = 100
rect_height = 200
rect_x = screen_width / 2 - rect_width / 2
rect_y = screen_height / 2 - rect_height / 2

screen = pygame.display.set_mode((screen_width, screen_height))

STEP = 10

while True:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and rect_y >= STEP:
                rect_y = rect_y - STEP
            if event.key == pygame.K_DOWN and rect_y <= screen_height - rect_height - STEP:
                rect_y += STEP #минус равно это тоже самое что rect_y -
            if event.key == pygame.K_LEFT and rect_x >= STEP:
                rect_x -= STEP
            if event.key == pygame.K_RIGHT and rect_x <= screen_width - rect_width - STEP:
                rect_x = rect_x + STEP


    screen.fill((0, 255, 255))
    pygame.draw.rect(screen, (192, 192, 192), (rect_x, rect_y, rect_width, rect_height))
    pygame.display.update()

    clock.tick(1)

