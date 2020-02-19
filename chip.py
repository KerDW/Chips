import pygame


class Chip(pygame.sprite.Sprite):
    chipCount = 0

    def __init__(self, pos):
        super().__init__()
        self.pos = pos

    @property
    def pos(self):
        return self.pos

    @pos.setter
    def pos(self, pos):
        self.pos = pos

    def displayCount(self):
        return Chip.chipCount
