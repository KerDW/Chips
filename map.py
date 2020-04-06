import json
import pygame
import time
import threading

from chip import Chip
from coords import Coords
from item import Item
from player import Player
from enemy import Enemy
from square import Square

class Map:

    def __init__(self, level, player):
        self._level = level
        self._squares = []
        self._player = player
        self._enemies = []
        self._map_completed = 0
        self._sidebar = pygame.image.load("resources/game_images/sidebar.png").convert_alpha()

        self._time = None
        self._timer_running = True
        # condition object, this allows us to pause and resume the timer thread
        self._timer_condition = threading.Condition()

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
            self._player.rect.x = data['player']['coordinates']["x"] 
            self._player.rect.y = data['player']['coordinates']["y"]
            self._player.start_level_score = self._player.score
            for item in data['items']:
                x = item['coordinates']['x']
                y = item['coordinates']['y']
                item_square = self._squares[int(y / 64)][int(x / 64)]

                item_square.item = Item(item['name'], item_square)
            for chip in data['chips']:
                x = chip['coordinates']['x']
                y = chip['coordinates']['y']
                chip_square = self._squares[int(y / 64)][int(x / 64)]
                chip_square.chip = Chip(chip['id'], chip_square)
            for enemy in data['enemies']:
                x = enemy['coordinates']['x']
                y = enemy['coordinates']['y']
                
                movementPattern = enemy['movementPattern']
                
                # try to get defined value in json else set to 0.75 by default
                movementSpeed = enemy.get('movementSpeed', 0.75) 
                
                enemy = Enemy(self, movementPattern, movementSpeed)
                enemy.rect.move_ip(x + 12 , y + 12)
                self._enemies.append(enemy)
                
            self._time = data.get('time', 300)
            
            thread = threading.Thread(target=self.startTimer)
            thread.setDaemon(True)
            
            thread.start()

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
        for enemy in self._enemies:
            enemy.drawAtCurrentCoords(screen)

        screen.blit(self._sidebar, (576, 0))
        # check if there are enemies on the map and then draw them

    def givePlayerSquareItem(self):

        x = self._player.rect.x
        y = self._player.rect.y

        current_square = self._squares[int(y / 64)][int(x / 64)]

        if current_square.hasItem:
            self._player.items.append(current_square.item)
            current_square.item = None

    # checks if player can access to given square
    def canMoveThere(self, x, y, entity):

        x_npixels = len(self._squares[0]) * 64
        y_npixels = len(self._squares) * 64

        if (x >= 0 and x <= x_npixels - 64) and (y >= 0 and y <= y_npixels - 64):

            target_square = self._squares[int(y / 64)][int(x / 64)]
            
            if type(entity) is Player:
                player = entity
            elif type(entity) is Enemy:
                enemy = entity
                if target_square.sprite_type == Square.NORMAL_SQUARE:
                    return 1
                else:
                    return 0

            # needs the player object to check for items
            if target_square.isWalkable(player):
                if target_square.hasChip:
                    player.chips.append(target_square.chip)
                    Chip.chipCount -= 1
                    player.score += 10
                    target_square.chip = None
                    if Chip.chipCount == 0:
                        self._map_completed = 1
                return 1

            return 0

        return 0
    
    # if the timer is not paused it will count down until it reaches 0
    # if the timer is paused the thread will be waiting to be resumed
    def startTimer(self):
        self._timer_condition.acquire()
        while self._time > 0:
            if self._timer_running == True:
                self._time -= 1
                time.sleep(1)
            else:
                self._timer_condition.wait()
        self._player.alive = False
        self._timer_condition.release()

    def pauseTimer(self):
        self._timer_running = False

    # resumes the timer and adds a second that is lost while pausing
    def resumeTimer(self):
        self._timer_condition.acquire()

        self._timer_running = True
        self._time += 1
        self._timer_condition.notify()

        self._timer_condition.release()

    @property
    def squares(self):
        return self._squares
    
    @property
    def enemies(self):
        return self._enemies
    
    @property
    def time(self):
        return self._time

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
