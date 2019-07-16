import pygame
import os, sys
import math
sys.path.append('./astron')
from game import *


############# LEVEL 1 #############

sc = Spacecraft('test', 100, 1000, 10)
orbit = Orbit(100,100, 250, 250, angular_step = 3.14/2000)
planet = Planet('test', 1e14, orbit)
level1 = GameScene((500,500), sc, [planet], win_region = ([100,0], [400, 0]))

##################################


game = Game(scenes = [level1])
game.startGame()