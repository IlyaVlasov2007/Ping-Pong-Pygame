import pygame.constants

from Player import *
from Ball import *

import sys

WIDTH = 700
HEIGHT = 500
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

root = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping Pong')

last_player = 0

player_width, player_height = 10, 100

player_left = Player(x=10, y=HEIGHT//2-player_height, speed=5, width=10, height=100,
                     texture="Assets/Textures/player_left.png",
                     pressed_btn=(pygame.constants.K_w, pygame.constants.K_s))

player_right = Player(x=WIDTH-player_width-10, y=HEIGHT//2-player_height, speed=5, width=10, height=100,
                      texture="Assets/Textures/player_right.png",
                      pressed_btn=(pygame.constants.K_UP, pygame.constants.K_DOWN))

ball = Ball(x=WIDTH//2, y=HEIGHT//2, width=40, height=40, speed=1.5,
            texture="Assets/Textures/ball.png",)

FPS = 60
lose = False

pygame.font.init()
font = pygame.font.SysFont("Droid Sans Mono", 30)

win_left_label = font.render("Left Won!", True, green)
win_right_label = font.render("Right Won!", True,  green)
draw_label = font.render("Draw!", True, red)

while True:
    pygame.draw.rect(root, white, (0, 0, WIDTH, HEIGHT))

    player_left.draw(root)
    player_right.draw(root)
    ball.draw(root)

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            sys.exit(0)

    if pygame.sprite.collide_rect(ball ,player_left):
        ball.direction_x *= -1
        last_player = -1
    elif pygame.sprite.collide_rect(ball ,player_right):
        ball.direction_x *= -1
        last_player = 1

    if ball.rect.top <= 0 or ball.rect.bottom >= HEIGHT:
        ball.direction_y *= -1

    if ball.rect.right <= 0 or ball.rect.left >= WIDTH:
        lose = True

    if not lose:
        player_left.update()
        player_right.update()
        ball.update()
    else:
        if last_player == 0:
            root.blit(draw_label, (WIDTH//2, HEIGHT//2))
        elif last_player == -1:
            root.blit(win_left_label, (WIDTH//2, HEIGHT//2))
        elif last_player == 1:
            root.blit(win_right_label, (WIDTH//2, HEIGHT//2))

    pygame.display.update()
    pygame.time.Clock().tick(FPS)
