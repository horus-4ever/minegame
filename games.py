import blocks
import constants as const
import personnage
import game_reader
import os
import random

class Map():

    def __init__(self, reader, position):
        """Class Map. There are different map : garden, house, ..."""
        self._size = reader.MAP_SIZE
        self._pixel_size = (self._size[0] * const.BLOCK_SIZE[0], self._size[1] * const.BLOCK_SIZE[1])
        self._position = position
        self.initMap(reader.MAP)
        self._personnage = personnage.Personnage(self._position)
        self._map_path = os.path.basename(reader._path)
        #case of linked map
        self._links = reader.LINKS

    def wasOnLink(self):
        """Return if player is already on a link"""
        result = self._personnage.onlink
        if self.onLink() is not None:
            self._personnage.onlink = True
        return result

    def resetDefault(self):
        """Reset all the default value of the map."""
        self._personnage._position = self._position

    def initMap(self, _map):
        """Create the map with block objects."""
        posx, posy = self._position
        for x, line in enumerate(_map):
            inter = []
            for y, obj in enumerate(line):
                #give the true position to the block object
                dx, dy = posx + (y * const.BLOCK_SIZE[1]), posy + (x * const.BLOCK_SIZE[0])
                to_set = blocks.ALL_BLOCKS[obj]((dx, dy))
                _map[x][y] = to_set
        #create the _map attributes
        self._map = _map

    def display(self, surface):
        """Display the whole map, with the character."""
        for x, line in enumerate(self._map):
            for y, obj in enumerate(line):
                #blit all blocks column by column
                obj.draw(surface)
        #display the character
        self._personnage.draw(surface)

    def onLink(self):
        """Return if the player is on a link."""
        if self._links is None:
            return None
        pos = self._personnage.getPlayerPos(self)
        for link in self._links:
            if pos == link[0]:
                return link[1]
        self._personnage.onlink = False
        return None

    def collide(self, fake):
        """Return wether the player collides a block or not"""
        for x, line in enumerate(self._map):
            for y, obj in enumerate(line):
                # blit all blocks column by column
                if fake.collide(obj):
                    return True
        return False

    def move(self, direction):
        """Try to move the character in the specific direction."""
        #create a false character
        x, y = self._personnage._position
        if direction == const.UP:
            y -= const.MOVE_SIZE
        elif direction == const.DOWN:
            y += const.MOVE_SIZE
        elif direction == const.RIGHT:
            x += const.MOVE_SIZE
        elif direction == const.LEFT:
            x -= const.MOVE_SIZE
        fake = personnage.Personnage((x, y))
        #collision ?
        if self.collide(fake):
            return
        #outside ?
        if fake.isOut(self):
            return
        self._personnage.move(direction)

def load_map(path, position):
    path = os.path.join(const.GAMES_PATH, path)
    reader = game_reader.MapReader(path)
    return Map(reader, position)

AVAIBLE_MAPS = [load_map(path, (50, 50)) for path in os.listdir(const.GAMES_PATH)]

def chooseRandomMap():
    return AVAIBLE_MAPS[2]
