import pygame
from ball import Ball
from utils import *

vector2 = pygame.math.Vector2
class Kunkun(pygame.sprite.Sprite):
    """管理坤坤的类"""
    def __init__(self,aigame):
        pygame.sprite.Sprite.__init__(self)
        """初始化坤坤并管理其位置"""
        self.game=aigame
        self.screen=aigame.screen
        self.screen_rect=aigame.screen.get_rect()
        self.settings=aigame.settings
        
        #加载坤坤
        self.images = []
        self.imageIndex = 0
        for path in self.settings.PLAYER_RES:
            img = pygame.image.load(path)
            img = pygame.transform.scale(img, (self.settings.PLAYER_SIZE_W, self.settings.PLAYER_SIZE_H))
            self.images.append( img )
        self.image = self.images[self.imageIndex]
        self.rect=self.image.get_rect()

        self.preChangeTime = getCurrentTime()

        #速度
        self.pos = vector2(self.settings.screen_width/2,self.settings.screen_height*3/4)
        self.vel = vector2(0,0)
        self.acc = vector2(0.0)
        self.button_vel = True
        
        self.jiSound = pygame.mixer.Sound(self.settings.Ji_snd)
        self.ngmSound = pygame.mixer.Sound(self.settings.niganma_snd)
        self.meiSound = pygame.mixer.Sound(self.settings.mei_snd)
        self.niSound = pygame.mixer.Sound(self.settings.ni_snd)

    def fire_ball(self):
        self.jiSound.play()
        ball = Ball(self.game)
        self.game.balls.add(ball)
        self.game.all_sprites.add(ball)

    def jump(self):
        self.rect.y += 4
        hit = pygame.sprite.spritecollide(self,self.game.platforms,False)
        self.rect.y -= 4
        if hit:
            self.vel.y -= 15

    def update(self):
        """更新坤的状态"""
        self.image = self.images[self.imageIndex]

        if self.game.kun_ontheground:
            self.acc = vector2(0,0)
        else:
            self.acc = vector2(0,0.5)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -self.settings.kun_acc
        if keys[pygame.K_RIGHT]:
            self.acc.x = self.settings.kun_acc

        if getCurrentTime() - self.preChangeTime > 200:
            self.preChangeTime = getCurrentTime()
            self.imageIndex = (self.imageIndex + 1) % len(self.images)

        self.acc.x += self.vel.x * self.settings.kun_friction
        
        self.vel += self.acc

        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom= self.pos

        if self.rect.top > self.screen_rect.bottom:
            self.ngmSound.play()
            self.kill()
            for mob in self.game.mobs:
                mob.kill()
            self.game.playing = False

        
        
        
        
        