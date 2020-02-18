class Square:
    squareCount = 0

    def __init__(self, pos, item, sprite):
        self.pos = pos
        self.item = item
        self.sprite = sprite

    @property
    def item(self):
        return self.item

    @item.setter
    def item(self, item):
        self.item = item

    @property
    def pos(self):
        return self.pos

    @pos.setter
    def pos(self, pos):
        self.pos = pos

    def displayCount(self):
        return Square.chipCount

    def hasItem(self):
        return self.item
