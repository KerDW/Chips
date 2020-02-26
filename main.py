import pygame

from map import Map

WIDTH = 832
HEIGHT = 576
FPS = 30
LEVEL = 3

path = 'resources/maps/' + str(LEVEL) + '.txt'
file = open(path, 'r')
mapSizeCoords = [int(i)*64 for i in file.readline().split(',')]

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(mapSizeCoords)
pygame.display.set_caption("Chips")
clock = pygame.time.Clock()

gameMap = Map(LEVEL)
player = gameMap.player
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

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.moveLeft()

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.moveRight()

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.moveUp()

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.moveDown()

            if event.key == pygame.K_e:
                gameMap.pickUpSquareItem()

    # Draw / render
    gameMap.drawMap(screen)
    
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
