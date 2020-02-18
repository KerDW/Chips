class Square:
    squareCount = 0

    def __init__(self, pos, item, sprite):
        self.pos = pos
        self.item = item
        self.sprite = sprite

    def displayCount(self):
        return Square.chipCount

    def hasItem(self):
        return self.item
