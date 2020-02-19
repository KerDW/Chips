import pygame
from square import Square

class Map(pygame.sprite.Sprite):

	level = 0
	level_map = []


	def __init__(self, level):
		self.level = level

	#loads map from txt file located in /maps and generates a matrix with square objects
	def loadMap(self):

		tmp_map = []
		tmp_row = []

		path = 'maps/' + str(self.level) + '.txt'
		file = open(path, 'r')
		for line in file.readlines():
			tmp_map.append([int (i) for i in line.split(',')])

		for row in tmp_map:
			print(row)
			for square in row:
				print(square)
				r_sq = Square(1, 1, square) 
				tmp_row.append(r_sq)
			self.level_map.append(tmp_row)
			tmp_row = []

	#prints map in screen
	def printMap(self, screen):
		x = y = 0
		for i in range(len(self.level_map)):
			for j in range(len(self.level_map[i])):
				screen.blit(self.level_map[i][j].getImg(), (x,y))
				x += 64
			x = 0
			y += 64
	

