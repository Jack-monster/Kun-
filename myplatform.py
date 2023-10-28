import pygame

class Platfrom(pygame.sprite.Sprite):
    def __init__(self,aigame,x,y,w,h) :
        super().__init__()
        self.game=aigame
        self.screen=aigame.screen
        self.screen_rect=aigame.screen.get_rect()
        self.settings=aigame.settings

        self.image = pygame.Surface((w,h))
        self.image.fill((0,255,0))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y