import pygame


class Chip(pygame.sprite.Sprite):
    chipCount = 0

    def __init__(self, id, square_coords):
        super().__init__()
        self._id = id
        self._square_coords = square_coords

        # self._image =

    # def drawAtSquare(self, screen, coords):
    #     screen.blit(self._image, coords.toArray())

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @staticmethod
    def displayCount():
        return Chip.chipCount
