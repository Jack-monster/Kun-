import pygame
from math import sqrt
from settings import Settings
import ikun
import xiaoheizi
import myplatform
from random import randrange

class Game:    
    """管理游戏资源和行为"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        pygame.mixer.init()
        self.settings=Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Kunの复仇")

        self.all_sprites = pygame.sprite.Group()
        self.kunkun=ikun.Kunkun(self)
        

        self.kun_ontheground = False
        

        self.ground = myplatform.Platfrom(self,200,self.settings.screen_height-30,self.settings.screen_width-400,30)
        self.platforms = pygame.sprite.Group()
        self.platforms.add(self.ground)
        self.all_sprites.add(self.ground)
        
        self.mobs = pygame.sprite.Group()
        

        self.balls = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

        self.running = True

        self.font_name = pygame.font.match_font('KaiTi')

        self.mobs_Number = 3
        

    def new(self):
            #开始新游戏
            self.playSwich = randrange(0,2)
            self.score = 0
            self.mobs_Number = 3
            self.all_sprites.add(self.kunkun)
            for i in range(int(self.mobs_Number)):
                m = xiaoheizi.xiaoheizi(self)
                self.mobs.add(m)
                self.all_sprites.add(m)
            self.run_game()

    def run_game(self):
        """开始游戏的主循环"""
        self.playing = True
        while self.playing:
            self.clock.tick(self.settings.FPS)
            self.mobs_Number = int(sqrt(self.score) + 3)
            self.events()
            self.update()
            self.draw()

            
    def update(self):
        #更新


        keys = pygame.key.get_pressed()

        self.all_sprites.update()

        hits2 = pygame.sprite.spritecollide(self.kunkun,self.platforms,False)
        if hits2:
            self.kunkun.rect.bottom = hits2[0].rect.top
            self.kunkun.vel.y = 0
            self.kun_ontheground = True
        else:
            self.kun_ontheground = False

        hits3 = pygame.sprite.spritecollide(self.ground,self.mobs,False)
        if hits3:
            hits3[0].rect.bottom = self.ground.rect.top
            hits3[0].speedy = 0

        hits1 = pygame.sprite.spritecollide(self.kunkun,self.mobs,False)
        if hits1:
            timeNow=pygame.time.get_ticks()
            if self.playSwich == 1:
                self.kunkun.ngmSound.play()
            else:
                self.kunkun.niSound.play()
                pygame.time.delay(500)
                self.kunkun.meiSound.play()
                pygame.time.delay(500)
                self.kunkun.jiSound.play()
                pygame.time.delay(500)
                self.kunkun.jiSound.play()
                pygame.time.delay(500)
            self.kunkun.kill()
            for mob in self.mobs:
                mob.kill()
            self.playing = False

        hits0 = pygame.sprite.groupcollide(self.balls,self.mobs,True,True)
        for hit in hits0:
            newheizi = xiaoheizi.xiaoheizi(self)  
            newheizi.punch.play()
            self.all_sprites.add(newheizi)
            self.mobs.add(newheizi)
            self.score += 10

        if len(self.mobs) < self.mobs_Number:
            newheizi = xiaoheizi.xiaoheizi(self)  
            self.all_sprites.add(newheizi)
            self.mobs.add(newheizi)

    def events(self):
        #事件响应
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.kunkun.fire_ball()
                if event.key == pygame.K_SPACE:
                    self.kunkun.jump()

    def draw(self):
        #游戏循环中 绘制
        self.screen.fill(self.settings.bg_color)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score),30,(0,0,0),self.settings.screen_width/2,10)
        pygame.display.flip()

    def waitTostart(self):
        waiting = True
        while waiting:
            self.clock.tick(self.settings.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    waiting = False
                    self.playing = True

    def waitTostartover(self):
        waiting = True
        while waiting:
            self.clock.tick(self.settings.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        waiting = False
                        self.playing = True

    def show_start_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.draw_text("Kunの复仇",48,(0,0,0),self.settings.screen_width/2,self.settings.screen_height/4)
        self.draw_text("按键可玩",30,(0,0,0),self.settings.screen_width/2,self.settings.screen_height/2)
        self.draw_text("<-,->移动，上箭头发射篮球，空格跳跃",30,(0,0,0),self.settings.screen_width/2,3*self.settings.screen_height/4)
        pygame.display.flip()
        self.waitTostart()

    def show_gameover_screen(self):
        if not self.running:
            return
        self.screen.fill(self.settings.bg_color)
        self.draw_text("Ikun 阵亡!",48,(0,0,0),self.settings.screen_width/2,self.settings.screen_height/4)
        self.draw_text("您的得分为:"+str(self.score),30,(0,0,0),self.settings.screen_width/2,self.settings.screen_height/2)
        self.draw_text("按任意键重新开始复仇",30,(0,0,0),self.settings.screen_width/2,3*self.settings.screen_height/4)
        pygame.display.flip()
        self.waitTostartover()

    def draw_text(self,text,size,color,x,y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface,text_rect)

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_gameover_screen()

pygame.quit()