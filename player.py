import pygame

from coords import Coords

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self._image = pygame.image.load('resources/sprites/player.png').convert_alpha()
        self._rect = self._image.get_rect()
        
        self._items = []
        self._chips = []
        self._gameMap = None
        self._score = 0
        self._start_level_score = 0
        self._username = None
        self._alive = True

    def drawAt(self, screen, coords):
        screen.blit(self._image, coords.toArray())

    def drawAtCurrentCoords(self, screen):
        screen.blit(self._image, self._rect)

    def moveUp(self):
        if self._gameMap.canMoveThere(self._rect.x, self._rect.y - 64, self):
            self._rect.y -= 64
            self.checkCollision()

    def moveDown(self):
        if self._gameMap.canMoveThere(self._rect.x, self._rect.y + 64, self):
            self._rect.y += 64
            self.checkCollision()

    def moveLeft(self):
        if self._gameMap.canMoveThere(self._rect.x - 64, self._rect.y, self):
            self._rect.x -= 64
            self.checkCollision()

    def moveRight(self):
        if self._gameMap.canMoveThere(self._rect.x + 64, self._rect.y, self):
            self._rect.x += 64
            self.checkCollision()
            
    def checkCollision(self):
        for enemy in self._gameMap.enemies:
            if self._rect.colliderect(enemy.rect):
                self._alive = False

    @property
    def image(self):
        return self._image
    
    @property
    def rect(self):
        return self._rect
    
    @rect.setter
    def rect(self, rect):
        self._rect = rect

    @image.setter
    def image(self, image):
        self._image = image

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

    @property
    def chips(self):
        return self._chips

    @chips.setter
    def chips(self, chips):
        self._chips = chips
    
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

    @property
    def start_level_score(self):
        return self._start_level_score

    @start_level_score.setter
    def start_level_score(self, start_level_score):
        self._start_level_score = start_level_score

    @property
    def alive(self):
        return self._alive

    @alive.setter
    def alive(self, alive):
        self._alive = alive
        
    @property
    def gameMap(self):
        return self._gameMap

    @gameMap.setter
    def gameMap(self, gameMap):
        self._gameMap = gameMap

    def addItem(self, item):
        self.items.append(item)
