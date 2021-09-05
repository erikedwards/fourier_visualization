
import pygame
import math

# CONSTANTS
SCREEN_WIDTH = 1400
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
FONT = pygame.font.SysFont('Courier New', 30)
FONT_RGB = RED

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# init game values
circX = int(SCREEN_WIDTH / 6)
circY = int(SCREEN_HEIGHT / 2)
circScale = 150
wave = []
# waveX = int(SCREEN_WIDTH * (2/4))
waveX = circX
# waveY = int(SCREEN_HEIGHT / 2)
time = 0.00
timeStep = 0.005

# Main Loop
run = True

# max "N" to be evaluated. Not the same as number of terms to be evaluated
# maxN = 5, terms = 1, 3, and 5. Num terms = 3
# maxN = 11, terms = 1, 3, 5, 7, 9, 11. Num terms = 6
# num terms = (1/2)*(maxN + 1)
maxN = 5

# set frame rate
FR = 60

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                maxN += 2
            if event.key == pygame.K_DOWN and maxN > 2:
                maxN -= 2
            if event.key == pygame.K_RIGHT:
                if FR > 9:
                    FR += 10
                else:
                    FR += 1
            if event.key == pygame.K_LEFT:
                if FR > 19:
                    FR -= 10
                elif FR > 1:
                    FR -= 1


    # Game logic
    time += timeStep

    # Clear Screen
    screen.fill(WHITE)

    # show maxN (number of terms in series)
    maxN_String = "Num terms: " + str((maxN + 1) /2) + "  [UP/DOWN Arrows to change]"
    maxN_surf = FONT.render(maxN_String, True, FONT_RGB)
    nX = 20
    nY = SCREEN_HEIGHT - 80
    screen.blit(maxN_surf, (nX, nY))

    # show frame rate
    FR_String = "Frame rate: " + str(FR) + "  [LEFT/RIGHT Arrows to change]"
    FR_surf = FONT.render(FR_String, True, FONT_RGB)
    nX = 20
    nY = SCREEN_HEIGHT - 40
    screen.blit(FR_surf, (nX, nY))

    # --- draw wave CS
    rad = int(circScale * (4 / (1 * math.pi)))
    pygame.draw.line(screen, BLACK, [waveX, circY - rad], [waveX, circY + rad])
    pygame.draw.line(screen, BLACK, [waveX - 50, circY], [SCREEN_WIDTH, circY])
    #TODO --- add lines to Catia geoset "geom_drawAxis"

    x = circX
    y = circY
    for n in range(1, maxN +1, 2):
        prevX = x
        prevY = y
        rad = int(circScale * ( 4 / (n * math.pi)))
        x += int(rad * math.cos(n * time))
        y += int(-1 * rad * math.sin(n * time))
        # --- draw circle
        pygame.draw.circle(screen, BLACK, [prevX, prevY], rad, 1)
        pygame.draw.line(screen, RED, [prevX, prevY], [x, y])
        #TODO --- add circle and line to Catia geoset "geom_circularMotion"

    # Add y value of smallest circle to wave
    wave.insert(0, y)
    if len(wave) > 1300:
        wave.pop(-1)

    # --- draw wave
    for i in range(0, len(wave)):
        pX = int(waveX + i)
        pY = int(wave[i])
        pygame.draw.circle(screen, GREEN, [pX, pY], 1)
        #TODO --- add point to Catia geoset "geom_linearMotion-Sin(theta)"
    # --- draw connecting level line
    pygame.draw.line(screen, GREY, [x, y], [waveX, y])


    # --- Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(FR)

# Close the window and quit.
pygame.quit()

