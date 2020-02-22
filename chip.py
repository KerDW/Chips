import pygame


class Chip(pygame.sprite.Sprite):
    chipCount = 0

    def __init__(self):
        super().__init__()

    @staticmethod
    def displayCount():
        return Chip.chipCount
