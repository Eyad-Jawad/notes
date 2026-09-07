# PyGame

import pygame obviously to use it

from pygame.locals import * to access constants

to start the pygame:

pygame.init()

and the screen:

x = pygame.display.set_mode((width, height))

then you need a while loop to update the display

to not make the system break use:

for event in pygame.event.get():

if event.type == pygame.QUIT:

and there a bunch of other, but as for keys we say:

event.key and then use it with pygame keys

pygame.quit()

sys.exit()

and inside the while loop say:

pygame.display.update()

you can change the name (title) of the window above in the code:

pygame.display.set_caption(’lol’)

you can set a ceiling to the speed of the game by using a clock:

x = pygame.time.Clock()

and them inside the while loop:

x.tick(the frame rate)

you can load an image by saying:

x = pygame.image.load(’name.png’)

and to load it say on a surface or a screen say:

screen.blit(x, coordinates)

to change the color of the screen say:

x.fill((255, 255, 255))

to draw a ball:

 pygame.draw.circle(screen, ball_color, ball_position, ball_radius)