import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load('IMG_3862.JPG')
pygame.display.set_icon(icon)


target_image = pygame.image.load("img/target.png")
target_width = 150
target_height = 195


target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)




running = True

while running:
    pass

pygame.quit()