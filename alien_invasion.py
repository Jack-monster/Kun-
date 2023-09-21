import sys
import pygame

from settings import Settings
from ikun import Kunkun

class AlienInvasion:
    """管理游戏资源和行为"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        self.settings=Settings()
        

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.kunkun=Kunkun(self)

        
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            #监视键盘和鼠标
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            #让最近绘制的屏幕可见
            self.kunkun.blitme()
            pygame.display.flip()
    
if __name__=='__main__':
    #创建游戏实例并运行游戏
    ai=AlienInvasion()
    ai.run_game()