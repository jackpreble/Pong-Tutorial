#!/usr/bin/env/ python3
# Game
# Feb. 14, 2020
__author__ = 'Jack Pebble'

# https://www.101computing.net/pong-tutorial-using-pygame-getting-started/


import pygame
from sprite import Paddle

pygame.init()

black = (0,0,0)
white = (255,255,255)

carryOn = True

clock = pygame.time.Clock()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pong')

# Paddle 1
a = Paddle(white, 10, 100)
a.rect.x = 20
a.rect.y = 200

# Paddle 2
b = Paddle(white, 10, 100)
b.rect.x = 670
b.rect.y = 200

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(a, b)

def main():
    global carryOn, black, white, clock, size, screen, all_sprites_list

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # https://stackoverflow.com/questions/26822175/pygame-if-event-type-pygame-keydown-typeerror-int-object-is-not-callable/26822211
                carryOn = False

        all_sprites_list.update()

        screen.fill(black)
        pygame.draw.line(screen, white, [349,0], [349, 500], 5)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
    pygame.quit()
