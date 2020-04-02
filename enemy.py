import pygame
import threading
import time

class Enemy(pygame.sprite.Sprite):

    def __init__(self, coords, gameMap, movementPattern):
        super().__init__()
        self._image = pygame.image.load('sprites/enemy.png').convert_alpha()
        self._coords = coords
        self._gameMap = gameMap
        self._movementPattern = movementPattern
        
        self._thread = threading.Thread(target=self.followMovementPattern, args=(movementPattern,))
        
        self._thread.start()

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
            
    def followMovementPattern(self, movements):
        while True:
            for movement in movements:
                if movement == 'right':
                    self.moveRight()
                if movement == 'left':
                    self.moveLeft()
                if movement == 'up':
                    self.moveUp()
                if movement == 'down':
                    self.moveDown()
                time.sleep(1.0)

    @property
    def image(self):
        return self._image
    
    @property
    def thread(self):
        return self._thread
    
    @image.setter
    def image(self, image):
        self._image = image

    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self, coords):
        self._coords = coords
        
    @property
    def movementPattern(self):
        return self._movementPattern

    @movementPattern.setter
    def movementPattern(self, movementPattern):
        self._movementPattern = movementPattern
        
    
