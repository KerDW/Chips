import pygame


class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.pos = pos

    @property
    def pos(self):
        return self.pos

    @pos.setter
    def pos(self, pos):
        self.pos = pos


