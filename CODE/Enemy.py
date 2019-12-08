import pygame
import random
WHITE = (255, 255, 255)


class Enemy(pygame.sprite.Sprite):

    direction = 'right'
    UDdirection = 'down'
    alive = True

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.ellipse(self.image, color, [0, 0, width, height])

        # Instead we could load a proper pciture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.

        self.rect = self.image.get_rect()

        direction='left'

    def moveRight(self, rnd_low, rnd_high):
        self.rect.x += random.randint(rnd_low, rnd_high)

    def moveLeft(self, rnd_low, rnd_high):
        self.rect.x -= random.randint(rnd_low, rnd_high)

    def moveUp(self):
        self.rect.y -= random.randint(1, 20)

    def moveDown(self):
        self.rect.y += random.randint(1, 20)

    def moveDiagRightDown(self):
        self.rect.x += random.randint(1, 20)
        self.rect.y += random.randint(1, 20)

    def moveDiagRightUp(self):
        self.rect.x -= random.randint(1, 20)
        self.rect.y -= random.randint(1, 20)

    def moveDiagLeftDown(self):
        self.rect.x -= random.randint(1, 20)
        self.rect.y += random.randint(1, 20)

    def moveDiagLeftUp(self):
        self.rect.x -= random.randint(1, 20)
        self.rect.y -= random.randint(1, 20)
