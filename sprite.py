# class for the paddles
# https://www.101computing.net/pong-tutorial-using-pygame-adding-the-paddles/

import pygame

black = (0,0,0)


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()