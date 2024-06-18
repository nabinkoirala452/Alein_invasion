import pygame
import random
class Bomb():
    def __init__(self,screen):
        self.image=pygame.image.load('images/bomb.bmp')
        self.screen=screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.count=3
        self.reset_position()


    def reset_position(self):
        self.rect.x=random.randint(0,1250)
        self.rect.y=self.screen_rect.top
        self.y=float(self.rect.y)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
