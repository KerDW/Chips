import pygame
import threading
import time

class Enemy(pygame.sprite.Sprite):

    def __init__(self, gameMap, movementPattern, movementSpeed):
        super().__init__()
        self._image = pygame.image.load('sprites/virus.png').convert_alpha()
        self._rect = self._image.get_rect()
        
        self._gameMap = gameMap
        self._movementPattern = movementPattern
        self._movementSpeed = movementSpeed
        
        self._thread = threading.Thread(target=self.followMovementPattern, args=(movementPattern,))
        # daemon threads die when non daemon threads exit, what we want in this situation
        self._thread.setDaemon(True)
        
        self._thread.start()

    def drawAt(self, screen, coords):
        screen.blit(self._image, coords.toArray())

    def drawAtCurrentCoords(self, screen):
        screen.blit(self._image, self._rect)

    def moveUp(self):
        if self._gameMap.canMoveThere(self._rect.x, self._rect.y - 64, self):
            self._rect.y -= 64

    def moveDown(self):
        if self._gameMap.canMoveThere(self._rect.x, self._rect.y + 64, self):
            self._rect.y += 64

    def moveLeft(self):
        if self._gameMap.canMoveThere(self._rect.x - 64, self._rect.y, self):
            self._rect.x -= 64

    def moveRight(self):
        if self._gameMap.canMoveThere(self._rect.x + 64, self._rect.y, self):
            self._rect.x += 64
            
    def followMovementPattern(self, movements):
        # small sleep otherwise it bugs and skips the first movement
        time.sleep(0.001)
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
                    
                if self._rect.colliderect(self._gameMap.player.rect):
                    print('enemy collided with player')
                    print('player death')
                    
                time.sleep(self._movementSpeed)

    @property
    def image(self):
        return self._image
    
    @property
    def rect(self):
        return self._rect
    
    @property
    def thread(self):
        return self._thread
    
    @image.setter
    def image(self, image):
        self._image = image
        
    @property
    def movementPattern(self):
        return self._movementPattern

    @movementPattern.setter
    def movementPattern(self, movementPattern):
        self._movementPattern = movementPattern
        
    
