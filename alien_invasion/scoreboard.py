import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """显示得分信息的类"""
    def __init__(self,ai_settings,screen,stats):
        """初始化显示得分涉及的属性"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        # 准备包含最高得分,当前得分,等级的图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        # 剩下的飞船数量转换为渲染的图像
        self.prep_ship_left()
        # 用图像表示剩下的飞船
        self.prep_ships()

    def prep_ships(self):
        """显示还剩下多少搜飞船"""
        self.ships = Group()

        for ship_number in range(self.stats.ships_left):
            shipa = Ship(self.ai_settings,self.screen)
            shipa.rect.x = 10 + ship_number * shipa.rect.width
            shipa.rect.y = 10
            self.ships.add(shipa)

        print(self.ships)

    def prep_ship_left(self):
        """将剩下的飞船数量转换为一副渲染的图像"""
        self.ship_left_image = self.font.render(str(self.stats.ships_left),
            True,self.text_color,self.ai_settings.bg_color)

        # 将剩下的飞船数放在左上角
        self.ship_left_rect = self.ship_left_image.get_rect()
        self.ship_left_rect.left = self.screen_rect.left + 40
        self.ship_left_rect.top = 70


    def prep_score(self):
        """将得分转换为一副渲染的图像"""
        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,
            self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,
            True,self.text_color,self.ai_settings.bg_color)

        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.leve_image = self.font.render(str(self.stats.level),True,
            self.text_color,self.ai_settings.bg_color)
        
        # 将等级放在得分下方
        self.leve_rect = self.leve_image.get_rect()
        self.leve_rect.right = self.score_rect.right
        self.leve_rect.top = self.score_rect.bottom + 10


    def show_score(self):
        """在屏幕上显示得分和最高得分"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.leve_image,self.leve_rect)
        self.screen.blit(self.ship_left_image,self.ship_left_rect)
        self.ships.draw(self.screen)
    


