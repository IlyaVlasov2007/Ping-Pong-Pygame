import pygame.constants

from Player import *
from Ball import *

import sys

WIDTH = 700
HEIGHT = 500
white = (255, 255, 255)

root = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping Pong')

player_width, player_height = 10, 100

player_left = Player(x=10, y=HEIGHT//2-player_height, speed=5, width=10, height=100,
                     texture="Assets/Textures/player_left.png",
                     pressed_btn=(pygame.constants.K_w, pygame.constants.K_s))

player_right = Player(x=WIDTH-player_width-10, y=HEIGHT//2-player_height, speed=5, width=10, height=100,
                      texture="Assets/Textures/player_right.png",
                      pressed_btn=(pygame.constants.K_UP, pygame.constants.K_DOWN))

ball = Ball(x=WIDTH//2, y=100, width=40, height=40, speed=3,
            texture="Assets/Textures/ball.png",)

FPS = 60

while True:
    pygame.draw.rect(root, white, (0, 0, WIDTH, HEIGHT))

    player_left.draw(root)
    player_right.draw(root)
    ball.draw(root)

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            sys.exit(0)

    if pygame.sprite.collide_rect(ball ,player_left) or pygame.sprite.collide_rect(ball ,player_right):
        ball.direction_x *= -1

    if ball.rect.top <= 0 or ball.rect.bottom >= HEIGHT:
        ball.direction_y *= -1

    player_left.update()
    player_right.update()
    ball.update()

    pygame.display.update()
    pygame.time.Clock().tick(FPS)
