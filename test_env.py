import pygame
import os, sys
import math
import numpy as np
sys.path.append('./astron')
from game import *


############# LEVEL 1 #############

sc = Spacecraft('Test', mass = 100, thrust_force = 3000, gas_level = 1000)
orbit = Orbit(a=300, b=100, center_x=500*0.75, center_y=500*0.3, CW=True, angular_step = 2*np.pi/(200.0*60.0), progress = np.pi/2)
planet = Planet('Test', mass = 2e16, orbit = orbit)
level1 = GameScene(resolution = (500,500), sc=sc, planets=[planet], win_region = ([0,0], [0, 100]), win_velocity = 190.0,
                #    background = r'C:\Users\addym\Documents\Gravity Assists\astron\images\stars_1.jpg'
                   )

##################################

game = Game(scenes = [level1], fullscreen=False)
game.startGame()