import pygame


class Player(pygame.sprite.Sprite):


    def __init__(self, x, y):
        super().__init__()
        self._image = pygame.image.load('sprites/player.png').convert_alpha()
        # self.rect = self._image.get_rect()
        self._items = []
        self._position = [x,y]

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

    @property
    def position(self):
        return self._position
        
    @position.setter
    def position(self, x, y):
        self._position[0] = x
        self._position[1] = y

    @items.setter
    def items(self, items):
        self._items = items

    def addItem(self, item):
        self.items.append(item)
