class Chip:
    chipCount = 0

    def __init__(self, pos):
        self.pos = pos

    def displayCount(self):
        return Chip.chipCount
