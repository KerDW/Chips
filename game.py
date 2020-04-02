import pygame
import sys

from map import Map

class Game:

    def __init__(self):
        # game window values
        self._WIDTH = 832
        self._HEIGHT = 576
        self._FPS = 30
        self._clock = pygame.time.Clock()
        self._screen = None
        
        # initialize pygame and create window
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        pygame.display.set_caption("Chips")
        
        # game values
        self._LEVEL = 2
        self._gameMap = None
        self._player = None
        
        self.defineMap()
    
    def defineMap(self):
        
        path = 'resources/maps/' + str(self._LEVEL) + '.txt'
        try:
            file = open(path, 'r')
        except FileNotFoundError:
            sys.exit()
        mapSizeCoords = [int(i)*64 for i in file.readline().split(',')]

        self._screen = pygame.display.set_mode(mapSizeCoords)

        self._gameMap = Map(self._LEVEL)
        self._player = self._gameMap.player
        self._gameMap.loadMap()
        self._gameMap.loadEntities()
        
        self._LEVEL += 1
        self.gameLoop()

    def gameLoop(self):
        while True:
            # keep loop running at the right speed
            self._clock.tick(self._FPS)
            # Process input (events)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self._player.moveLeft()

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self._player.moveRight()

                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self._player.moveUp()

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self._player.moveDown()

                    if event.key == pygame.K_e:
                        self._gameMap.givePlayerSquareItem()

                    if event.key == pygame.K_ESCAPE:
                        #pause menu pops up
                        self._gameMap.pause(self._screen)

            # Draw / render
            self._gameMap.drawMapAndEntities(self._screen)

            if self._gameMap.map_completed:
                break

            # *after* drawing everything, flip the display
            pygame.display.flip()
            
        self.defineMap()
        
        
