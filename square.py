class Square:
    squareCount = 0

    def __init__(self, pos, item):
        self.pos = pos
        self.item = item

    def displayCount(self):
        return Square.chipCount

    def hasItem(self):
        if self.item is not None:
            return self.item
        return None
