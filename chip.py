import pygame


class Chip(pygame.sprite.Sprite):
    chipCount = 0

    def __init__(self, id, square):
        super().__init__()
        self._id = id
        self._square = square
        Chip.chipCount += 1

        self._image = pygame.image.load("sprites/chip.png").convert_alpha()

    def drawAtSquare(self, screen):
        screen.blit(self._image, [self._square.coords.x + 15,self._square.coords.y + 17])

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id
    
    
