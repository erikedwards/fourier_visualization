
import pygame
import math

# CONSTANTS
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

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

# init game values
circX = int(SCREEN_WIDTH / 4)
circY = int(SCREEN_HEIGHT / 2)
circScale = 150
wave = []
waveX = int(SCREEN_WIDTH * (2/4))
# waveY = int(SCREEN_HEIGHT / 2)
time = 0.00
timeStep = 0.005

# Main Loop
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Clear Screen
    screen.fill(WHITE)

    # Game logic
    time += timeStep

    # --- draw wave CS
    rad = int(circScale * (4 / (1 * math.pi)))
    pygame.draw.line(screen, BLACK, [waveX, circY - rad], [waveX, circY + rad])
    pygame.draw.line(screen, BLACK, [waveX - 50, circY], [SCREEN_WIDTH, circY])

    x = circX
    y = circY
    for n in range(1, 13, 2):
        prevX = x
        prevY = y
        rad = int(circScale * ( 4 / (n * math.pi)))
        x += int(rad * math.cos(n * time))
        y += int(-1 * rad * math.sin(n * time))
        # --- draw circle
        pygame.draw.circle(screen, BLACK, [prevX, prevY], rad, 1)
        pygame.draw.line(screen, GREEN, [prevX, prevY], [x, y])

    # Add y value of smallest circle to wave
    wave.insert(0, y)
    if len(wave) > 500:
        wave.pop(-1)

    # --- draw wave
    for i in range(0, len(wave)):
        pX = int(waveX + i)
        pY = int(wave[i])
        pygame.draw.circle(screen, GREEN, [pX, pY], 1)
    # --- draw connecting level line
    pygame.draw.line(screen, GREY, [x, y], [waveX, y])


    # --- Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(120)

# Close the window and quit.
pygame.quit()

