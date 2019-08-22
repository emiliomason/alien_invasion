import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):  # inherits from Sprite
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ships current position"""
        super(Bullet, self).__init__()  # super to inherit properly from Sprite
        self.screen = screen

        # create a bullet rect at (0, 0) and the set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        # create the bullets rect, the bullet is not based on an image so need to build
        # the rect from scratch using the pygame.Rect() class
        # this class required the x/y co-ordinates of the rect and the height and width
        self.rect.centerx = ship.rect.centerx  # bullets center = ships center
        self.rect.top = ship.rect.top  # set bullet top to ship top for affect

        # store the bullets position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen"""
        # update the decimal position of the bullet.
        self.y -= self.speed_factor
        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
