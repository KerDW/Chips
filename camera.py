import pygame

class Camera:
    def __init__(self, map_width, map_height):
        self._width = 832
        self._height = 512

        self.camera = pygame.Rect(0, 0, self._width, self._height)

        self._map_width = map_width
        self._map_height = map_height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(self._width / 2)
        y = -target.rect.y + int(self._height / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self._map_width - self._width), x)  # right
        y = max(-(self._map_height - self._height), y)  # bottom
        self.camera = pygame.Rect(x, y, self._map_width, self._map_height)