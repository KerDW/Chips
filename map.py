import json

from chip import Chip
from coords import Coords
from item import Item
from player import Player
from square import Square


class Map:

    def __init__(self, level):
        self._level = level
        self._squares = []
        self._player = Player(self)
        self._map_completed = 0

    # loads the map from the .txt file and generates a matrix with square objects
    def loadMap(self):

        temp_map = []
        temp_row = []

        path = 'resources/maps/' + str(self._level) + '.txt'
        file = open(path, 'r')

        # skip first line, which is the map size we already used
        file.readline()

        for line in file.readlines():
            temp_map.append([int(i) for i in line.split(',')])

        for row in temp_map:
            for value in row:
                temp_square = Square(value)
                temp_row.append(temp_square)
            self._squares.append(temp_row)
            temp_row = []

    def loadEntities(self):
        with open('resources/entities/entities_' + str(self._level) + ".json") as json_file:
            data = json.load(json_file)
            self._player.coords = Coords(data['player']['coordinates']["x"], data['player']['coordinates']["y"])
            for item in data['items']:
                x = item['coordinates']['x']
                y = item['coordinates']['y']
                item_square = self._squares[int(y / 64)][int(x / 64)]

                # since the item is not at the center of the square
                # it might be a good idea to pass slightly modified coordinates to the item object
                item_square.item = Item(item['name'], item_square)
            for chip in data['chips']:
                x = chip['coordinates']['x']
                y = chip['coordinates']['y']
                chip_square = self._squares[int(y / 64)][int(x / 64)]
                chip_square.chip = Chip(chip['id'], chip_square)
            for enemy in data['enemies']:
                x = enemy['coordinates']['x']
                y = enemy['coordinates']['y']
                # WIP, but enemies will be an attribute for map considering they have movement, just like the player

    # draws the map in the screen
    def drawMapAndEntities(self, screen):
        x = y = 0
        for i in range(len(self._squares)):
            for j in range(len(self._squares[i])):
                temp_square = self._squares[i][j]
                temp_square.coords = Coords(x, y)
                screen.blit(temp_square.image, (x, y))
                if temp_square.hasItem:
                    temp_square.item.drawAtSquare(screen)
                if temp_square.hasChip:
                    temp_square.chip.drawAtSquare(screen)
                x += 64
            x = 0
            y += 64
        self._player.drawAtCurrentCoords(screen)
        # check if there are enemies on the map and then draw them

    def givePlayerSquareItem(self):

        x = self._player.coords.x
        y = self._player.coords.y

        current_square = self._squares[int(y / 64)][int(x / 64)]

        if current_square.hasItem:
            self._player.items.append(current_square.item)
            current_square.item = None

    # checks if player can access to given square
    def canMoveThere(self, x, y, player):

        x_npixels = len(self._squares[0]) * 64
        y_npixels = len(self._squares) * 64

        if (x >= 0 and x <= x_npixels - 64) and (y >= 0 and y <= y_npixels - 64):

            target_square = self._squares[int(y / 64)][int(x / 64)]

            if target_square.hasChip:
                player.chips.append(target_square.chip)
                Chip.chipCount -= 1
                target_square.chip = None
                if Chip.chipCount == 0:
                    self._map_completed = 1

            # needs the player object to check for items
            if target_square.isWalkable(player):
                return 1

            return 0

        return 0

    @property
    def squares(self):
        return self._squares

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        self._player = player

    @property
    def map_completed(self):
        return self._map_completed

    @map_completed.setter
    def map_completed(self, map_completed):
        self._map_completed = map_completed

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level
