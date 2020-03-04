import pygame
import sys

from map import Map

WIDTH = 832
HEIGHT = 576
FPS = 30
LEVEL = 2

# initialize pygame and create window
pygame.init()
pygame.mixer.init()

while True:

    path = 'resources/maps/' + str(LEVEL) + '.txt'
    try:
        file = open(path, 'r')
    except FileNotFoundError:
        break
    mapSizeCoords = [int(i)*64 for i in file.readline().split(',')]

    screen = pygame.display.set_mode(mapSizeCoords)
    pygame.display.set_caption("Chips")
    clock = pygame.time.Clock()

    gameMap = Map(LEVEL)
    player = gameMap.player
    gameMap.loadMap()
    gameMap.loadEntities()

    # Game loop
    while True:
        # keep loop running at the right speed
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.moveLeft()

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.moveRight()

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.moveUp()

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.moveDown()

                if event.key == pygame.K_e:
                    gameMap.givePlayerSquareItem()

        # Draw / render
        gameMap.drawMapAndEntities(screen)

        if gameMap.map_completed:
            break

        # *after* drawing everything, flip the display
        pygame.display.flip()

    LEVEL += 1
