import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, gameMap):
        super().__init__()
        self._image = pygame.image.load('sprites/player.png').convert_alpha()
        self._items = []
        self._chips = []
        self._coords = None
        self._gameMap = gameMap
        self._score = 0
        self._username = None

    def drawAt(self, screen, coords):
        screen.blit(self._image, coords.toArray())

    def drawAtCurrentCoords(self, screen):
        screen.blit(self._image, self._coords.toArray())

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
    def items(self):
        return self._items

    @property
    def chips(self):
        return self._chips

    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self, coords):
        self._coords = coords
        
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username
        
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    @items.setter
    def items(self, items):
        self._items = items

    def addItem(self, item):
        self.items.append(item)
