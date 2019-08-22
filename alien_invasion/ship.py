import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """initialize the ship and set its starting position."""
        # two parameters, self reference and where we draw the ship
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')  # load image
        self.rect = self.image.get_rect()  # access rect attribute
        # allows elements to be treated as rectangles even they aren't
        # working with rect object, you can use the x/y coordinates of the
        # top, bottom, left and right edges as well as the center
        self.screen_rect = screen.get_rect()
        # storing the screen rectangle

        # start each new ship at the bottom centre of the screen.
        self.rect.centerx = self.screen_rect.centerx
        # when centering a game element use center, centerx or centery
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal value for the ships center.
        self.center = float(self.rect.centerx)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's position based on the movement flag"""
        # update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update the rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx
