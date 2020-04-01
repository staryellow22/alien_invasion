import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对飞船发射子弹进行管理的类"""

    def __init__(self,ai_settings,screen,ship):
        """在飞船所处的位置创建一个子弹对象"""
        # 初始化父类的属性，让子类的实例包含父类的所有属性
        super().__init__()
        self.screen = screen

        # 在（0，0）处创建一个表示子弹的钜行，再设置正确的位置
        # 从空白创建一个钜行，需提供钜行左上角的x和y坐标，还有钜行的宽度和高度
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
            ai_settings.bullet_height)
        # 将创建的钜行子弹放到合适的位置
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置，将子弹的y坐标存储为小数值，以便能微调子弹的速度
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y = self.y - self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)




