import pygame


class Square(pygame.sprite.Sprite):
    squareCount = 0

    normal_square = 'resources/sprites/normal_square.png'
    wall_square = 'resources/sprites/wall_square.png'
    water_square = 'resources/sprites/water_square.png'
    ice_square = 'resources/sprites/ice_square.png'
    fire_square = 'resources/sprites/fire_square.png'
    void_square = 'resources/sprites/void_square.png'

    VOID_SQUARE = -1
    NORMAL_SQUARE = 0
    WALL_SQUARE = 1
    WATER_SQUARE = 2
    ICE_SQUARE = 3
    FIRE_SQUARE = 4

    def __init__(self, sprite_type):
        super().__init__()
        self._item = None
        self._chip = None
        self._coords = None
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

        elif self._sprite_type == Square.VOID_SQUARE:
            self._image = pygame.image.load(Square.void_square).convert_alpha()

    def isWalkable(self, player):
        if self._sprite_type == Square.NORMAL_SQUARE:
            return 1
        elif self._sprite_type == Square.WATER_SQUARE:
            if any(item.name == "water_potion" for item in player.items):
                return 1
            return 0
        elif self._sprite_type == Square.ICE_SQUARE:
            if any(item.name == "ice_potion" for item in player.items):
                return 1
            return 0
        elif self._sprite_type == Square.FIRE_SQUARE:
            if any(item.name == "fire_potion" for item in player.items):
                return 1
            return 0
        return 0

    @property
    def hasItem(self):
        return 1 if self._item is not None else 0

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self, coords):
        self._coords = coords

    @property
    def hasChip(self):
        return 1 if self._chip is not None else 0

    @property
    def chip(self):
        return self._chip

    @chip.setter
    def chip(self, chip):
        self._chip = chip

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
