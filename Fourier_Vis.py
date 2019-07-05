
import pygame
import math

# CONSTANTS
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
circX = int(SCREEN_WIDTH / 4)
circY = int(SCREEN_HEIGHT / 2)
rad = 200

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# init pygame
pygame.init()
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Fourier Viz - a rad skillz joint")
FONT = pygame.font.SysFont('Courier New', 10)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

time = 0.00
timeStep = 0.01

# Main Loop
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # --- Game logic should go here
    time += timeStep
    x = rad * math.cos(time)
    y = -1 * rad * math.sin(time)


    # --- Screen-clearing code goes here
    screen.fill(WHITE)

    # --- Drawing code should go here
    pygame.draw.circle(screen, BLACK, [circX, circY], rad, 1)
    pygame.draw.line(screen, GREEN, [circX, circY], [circX + x, circY + y])


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(120)

# Close the window and quit.
pygame.quit()

