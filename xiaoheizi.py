import pygame
from random import randrange

class xiaoheizi(pygame.sprite.Sprite):
    def __init__(self, aigame):
        pygame.sprite.Sprite.__init__(self)

        self.screen=aigame.screen
        self.screen_rect=aigame.screen.get_rect()
        self.settings=aigame.settings

        img = pygame.image.load("game/img/lose.png").convert()
        self.image = pygame.transform.scale(img, (50, 50))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = randrange(self.settings.screen_width - self.rect.width)
        self.rect.y = randrange(-100,-40)
        self.speedy0 = randrange(1,5)
        self.speedy = self.speedy0
        self.speedx = randrange(-3,3)
        self.xiaoheizi_ontheground = False

        self.punch = pygame.mixer.Sound(self.settings.Punch_snd)

    def update(self):

        if self.rect.right > self.settings.screen_width - 199 or self.rect.left < 199:
            self.speedy = self.speedy0
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > self.settings.screen_height + 10:
            self.rect.x = randrange(self.settings.screen_width - self.rect.width)
            self.rect.y = randrange(-100,-40)
            self.speedy = randrange(1,5)
            self.speedx = randrange(-3,3)
        if self.rect.right > self.settings.screen_width or self.rect.left < 0:
            self.speedx = -self.speedx
            