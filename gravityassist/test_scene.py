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
sc = Spacecraft('Test', 225, 450, 100, thrust_force = 1000, gas_level = 5000)
orbit = Orbit(200, 300, 0, 275, CW=False, orbit_period = 10.0)
planet = Planet('Test', mass = 1e16, orbit = orbit)

while not done:
        
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        sc.brakes = not sc.brakes
                        # print(sc.vel)
                elif event.type == pygame.KEYDOWN and event.key in [pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT]:
                        sc.thrust = True
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
        
        # Planet
        planet.move()
        pygame.draw.ellipse(screen, (100,100,100), pygame.Rect(planet.x-25, planet.y-25, 50, 50))
        
        # Orbit
        pygame.draw.ellipse(screen, (255,255,255), pygame.Rect(orbit.center_x-orbit.a, orbit.center_y-orbit.b, orbit.a*2, orbit.b*2), 1)
        
        # Update spacecraft positions 
        sc.refresh([planet])
        # print(sc.vel, sc.x, sc.y)
        print(sc.gas_level)

        pygame.draw.polygon(screen, color, [
                [sc.x, sc.y],
                [sc.x-25, sc.y+35],
                [sc.x+25, sc.y+35],
                ])
        if sc.thrust:
                if sc.thrust_direction == '+y':
                        pygame.draw.polygon(screen, (255, 100, 0), [
                                [sc.x, sc.y],
                                [sc.x-5, sc.y-10],
                                [sc.x+5, sc.y-10],
                                ])
                if sc.thrust_direction == '-y':
                        pygame.draw.polygon(screen, (255, 100, 0), [
                                [sc.x, sc.y+35],
                                [sc.x-5, sc.y+35+10],
                                [sc.x+5, sc.y+35+10],
                                ])
                if sc.thrust_direction == '-x':
                        pygame.draw.polygon(screen, (255, 100, 0), [
                                [sc.x-10, sc.y+35/2],
                                [sc.x-20, sc.y+35/2-5],
                                [sc.x-20, sc.y+35/2+5],
                                ])
                if sc.thrust_direction == '+x':
                        pygame.draw.polygon(screen, (255, 100, 0), [
                                [sc.x+10, sc.y+35/2],
                                [sc.x+20, sc.y+35/2-5],
                                [sc.x+20, sc.y+35/2+5],
                                ])
                
        # Update screen
        pygame.display.flip()
        clock.tick(FPS)
        
pygame.quit()

