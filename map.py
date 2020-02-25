import pygame

import square
from coords import Coords
from player import Player
from square import Square


class Map:

    def __init__(self, level):
        self.level = level
        self.level_map = []
        self._player = Player(Coords(64, 64), self)

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        self._player = player

    # loads the map from the .txt file and generates a matrix with square objects
    def loadMap(self):

        temp_map = []
        temp_row = []

        path = 'resources/maps/' + str(self.level) + '.txt'
        file = open(path, 'r')
        for line in file.readlines():
            temp_map.append([int(i) for i in line.split(',')])

        for row in temp_map:
            print(row)
            for value in row:
                print(value)
                temp_square = Square(value)
                temp_row.append(temp_square)
            self.level_map.append(temp_row)
            temp_row = []

    # draws the map in the screen
    def drawMap(self, screen):
        x = y = 0
        for i in range(len(self.level_map)):
            for j in range(len(self.level_map[i])):
                screen.blit(self.level_map[i][j].image, (x, y))
                x += 64
            x = 0
            y += 64
        self._player.drawAtCurrentCoords(screen)

    def pickUpSquareItem(self):

        x = self._player.coords.x
        y = self._player.coords.y

        current_square = self.level_map[int(y/64)][int(x/64)]

        if current_square.hasItem:
            self._player.items.append(current_square.item)
            current_square.item = None

    # checks if player can access to given square
    def canMoveThere(self, x, y, player):

        x_npixels = len(self.level_map[0]) * 64
        y_npixels = len(self.level_map) * 64

        if (x >= 0 and x <= x_npixels - 64) and (y >= 0 and y <= y_npixels - 64):

            target_square = self.level_map[int(y/64)][int(x/64)]

            # needs the player object to check for items
            if target_square.isWalkable(player):
                return 1

            return 0

        return 0
