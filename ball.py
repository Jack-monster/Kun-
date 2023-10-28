import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, aigame) :
        pygame.sprite.Sprite.__init__(self)
        self.screen=aigame.screen
        self.screen_rect=aigame.screen.get_rect()
        self.settings=aigame.settings

        img = pygame.image.load(self.settings.BALL_RES)
        self.image = pygame.transform.scale(img, (self.settings.SPRITE_SIZE_W, self.settings.SPRITE_SIZE_H))
        self.rect = self.image.get_rect()

        self.speedy = -5

        self.rect.midbottom = aigame.kunkun.rect.midtop

    def update(self):
        self.rect.y +=self.speedy
        if self.rect.bottom < 0:
            self.kill