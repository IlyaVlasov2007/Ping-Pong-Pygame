from GameSprite import *

class Ball(GameSprite):

    def __init__(self, x: int, y: int, texture: str, width: int, height: int, speed: float = 0):
        super().__init__(x, y, texture, width, height, speed)

        self.direction_x = 1
        self.direction_y = 1

    def update(self):
        self.rect.y += self.speed * self.direction_y
        self.rect.x += self.speed * self.direction_x

        self.speed *= 1.0005