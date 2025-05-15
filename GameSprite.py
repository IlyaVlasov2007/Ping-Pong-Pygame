import pygame

class GameSprite(pygame.sprite.Sprite):

    def __init__(self, x:int, y:int, texture:str, width:int, height:int, speed:int = 0):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(texture), (width, height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def draw(self, screen:pygame.display):
        screen.blit(self.image, self.rect)