
# pylint: disable = unused-variable
# pylint: disable = missing-function-docstring
# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-module-docstring
# pylint: disable = line-too-long
# pylint: disable = global-statement
# pylint: disable = trailing-whitespace

import pygame

pygame.init()

window = pygame.display.set_mode((500,480)) # The parameter of the window is a tuple that containts its width and height

pygame.display.set_caption("First Game")

# Character's skins

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]

walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

bg = pygame.image.load('bg.jpg')

char = pygame.image.load('standing.png')


clock = pygame.time.Clock()

# We have to set the characters parameters

x = 250
y = 400

width = 64
height = 64

vel = 10

# Jumping

isJump = False
jumpCount = 10

# Move right and left

right = False
left = False
walkCount = 0

# It's better to have all the stuff of drawing in function instead of the mainloop
def redrawGameWindow():
    global walkCount

    window.blit(bg, (0,0))
    # pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        window.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        window.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        window.blit(char, (x,y))

    pygame.display.update() 


# Mainloop
running = True

while running:
    clock.tick(27)

    # Quitting the game with the ESC key
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
    # Setting the keys
    keys = pygame.key.get_pressed()

    ## IMPORTANT! -- The (0,0) is on the top-left of the screen, on the bottom-right is (500,500) (In our case)
    # The "and" are for the character not exiting the screen
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        left = False
        right = True
    else:
        right = False
        left = False
        walkCount = 0

    # When we jump we do not want to to be able to move up and down
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
       
    else:
        if jumpCount >= -10:
            sign = 1
            if jumpCount < 0:
                sign = -1
            y -= (jumpCount**2) * 0.5 * sign
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()

pygame.quit()










