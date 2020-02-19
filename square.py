import pygame
class Square:
    squareCount = 0

    normal_square = 'sprites/normal_square.png'
    wall_square = 'sprites/wall_square.png'
    water_square = 'sprites/water_square.png'
    ice_square = 'sprites/ice_square.png'
    fire_square = 'sprites/fire_square.png'
    s_type = None
    img = None


    def __init__(self, item, sprite, stype):
        #self.item = item
        self.sprite = sprite
        self.s_type = stype

        if(self.s_type == 0):
            self.img = pygame.image.load(self.normal_square)
        
        else:
            self.img = pygame.image.load(self.wall_square)

    @property
    def item(self):
        return self.item

    @item.setter
    def item(self, item):
        self.item = item

    def displayCount(self):
        return Square.chipCount

    def getImg(self):
        return self.img

    def hasItem(self):
        return self.item
