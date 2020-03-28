
import pygame

pygame.init()

window = pygame.display.set_mode((500,500)) # The parameter of the window is a tuple that containts its width and height

pygame.display.set_caption("First Game")

# We have to set the characters parameters

x = 50
y = 50

width = 40
height = 60

vel = 5

# Programming in the window

running = True

while running:
    pygame.time.delay(100)

    # Enabling the quit button (X)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False

    # Setting the keys
    keys = pygame.key.get_pressed()

    ## IMPORTANT! -- The (0,0) is on the top-left of the screen, on the bottom-right is (500,500) (In our case)
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y +=vel

    # For the character to move without copying constantly its image
    window.fill((0,0,0))

    # Drawing a red rectangle
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))

    pygame.display.update() # Updates constantly the window



pygame.quit()










