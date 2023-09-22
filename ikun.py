import pygame

class Kunkun:
    """管理坤坤的类"""
    def __init__(self,aigame):
        """初始化坤坤并管理其位置"""
        self.screen=aigame.screen
        self.screen_rect=aigame.screen.get_rect()
        self.settings=aigame.settings

        #加载坤坤
        self.image=pygame.image.load("C:\\Users\\86182\\Desktop\\python_work\\alien_invation_game\\img\\ji1.bmp")
        self.rect=self.image.get_rect()

        #初始化位置
        self.rect.midbottom=self.screen_rect.midbottom

        #位置属性
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

        #移动属性
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """绘制坤"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """更新坤的状态"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x +=self.settings.kunkun_speed_x
        if self.moving_left and self.rect.left > 0:
            self.x -=self.settings.kunkun_speed_x
        self.rect.x=self.x

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y +=self.settings.kunkun_speed_y
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -=self.settings.kunkun_speed_y
        self.rect.y=self.y