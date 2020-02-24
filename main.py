#!/usr/bin/env/ python3
# Game
# Feb. 14, 2020
__author__ = 'Jack Pebble'

# https://www.101computing.net/pong-tutorial-using-pygame-getting-started/


import pygame
from sprite import Paddle
from ball import Ball

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

# Ball
ball = Ball(white, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(a, b, ball)

def main():
    global carryOn, black, white, clock, size, screen, all_sprites_list, a, b, ball

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # https://stackoverflow.com/questions/26822175/pygame-if-event-type-pygame-keydown-typeerror-int-object-is-not-callable/26822211
                carryOn = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            a.moveUp(10)
        if keys[pygame.K_s]:
            a.moveDown(10)
        if keys[pygame.K_UP]:
            b.moveUp(10)
        if keys[pygame.K_DOWN]:
            b.moveDown(10)


        all_sprites_list.update()

        if ball.rect.x >= 690:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <=0:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y >= 490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y <= 0:
            ball.velocity[1] = -ball.velocity[1]

        screen.fill(black)
        pygame.draw.line(screen, white, [349,0], [349, 500], 5)
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
    pygame.quit()
