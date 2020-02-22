import pygame

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

    # loads map from txt file located in /maps and generates a matrix with square objects
    def loadMap(self):

        tmp_map = []
        tmp_row = []

        path = 'maps/' + str(self.level) + '.txt'
        file = open(path, 'r')
        for line in file.readlines():
            tmp_map.append([int(i) for i in line.split(',')])

        for row in tmp_map:
            print(row)
            for square in row:
                print(square)
                r_sq = Square(1, 1, square)
                tmp_row.append(r_sq)
            self.level_map.append(tmp_row)
            tmp_row = []

    # prints map in screen
    def printMap(self, screen):
        x = y = 0
        for i in range(len(self.level_map)):
            for j in range(len(self.level_map[i])):
                screen.blit(self.level_map[i][j].image, (x, y))
                x += 64
            x = 0
            y += 64
        self._player.drawAtCurrentCoords(screen)

    # checks if player can access to given square
    def canMoveThere(self, x, y, player):

        x_npixels = len(self.level_map[0]) * 64
        y_npixels = len(self.level_map) * 64

        if x >= 0 and x <= x_npixels - 64 and y >= 0 and y <= y_npixels - 64:

            g_square = self.level_map[int(y/64)][int(x/64)]

            if g_square.isWalkable(player):
                return 1

        return 0
