import pygame


class Square(pygame.sprite.Sprite):
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
        super().__init__()
        self._item = item
        self._sprite = sprite
        self._sprite_type = sprite_type
        # Changing the image or the sprite type should execute this code to change the image I think

        if self._sprite_type == Square.NORMAL_SQUARE:
            self._image = pygame.image.load(Square.normal_square).convert_alpha()

        elif self._sprite_type == Square.WALL_SQUARE:
            self._image = pygame.image.load(Square.wall_square).convert_alpha()

        elif self._sprite_type == Square.WATER_SQUARE:
            self._image = pygame.image.load(Square.water_square).convert_alpha()

        elif self._sprite_type == Square.ICE_SQUARE:
            self._image = pygame.image.load(Square.ice_square).convert_alpha()

        elif self._sprite_type == Square.FIRE_SQUARE:
            self._image = pygame.image.load(Square.fire_square).convert_alpha()

    def isWalkable(self, player):
        if self._sprite_type == Square.NORMAL_SQUARE:
            return 1
        elif self._sprite_type == Square.WALL_SQUARE:
            return 0
        elif self._sprite_type == Square.WATER_SQUARE:
            # check for player item
            return 0
        elif self._sprite_type == Square.ICE_SQUARE:
            # check for player item
            return 0
        elif self._sprite_type == Square.FIRE_SQUARE:
            # check for player item
            return 0
        return 0

    @property
    def item(self):
        return self.item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def image(self):
        return self._image

    @property
    def sprite_type(self):
        return self._sprite_type

    @sprite_type.setter
    def sprite_type(self, sprite_type):
        self._sprite_type = sprite_type

    @staticmethod
    def displayCount():
        return Square.squareCount
