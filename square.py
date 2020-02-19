import pygame


class Square:
    squareCount = 0

    normal_square = 'sprites/normal_square.png'
    wall_square = 'sprites/wall_square.png'
    water_square = 'sprites/water_square.png'
    ice_square = 'sprites/ice_square.png'
    fire_square = 'sprites/fire_square.png'

    NORMAL_SQUARE = 0
    WALL_SQUARE = 1
    WATER_SQUARE = 2
    ICE_SQUARE = 3
    FIRE_SQUARE = 4


    def __init__(self, item, sprite, sprite_type):
        self._item = item
        self._sprite = sprite
        self._sprite_type = sprite_type

        # Changing the image or the sprite type should execute this code to change the image I think

        if self._sprite_type == NORMAL_SQUARE:
            self._image = pygame.image.load(self.normal_square)

        elif self._sprite_type == WALL_SQUARE:
            self._image = pygame.image.load(self.wall_square)

        elif self._sprite_type == WATER_SQUARE:
            self._image = pygame.image.load(self.water_square)

        elif self._sprite_type == ICE_SQUARE:
            self._image = pygame.image.load(self.ice_square)

        elif self._sprite_type == FIRE_SQUARE:
            self._image = pygame.image.load(self.fire_square)
        

    @property
    def item(self):
        return self.item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def sprite_type(self):
        return self._sprite_type

    @sprite.setter
    def sprite_type(self, sprite_type):
        self._sprite_type = sprite_type

    def displayCount(self):
        return Square.chipCount

