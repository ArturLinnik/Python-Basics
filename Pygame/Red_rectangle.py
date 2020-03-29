
import pygame

pygame.init()

window = pygame.display.set_mode((500,500)) # The parameter of the window is a tuple that containts its width and height

pygame.display.set_caption("First Game")

# We have to set the characters parameters

x = 250
y = 250

width = 40
height = 60

vel = 10

# Jumping

isJump = False
jumpCount = 10

# Programming in the window

running = True

while running:
    pygame.time.delay(50)

    # Enabling the quit button (X)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False

    # Setting the keys
    keys = pygame.key.get_pressed()

    ## IMPORTANT! -- The (0,0) is on the top-left of the screen, on the bottom-right is (500,500) (In our case)
    # The "and" are for the character not exiting the screen
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel

    # When we jump we do not want to to be able to move up and down
    if not isJump:
       
        # Jumping key
        if keys[pygame.K_SPACE]:
            isJump = True
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

    # For the character to move without copying constantly its image
    window.fill((0,0,0))

    # Drawing a red rectangle
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))

    pygame.display.update() # Updates constantly the window



pygame.quit()










