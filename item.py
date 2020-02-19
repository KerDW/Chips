class Item(pygame.sprite.Sprite):
    itemCount = 0

    def __init__(self, pos, name):
        self.pos = pos
        self.name = name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def pos(self):
        return self.pos

    @pos.setter
    def pos(self, pos):
        self.pos = pos

    def displayCount(self):
        return Item.itemCount
