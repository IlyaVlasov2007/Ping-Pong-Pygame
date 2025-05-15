from GameSprite import *

class Player(GameSprite):

    def __init__(self, x:int, y:int, texture:str, width:int, height:int,  pressed_btn:tuple[int, int], speed:int = 0):
        super().__init__(x, y, texture, width, height, speed)
        self.btn_up = pressed_btn[0]
        self.btn_down = pressed_btn[1]

    def up(self):
         self.rect.y -= self.speed

    def down(self):
        self.rect.y += self.speed

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[self.btn_up]: self.up()
        if keys[self.btn_down]: self.down()