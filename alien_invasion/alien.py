import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,ai_settings,screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人初始都在屏幕左上角附近(每个外星人的左边距设置为外星人的宽度，上边距为外星人的高度)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
            
    def update(self):
        """向左或者向右移动外星人"""
        self.x = self.x + (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
