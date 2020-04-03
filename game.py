import pygame
import json
import sys

from map import Map
from coords import Coords
from chip import Chip
from player import Player

class Game:

	def __init__(self):
		# game window values
		self._WIDTH = 832
		self._HEIGHT = 512
		self._FPS = 30
		self._clock = pygame.time.Clock()
		self._screen = pygame.display.set_mode((self._WIDTH, self._HEIGHT))
		
		# initialize pygame and create window
		pygame.init()
		pygame.mixer.init()
		pygame.font.init()
		pygame.display.set_caption("Chips")
		
		# game values
		self._LEVEL = 2
		self._gameMap = None
		self._player = Player()
		
		# define the map and start the game
		self.defineMap()
		
		# load game testing while we don't have a main menu
		# self.loadGame()
	
	def defineMap(self):
		
		path = 'resources/maps/' + str(self._LEVEL) + '.txt'
		try:
			file = open(path, 'r')
		except FileNotFoundError:
			sys.exit()
		# mapSizeCoords = [int(i)*64 for i in file.readline().split(',')]

		self._gameMap = Map(self._LEVEL, self._player)
		self._player.gameMap = self._gameMap
		self._gameMap.loadMap()
		self._gameMap.loadEntities()
		
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
						self.pause()

			# Draw / render
			self._gameMap.drawMapAndEntities(self._screen)
			self.printText(str(self._player.score), Coords(700, 85))
			self.printText(str(Chip.chipCount), Coords(700, 245))

			if self._gameMap.map_completed:
				break
				
			# *after* drawing everything, flip the display
			pygame.display.flip()
			
		self._LEVEL += 1
		self.defineMap()
	  
	def saveGame(self):
		data = {
			'username': self._player.username,
			'level': self._LEVEL,
			'score': self._player.score
		}

		with open('resources/save_files/savefile.json', 'w') as outfile:
			json.dump(data, outfile, indent=4)
			
	def loadGame(self):
		with open('resources/save_files/savefile.json') as json_file:
			data = json.load(json_file)
			
			self._LEVEL = data['level']
			self._player.username = data['username']
			self._player.score = data['score']
   
			self.defineMap()
			
	def printText(self, text, coords):
		font = pygame.font.SysFont("microsoftsansserif", 27)
		textsurface = font.render(text, False, (0,0,0))
		self._screen.blit(textsurface, coords.toArray())
		
	# PAUSE FUNCTIONS
	def pause(self):
		paused = True
		menu_selector = Coords(128, 128)
		while paused:
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP and menu_selector.y > 128:
						menu_selector.y -= 64
					if event.key == pygame.K_DOWN and menu_selector.y < 320:
						menu_selector.y += 64
					if event.key == pygame.K_RETURN:
						paused = self.executeMenuFunctionality(menu_selector, paused)
			
			self._gameMap.drawMapAndEntities(self._screen)
			self.drawPauseMenu(menu_selector)
			pygame.display.flip()

	def printScore(self):
		showing = True
		# dummy data
		scores = [["XBSK", 150], ["NIGG", 100], ["HIT", 75]]
		while showing:
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						showing = False
			x = 160
			y = 150
			i = 1
			self._screen.blit(pygame.image.load("sprites/score_background.png").convert_alpha(), [128, 128])
			for score in scores:
				line = str(i) + " - " + score[0] + ": " + str(score[1])
				self.printText(line, Coords(x, y))
				y += 64
				i += 1

			self.printText("ESC to return", Coords(x, 342))
			pygame.display.flip()

	def drawPauseMenu(self, selector_coords):
		pause = pygame.image.load("sprites/pause.png").convert_alpha()
		selector = pygame.image.load("sprites/selector.png").convert_alpha()
		# [64, 64] should be a variable with a proper name
		self._screen.blit(pause, [64, 64])
		self._screen.blit(selector, selector_coords.toArray())

	def executeMenuFunctionality(self, menu_selector, paused):

		RESUME = 128
		TOP_SCORES = 192
		SAVE = 256
		EXIT = 320

		if menu_selector.y == RESUME:
			paused = False
		if menu_selector.y == TOP_SCORES:
			self.printScore()
		if menu_selector.y == SAVE:
			print("Save functionality")
			self.saveGame()
		if menu_selector.y == EXIT:
			sys.exit()

		return paused
	# END OF PAUSE FUNCTIONS
