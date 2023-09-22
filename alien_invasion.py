import sys
import pygame

from settings import Settings
from ikun import Kunkun
from ball import Ball

class AlienInvasion:
    """管理游戏资源和行为"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        self.settings=Settings()
        

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.kunkun=Kunkun(self)
        self.balls=pygame.sprite.Group()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                #检测按键事件并响应
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                #检测离键事件并响应
                self._check_keyup_events(event)
            

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            #向右移动
            self.kunkun.moving_right = True
        elif event.key == pygame.K_LEFT:
            #向左移动
            self.kunkun.moving_left = True
        elif event.key == pygame.K_UP:
            #向上移动
            self.kunkun.moving_up = True
        elif event.key == pygame.K_DOWN:
            #向下移动
           self.kunkun.moving_down = True
        elif event.key == pygame.K_SPACE:
            #发出球
            self._fire_ball()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            #停止向右移动
            self.kunkun.moving_right = False
        elif event.key == pygame.K_LEFT:
            #停止向左移动
            self.kunkun.moving_left = False
        elif event.key == pygame.K_UP:
            #向上移动
            self.kunkun.moving_up = False
        elif event.key == pygame.K_DOWN:
            #向下移动
            self.kunkun.moving_down = False

    def _fire_ball(self):
        #开火 创建一个球的实例
        if len(self.balls) <= self.settings.ball_maxnum:
            new_ball=Ball(self)
            self.balls.add(new_ball)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        #让最近绘制的屏幕可见
        self.kunkun.blitme()
        for ball in self.balls.sprites():
            ball.blitme()
        pygame.display.flip()

    def _update_balls(self):
        self.balls.update()
        for ball in self.balls.copy():
            if ball.rect.bottom <= 0:
                self.balls.remove(ball)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            #监视键盘和鼠标
            self._check_events()
            self.kunkun.update()
            self._update_balls()
            self._update_screen()
    
if __name__=='__main__':
    #创建游戏实例并运行游戏
    ai=AlienInvasion()
    ai.run_game()