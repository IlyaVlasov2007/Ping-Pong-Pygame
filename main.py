from GameSprite import *

import sys

root = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Ping Pong')

FPS = 60

while True:

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            sys.exit(0)

    pygame.display.update()
    pygame.time.Clock().tick(FPS)
