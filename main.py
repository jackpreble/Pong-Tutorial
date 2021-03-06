#!/usr/bin/env/ python3
# Game
# Feb. 14, 2020
__author__ = 'Jack Pebble'

# https://www.101computing.net/pong-tutorial-using-pygame-getting-started/

import pygame
from sprite import Paddle
from ball import Ball
from random import randint

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

f = open("data.csv")


'''def opponent(): !!!! ( This was going to be the function that does what the code on Line 123 does)
    global b, ball

    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    alist = []
    blist = []

    loss = False

    if ball.rect.x > 700:
        loss = True

    if ball.is_collided_with(a): # https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame
        x1 = int(ball.rect.x)
        y1 = int(ball.rect.y)

        alist.clear()

        if x1 > 0:
            alist.append(x1)

        if y1 > 0:
            alist.append(y1)

    if ball.rect.x == 35:
        x2 = int(ball.rect.x)
        y2 = int(ball.rect.y)

        blist.clear()

        if x1 > 0:
            blist.append(x1)

        if y1 > 0:
            blist.append(y1)

    print(x1, x2, y1, y2)
    print(a, b)

            # creates equation of the line

           # m = (t - ball.rect.y)/(20 - ball.rect.x)

   # print(m)'''


def main():
    global carryOn, black, white, clock, size, screen, all_sprites_list, a, b, ball

    scoreA = 0
    scoreB = 0

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # https://stackoverflow.com/questions/26822175/pygame-if-event-type-pygame-keydown-typeerror-int-object-is-not-callable/26822211
                carryOn = False

        # move the left paddle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            a.moveUp(10)
        if keys[pygame.K_s]:
            a.moveDown(10)

        # replaced by AI
        '''if keys[pygame.K_UP]:
            b.moveUp(10)
        if keys[pygame.K_DOWN]:
            b.moveDown(10)'''

        # yes, this is the AI
        b.rect.y = ball.rect.y # Scurria gave me this idea

        off_screen = False

        all_sprites_list.update()

        if ball.rect.x >= 690:
            scoreA += 1
            off_screen = True
        if ball.rect.x <= 0:
            scoreB += 1
            off_screen = True
        if ball.rect.y >= 490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y <= 0:
            ball.velocity[1] = -ball.velocity[1]

        if pygame.sprite.collide_mask(ball, a) or pygame.sprite.collide_mask(ball, b):
            ball.bounce()

        if off_screen:
            ball.velocity[0] = -ball.velocity[0]
            ball.rect.x = 345
            ball.rect.y = 195

        screen.fill(black)
        pygame.draw.line(screen, white, [349,0], [349, 500], 5)
        all_sprites_list.draw(screen)

        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, white)
        screen.blit(text, (250, 10))
        text = font.render(str(scoreB), 1, white)
        screen.blit(text, (420, 10))

        pygame.display.flip()
        clock.tick(120)


if __name__ == "__main__":
    main()
    pygame.quit()
