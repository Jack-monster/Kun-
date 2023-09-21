import pygame

class Kunkun:
    """管理坤坤的类"""
    def __init__(self,aigame):
        """初始化坤坤并管理其位置"""
        self.screen=aigame.screen
        self.screen_rect=aigame.screen.get_rect()

        #加载飞船
        self.image=pygame.image.load("C:\\Users\\86182\\Desktop\\python_work\\alien_invation_game\\img\\ji1.bmp")
        self.rect=self.image.get_rect()

        self.rect.midbottom=self.screen_rect.midbottom

    def blitme(self):
        """绘制坤"""
        self.screen.blit(self.image,self.rect)
