from math import *
from random import *

import pygame as pg
from pygame.locals import *

from pytmx		 import *
from pytmx.util_pygame import load_pygame

#Tile size
TILE_SIZE = 16

#Window size
WINDOW_TILE_W = 21
WINDOW_TILE_H = 30
WINDOW_W = WINDOW_TILE_W * TILE_SIZE
WINDOW_H = WINDOW_TILE_H * TILE_SIZE

#Score offset
SCORE_OFF = TILE_SIZE * 2

#Colors
ALPHA_COLOR  = (34, 177, 76) #(255, 0, 255)
PINK 		 = (255, 0, 255)
BLACK 		 = (0, 0, 0)

from sprites import *
from text 	 import *
from actors	 import *
from maps	 import *

if __name__ == "__main__":
	print("This file is not supposed to be run directly.")