
# pylint: disable = unused-variable
# pylint: disable = missing-function-docstring
# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-module-docstring
# pylint: disable = trailing-whitespace
# pylint: disable = trailing-newlines
# pylint: disable = wrong-import-order

import pygame
import random

pygame.init()

# Window parameters

window = pygame.display.set_mode((500,500))

pygame.display.set_caption("Snake")

# Character parameters 

x = 250
y = 250

width = 10 
height = 10

speed = 10

head_green = (76,187,23)
body_green = (79,121,66)
red_snack = (153,26,0)

# Snake

snake_head = [x,y]
snake_body = [[x,y], [x-width, y], [x-2*width, y]]

# Initial moving direction

direction = "RIGHT"
change = direction

# Snacks

def snack():

    random_number1 = random.randrange(0,500,10)
    random_number2 = random.randrange(0,500,10)

    approved_snack = False
    
    # For the snacks to don't appear on the snake

    while not approved_snack:

        my_snack = [random_number1, random_number2]

        if my_snack not in snake_body:
            my_snack_x = my_snack[0]
            my_snack_y = my_snack[1]
            approved_snack = True

        else:
            random_number1 = random.randrange(0,500,10)
            random_number2 = random.randrange(0,500,10)

    return my_snack_x, my_snack_y

# Initial snack

snack_x, snack_y = snack()

# Mainloop

running = True

while running:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                running = False

    # Keys pressing

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        change = "LEFT"

    if keys[pygame.K_RIGHT]:
        change = "RIGHT"

    if keys[pygame.K_UP]:
        change = "UP"

    if keys[pygame.K_DOWN]:
        change = "DOWN"

    # Changes the movement direction and prohibits going backwards

    if change == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    elif change == "LEFT" and direction != "RIGHT":
        direction = "LEFT"

    elif change == "UP" and direction != "DOWN":
        direction = "UP"
        
    elif change == "DOWN" and direction != "UP":
        direction = "DOWN"

    # Moves the snake and breaks if touches the border

    if direction == "RIGHT" and snake_head[0] < 500-width:
        snake_head[0] += speed

    elif direction == "LEFT" and snake_head[0] > 0:
        snake_head[0] -= speed

    elif direction == "UP" and snake_head[1] > 0:
        snake_head[1] -= speed
        
    elif direction == "DOWN" and snake_head[1] < 500-height:
        snake_head[1] += speed

    else:
        break

    # Breaks when head is touching body

    if snake_head in snake_body[1:]:
        break

    # Creates and deletes the body in the screen

    snake_body.insert(0, list(snake_head))
    snake_body.pop()

    window.fill((0,0,0))    # Black background

    # Snake's head

    pygame.draw.rect(window, head_green, (snake_head[0],snake_head[1], width, height))

    # Snake's body

    for index in snake_body[1:]:
        pygame.draw.rect(window, body_green, pygame.Rect(index[0], index[1], width, height))

    # Snacks

    if snack_x == snake_head[0] and snack_y == snake_head[1]:
        snack_x, snack_y = snack()
        pygame.draw.rect(window, red_snack, (snack_x, snack_y, width, height))
        snake_body.insert(0, list(snake_head))

    pygame.draw.rect(window, red_snack, (snack_x, snack_y, width, height))

    # Updating the screen

    pygame.display.update()

pygame.quit()













