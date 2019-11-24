import configuration_reader as reader
import pygame

try:
    #path where maps are stored
    GAMES_PATH = reader.READER.MAPS
    #texture path
    TEXTURE_PATH = reader.READER.TEXTURES
    # size of 1 block in px. Assume blocks are squares
    BLOCK_SIZE = tuple(map(int, reader.READER.BLOCK_SIZE.split(",")))
except:
    raise SystemError()

PERSONNAGE_SIZE = (30, 30)
PERSONNAGE_DEFAULT_POS = (0,0)
MAXIMUM_VIEW = (5,5)
#for text
FONT = None
#direction
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3
MOVE_SIZE = 2

#FPS
FPS = 60

#window size
WINDOW_INFOS = None
WINDOW_SIZE = (500, 500)
WINDOW = None

def clearScreen():
    WINDOW.fill([0,0,0])