# Pygame template - skeleton for a new pygame project
import pygame
import random
from player import Player
from square import Square
from map import Map

WIDTH = 832
HEIGHT = 576
FPS = 30

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chips")
clock = pygame.time.Clock()

gameMap = Map(3)
gameMap.loadMap()


# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                if gameMap.squareCheck(gameMap.player.position[0] - 64, gameMap.player.position[1]):
                    gameMap.player.position[0] = gameMap.player.position[0] - 64 

            if event.key == pygame.K_RIGHT:
                if gameMap.squareCheck(gameMap.player.position[0] + 64, gameMap.player.position[1]):
                    gameMap.player.position[0] = gameMap.player.position[0] + 64 

            if event.key == pygame.K_UP:
                if gameMap.squareCheck(gameMap.player.position[0], gameMap.player.position[1] - 64):
                    gameMap.player.position[1] = gameMap.player.position[1] - 64 
            if event.key == pygame.K_DOWN:
                if gameMap.squareCheck(gameMap.player.position[0], gameMap.player.position[1] + 64):
                    gameMap.player.position[1] = gameMap.player.position[1] + 64     

    # Draw / render
    gameMap.printMap(screen)
    
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
