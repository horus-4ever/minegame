import constants as const
import pygame
import os

#texture
PATH = "personnage.jpeg"
image = pygame.image.load(os.path.join(const.TEXTURE_PATH, PATH))
image = pygame.transform.scale(image, const.PERSONNAGE_SIZE)

class Personnage():

    def __new__(cls, position):
        obj = object.__new__(cls)
        obj.__class__.image = image
        return obj

    def __init__(self, position):
        self._position = position
        self.onlink = False

    def getPlayerPos(self, _map):
        """Return the matrix coordinates of the player."""
        x, y = _map._position
        px, py = self._position
        bx, by = const.BLOCK_SIZE
        dx, dy = (px - x) // bx, (py - y) // by
        return dx, dy

    def collide(self, obj):
        """Return wether you collide a block or not. If block isn't set as obstacle, then no collision."""
        #is the block an obstacle
        if not obj.isObstacle():
            return False
        #check with position
        x, y = self._position
        objx, objy = obj.position
        dx, dy = const.BLOCK_SIZE
        px, py = const.PERSONNAGE_SIZE
        flag = False
        if (x > objx and x < objx + dx) or (x + px > objx and x + px < objx + dx):
            if (y > objy and y < objy + dy) or (y + py > objy and y + py < objy + dy):
                return True
        return False

    def isOut(self, _map):
        """Return wether you are outside the _map or not."""
        x, y = self._position
        objx, objy = _map._position
        dx, dy = _map._pixel_size
        px, py = const.PERSONNAGE_SIZE
        #check the position
        if ((x >= objx) and (x + px) <= (objx + dx)) and ((y >= objy) and (y + py) <= (objy + dy)):
            return False
        return True

    def move(self, direction):
        """Move to the specific direction"""
        x, y = self._position
        if direction == const.UP:
            y -= const.MOVE_SIZE
        elif direction == const.DOWN:
            y += const.MOVE_SIZE
        elif direction == const.RIGHT:
            x += const.MOVE_SIZE
        elif direction == const.LEFT:
            x -= const.MOVE_SIZE
        self._position = (x, y)

    def draw(self, surface):
        surface.blit(self.getTexture(), self._position)

    def getTexture(self):
        return self.__class__.image
