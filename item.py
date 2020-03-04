import pygame

from coords import Coords


class Item(pygame.sprite.Sprite):
    itemCount = 0

    fire_potion = 'sprites/fire_potion.png'
    water_potion = 'sprites/water_potion.png'
    ice_potion = 'sprites/ice_potion.png'

    def __init__(self, name, square):
        super().__init__()
        self._name = name
        self._square = square

        if self._name == "fire_potion":
            self._image = pygame.image.load(Item.fire_potion).convert_alpha()
        elif self._name == "water_potion":
            self._image = pygame.image.load(Item.water_potion).convert_alpha()
        elif self._name == "ice_potion":
            self._image = pygame.image.load(Item.ice_potion).convert_alpha()

    def drawAtSquare(self, screen):
        # adjust potions to the middle
        coords_adjusted_x = self._square.coords.x + 12
        coords_adjusted_y = self._square.coords.y + 12
        screen.blit(self._image, Coords(coords_adjusted_x, coords_adjusted_y).toArray())

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @staticmethod
    def displayCount():
        return Item.itemCount
