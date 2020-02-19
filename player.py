import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self._image = pygame.image.load('sprites/player.png').convert_alpha()
        # self.rect = self._image.get_rect()
        self._items = []

    def drawAt(self, screen, pos):
        screen.blit(self._image, pos)

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

    def addItem(self, item):
        self.items.append(item)
