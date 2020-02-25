import pygame


class Enemy(pygame.sprite.Sprite):

    def __init__(self, coords, gameMap):
        super().__init__()
        self._image = pygame.image.load('sprites/enemy.png').convert_alpha()
        self._coords = coords
        self._gameMap = gameMap

    def drawAt(self, screen, coords):
        screen.blit(self._image, coords.toArray())

    def moveUp(self):
        if self._gameMap.canMoveThere(self._coords.x, self._coords.y - 64, self):
            self._coords.y -= 64

    def moveDown(self):
        if self._gameMap.canMoveThere(self._coords.x, self._coords.y + 64, self):
            self._coords.y += 64

    def moveLeft(self):
        if self._gameMap.canMoveThere(self._coords.x - 64, self._coords.y, self):
            self._coords.x -= 64

    def moveRight(self):
        if self._gameMap.canMoveThere(self._coords.x + 64, self._coords.y, self):
            self._coords.x += 64

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image

    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self, coords):
        self._coords = coords
