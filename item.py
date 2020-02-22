import pygame


class Item(pygame.sprite.Sprite):
    itemCount = 0

    def __init__(self, name):
        super().__init__()
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @staticmethod
    def displayCount():
        return Item.itemCount
