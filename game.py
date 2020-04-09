import pygame
import json
import sys
import os

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
		# pygame.mixer.init()
		pygame.font.init()
		pygame.display.set_caption("Chips")
		
		# game values
		self._LEVEL = None
		self._gameMap = None
		self._player = Player()
		
		#first goes to main menu, then loads game
		self.mainMenu()
  
	def resetValues(self):
		self._gameMap = None
		Chip.chipCount = 0

		player_username = self._player.username
		player_score = self._player._start_level_score

		self._player = Player()
		self._player.username = player_username
		self._player.start_level_score = player_score
		self._player.score = player_score

	def defineMap(self):
		
		path = 'resources/maps/' + str(self._LEVEL) + '.txt'
		try:
			file = open(path, 'r')
		except FileNotFoundError:
			sys.exit()

		self._gameMap = Map(self._LEVEL, self._player)
		self._player.gameMap = self._gameMap

		pygame.display.set_caption("Chips - Level " + str(self._LEVEL))

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
			self.printText(str(self._gameMap.time), Coords(700, 165))
			self.printText(str(Chip.chipCount), Coords(700, 245))

			if self._player.alive == False:
				self.gameOver()

			if self._gameMap.map_completed:
				break
				
			# *after* drawing everything, flip the display
			pygame.display.flip()
			
		self._LEVEL += 1
		self.defineMap()
	  
	def saveGame(self):
		filename = 'resources/game_data/save_files/' + self._player.username + '.json'
		filename_basename = os.path.basename(filename)
		folder_json_files = [f for f in os.listdir('resources/game_data/save_files') if f.endswith('.json')]
  
		data = {
			'username': self._player.username,
			'level': self._LEVEL,
			'score': self._player.start_level_score
		}
  
		# less than 3 savefiles, so we create file if not exists or rewrite if exists
		if len(folder_json_files) < 3 or filename_basename in folder_json_files:

			self.saveJson(filename, data)

		# 3 savefiles so we need to delete selected file and create a new one
		else:
			# deletes selected savefile and creates another one
			deleted_file_index = self.saveReplaceMenu(folder_json_files)
			os.remove('resources/game_data/save_files/' + folder_json_files[deleted_file_index])
			self.saveJson(filename, data)
	
	# returns index that identifies which file has to be replaced
	def saveReplaceMenu(self, folder_json_files):
		selected = False
		menu_selector = Coords(64,208)
  
		replace_menu = pygame.image.load("resources/game_images/replacesave.png").convert_alpha()
		selector = pygame.image.load("resources/game_images/selector.png").convert_alpha()
  
		names = [f.replace(".json", "") for f in folder_json_files]

		while not selected:
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP and menu_selector.y > 208:
						menu_selector.y -= 42
					if event.key == pygame.K_DOWN and menu_selector.y < 292:
						menu_selector.y += 42
					if event.key == pygame.K_RETURN:
						selected = True
			
			self._screen.blit(replace_menu, [64, 160])
			self.printText(names[0], Coords(140, 226))
			self.printText(names[1], Coords(140, 266))
			self.printText(names[2], Coords(140, 306))
			self._screen.blit(selector, menu_selector.toArray())
			pygame.display.flip()
   
		FILE_1 = 208
		FILE_2 = 250
		FILE_3 = 292

		if menu_selector.y == FILE_1:
			return 0
		elif menu_selector.y == FILE_2:
			return 1
		elif menu_selector.y == FILE_3:
			return 2

	def loadGame(self):

		savefiles = [f for f in os.listdir('resources/game_data/save_files') if f.endswith('.json')]
		names = [f.replace(".json","") for f in savefiles]
		number_of_savefiles = len(names)

		if number_of_savefiles < 3:
			for e in range(3 - number_of_savefiles):
				names.append("Empty savefile")

		menu_selector = Coords(192,304)
		selector_index = 0

		loadMenu = pygame.image.load("resources/game_images/load_save.png").convert_alpha()
		selector = pygame.image.load("resources/game_images/selector.png").convert_alpha()
		selected = False

		while not selected:
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP and menu_selector.y > 304 and names[selector_index - 1] != "Empty savefile":
						menu_selector.y -= 42
						selector_index -= 1
					if event.key == pygame.K_DOWN and menu_selector.y < 388 and names[selector_index + 1] != "Empty savefile":
						menu_selector.y += 42
						selector_index += 1
					if event.key == pygame.K_RETURN:
						selected = True
					if event.key == pygame.K_ESCAPE:
						self.mainMenu()

			self._screen.blit(loadMenu, [0,0])
			self._screen.blit(selector, menu_selector.toArray())
			self.printText("Press ESC to return to main menu", Coords(32,470))
			y = 330
			for name in names:
				self.printText(name, Coords(270,y))
				y += 40
			pygame.display.flip()

		FILE_1 = 304
		FILE_2 = 346
		FILE_3 = 388

		if menu_selector.y == FILE_1:
			filename = names[0]
		elif menu_selector.y == FILE_2:
			filename = names[1]
		elif menu_selector.y == FILE_3:
			filename = names[2]

		data = self.loadJson('resources/game_data/save_files/' + filename + '.json')
		self._LEVEL = data['level']
		self._player.username = data['username']
		self._player.score = data['score']

		self.defineMap()
			
	def saveJson(self, filename, data):
		with open(filename, 'w') as outfile:
			return json.dump(data, outfile, indent=4)

	def loadJson(self, file_route):
		with open(file_route) as json_file:
			return json.load(json_file)
 
	def printText(self, text, coords):
		font = pygame.font.SysFont("microsoftsansserif", 27)
		textsurface = font.render(text, False, (0,0,0))
		self._screen.blit(textsurface, coords.toArray())
		
	# PAUSE FUNCTIONS
	def pause(self):
		paused = True
		self._gameMap.pauseTimer()
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
			self.printText(str(self._player.score), Coords(700, 85))
			self.printText(str(self._gameMap.time), Coords(700, 165))
			self.printText(str(Chip.chipCount), Coords(700, 245))
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
			self._screen.blit(pygame.image.load("resources/game_images/score_background.png").convert_alpha(), [128, 128])
			for score in scores:
				line = str(i) + " - " + score[0] + ": " + str(score[1])
				self.printText(line, Coords(x, y))
				y += 64
				i += 1

			self.printText("ESC to return", Coords(x, 342))
			pygame.display.flip()

	def drawPauseMenu(self, selector_coords):
		pause = pygame.image.load("resources/game_images/pause.png").convert_alpha()
		selector = pygame.image.load("resources/game_images/selector.png").convert_alpha()
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
			self._gameMap.resumeTimer()
		if menu_selector.y == TOP_SCORES:
			self.printScore()
		if menu_selector.y == SAVE:
			self.saveGame()
		if menu_selector.y == EXIT:
			sys.exit()

		return paused
	# END OF PAUSE FUNCTIONS
	
	def mainMenu(self):

		# reset level to the first one when the player comes back to the main menu
		self._LEVEL = 1
		pygame.display.set_caption("Chips")

		selected = False
		selector_coords = Coords(256,256)
  
		NEW_GAME = 256
		LOAD_GAME = 320
		SCORES = 384

		while not selected:
			for event in pygame.event.get():
				# check for closing window
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.KEYDOWN:

					if event.key == pygame.K_RETURN:
						selected = True
					if event.key == pygame.K_UP and selector_coords.y > 256:
						selector_coords.y -= 64 
					if event.key == pygame.K_DOWN and selector_coords.y < 384:
						selector_coords.y += 64 

			self.drawMainMenu(selector_coords)
			pygame.display.flip()
   
		selected_menu_option = selector_coords.y
   
		if selected_menu_option == NEW_GAME:
			self._player.username = self.insertName()
			self.defineMap()
		elif selected_menu_option == LOAD_GAME:
			self.loadGame()
		elif selected_menu_option == SCORES:
			#function to load and print scores
			pass

	def drawMainMenu(self, selector_coords):
		menu = pygame.image.load('resources/game_images/main_menu.png').convert_alpha()
		selector = pygame.image.load("resources/game_images/selector.png").convert_alpha()
		self._screen.blit(menu,[0,0])
		self._screen.blit(selector, selector_coords.toArray())

	def drawInsertName(self, name):
		iname = pygame.image.load('resources/game_images/insert_name.png').convert_alpha()
		index = 0
		self._screen.blit(iname, [0,0])
		#print every char of name
		for ch in name:
			self.printText(ch.upper(), Coords(245 + index*64, 350))
			index += 1

	def insertName(self):
		inserted = False
		name = ["", "", "", "", "", ""]
		index = 0
		limit = False

		while not inserted:

			for event in pygame.event.get():
				# check for closing window
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						inserted = True
					elif event.key == pygame.K_BACKSPACE:
						if index > 0 and index <= 6:
							name[index-1] = ""
							index -= 1
						else:
							name[index] = ""
						 
					#between a-z ascii codes 
					elif event.key >= 97 and event.key <= 122:
						if index <= 5:
							name[index] = event.unicode
							index += 1

			self.drawInsertName(name)
			pygame.display.flip()

		return "".join(name).upper()

	def gameOver(self):
		self.resetValues()

		game_over = pygame.image.load('resources/game_images/game_over.png').convert_alpha()
		selector = pygame.image.load('resources/game_images/game_over_selector.png').convert_alpha()
  
		decided = False
		selector_coords = Coords(145, 335)

		while not decided:
			for event in pygame.event.get():
				# check for closing window
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT and selector_coords.x > 145:
						selector_coords.x -= 165
					if event.key == pygame.K_RIGHT and selector_coords.x < 310:
						selector_coords.x += 165
					if event.key == pygame.K_RETURN:
						decided = True

			self._screen.blit(game_over, [64, 64])
			self._screen.blit(selector, selector_coords.toArray())
			pygame.display.flip()

		RESET_LEVEL = 145
		MAIN_MENU = 310

		if selector_coords.x == RESET_LEVEL:
			self.defineMap()
		elif selector_coords.x == MAIN_MENU:
			self.mainMenu()
