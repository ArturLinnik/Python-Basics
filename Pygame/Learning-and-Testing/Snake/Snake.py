
# pylint: disable = unused-variable
# pylint: disable = missing-function-docstring
# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-module-docstring
# pylint: disable = trailing-whitespace
# pylint: disable = trailing-newlines

import pygame

pygame.init()

# Window parameters

window = pygame.display.set_mode((500,500))

pygame.display.set_caption("Snake")

# Character parameters 

x = 250
y = 250

width = 25 
height = 25

speed = 25

green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

# Snake

def snakeHead(color):
    snake_head = pygame.draw.rect(window, color, (x,y,width,height))
    
def redrawGameWindow():
    pygame.display.update()

# Axes

x_axis = True
y_axis = False
positive = True
negative = False

axis = x_axis
sign = positive

# Mainloop

running = True

while running:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Changes the movement direction

    if axis == x_axis and sign == positive and x < 500 - width:
        move = x
        move += speed
        x = move

    elif axis == x_axis and sign == negative and x > 0:
        move = x
        move -= speed
        x = move

    elif axis == y_axis and sign == positive and y > 0:
        move = y
        move -= speed
        y = move
        
    elif axis == y_axis and sign == negative and y < 500 - height:
        move = y
        move += speed
        y = move

    else:
        snakeHead(red)

    # Keys pressing

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        move = x
        axis = x_axis
        sign = negative

    if keys[pygame.K_RIGHT]:
        move = x
        axis = x_axis
        sign = positive

    if keys[pygame.K_UP] and y > 0:
        move = y
        axis = y_axis
        sign = positive

    if keys[pygame.K_DOWN]:
        move = y
        axis = y_axis
        sign = negative

    redrawGameWindow()

    window.fill((0,0,0))

    snakeHead(green)

pygame.quit()










