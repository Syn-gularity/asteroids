# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creates new screen with given parameters
    py_clock = pygame.time.Clock() # Initialize a Clock for clockspeed
    dt = 0

    while True:
        # Check for PlayerInput
        # Update World
        # Draw new state

        dt = py_clock.tick(60)
        dt /= 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()