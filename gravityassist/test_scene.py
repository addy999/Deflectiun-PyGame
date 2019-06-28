import pygame
import sys
sys.path.append('./')
from assests import *
from utilities import *

pygame.init()

# Setup screen
screen = pygame.display.set_mode((500, 500))
screen.fill((0, 0, 0))

# Utilities 
done = False
clock = pygame.time.Clock()
color = (0, 128, 255)

# Assets
sc = Spacecraft('Test', 225, 450, 100, thrust_force = 1000)
orbit = Orbit(200, 50, 250, 250)
planet = Planet('Test', 250, 150, mass = 10000)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key in [pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT]:
                        sc.thrust = True
                        color = (255, 100, 0)
                        if event.key == pygame.K_DOWN:
                                sc.thrust_direction = '+y'
                        if event.key == pygame.K_UP:
                                sc.thrust_direction = '-y'
                        if event.key == pygame.K_RIGHT:
                                sc.thrust_direction = '-x'
                        if event.key == pygame.K_LEFT:
                                sc.thrust_direction = '+x'
                elif event.type == pygame.KEYUP and event.key in [pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT]:
                        sc.thrust = False
                        color = (0, 128, 255)
                        
        # Update spacecraft positions 
        sc.refresh()
        print(sc.vel, sc.x, sc.y)
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, color, pygame.Rect(sc.x, sc.y, 50, 50))
        
        # pygame.draw.ellipse(screen, (255,255,255), pygame.Rect(orbit.center_x-orbit.a, orbit.center_y-orbit.b, orbit.a*2, orbit.b*2), 1)
        
        # Update screen
        pygame.display.flip()
        clock.tick(FPS)
        
pygame.quit()

