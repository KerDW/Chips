class Player:

    def __init__(self, pos):
        self.pos = pos
        self.items = []

    @property
    def pos(self):
        return self.pos

    @pos.setter
    def pos(self, pos):
        self.pos = pos

    @property
    def items(self):
        return self.items

    @items.setter
    def items(self, items):
        self.items = items

    def addItem(self, item):
        self.items.append(item)


