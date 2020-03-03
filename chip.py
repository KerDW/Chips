import pygame


class Chip(pygame.sprite.Sprite):
    chipCount = 0

    def __init__(self, id):
        super().__init__()
        self._id = id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @staticmethod
    def displayCount():
        return Chip.chipCount
