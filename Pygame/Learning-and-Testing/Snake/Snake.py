
# pylint: disable = unused-variable
# pylint: disable = missing-function-docstring
# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-module-docstring
# pylint: disable = trailing-whitespace
# pylint: disable = trailing-newlines

import pygame

pygame.init()

window = pygame.display.set_mode((500,500))

pygame.display.set_caption("Snake")

# Parameters 

x = 250
y = 250

width = 25
height = 25

vel = 10

# Square
def greenSquare():
    green_square = pygame.draw.rect(window, (0,255,0), (x,y,width,height))
    return green_square

def redrawGameWindow():
    pygame.display.update()

# Mainloop

running = True

while running:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel

    redrawGameWindow()

    window.fill((0,0,0))

    greenSquare()

pygame.quit()










