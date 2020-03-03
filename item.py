import pygame


class Item(pygame.sprite.Sprite):
    itemCount = 0

    fire_potion = 'sprites/fire_potion.png'
    water_potion = 'sprites/water_potion.png'
    ice_potion = 'sprites/ice_potion.png'

    def __init__(self, name, square_coords):
        super().__init__()
        self._name = name
        self._square_coords = square_coords

        if self._name == "fire_potion":
            self._image = pygame.image.load(Item.fire_potion).convert_alpha()
        elif self._name == "water_potion":
            self._image = pygame.image.load(Item.water_potion).convert_alpha()
        elif self._name == "ice_potion":
            self._image = pygame.image.load(Item.ice_potion).convert_alpha()

    def drawAtSquare(self, screen):
        screen.blit(self._image, self._square_coords.toArray())

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @staticmethod
    def displayCount():
        return Item.itemCount
