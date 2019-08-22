import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    """initialize pygame, settings and screen object."""
    pygame.init()  # initialize background settings needed to work
    ai_settings = Settings()
    # make an instance of settings and store it in ai_settings
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # create display window
    # the screen object is called a surface. surface is a part of the
    # screen where you display a game element.
    pygame.display.set_caption('Alien Invasion')

    # make the play button
    play_button = Button(ai_settings, screen, 'Play')

    # create an instance to store game stats and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # make a ship, a group of bullets and a group of aliens
    ship = Ship(ai_settings, screen)
    # import and make an instance of the ship (must before the main
    # while loop so we don't make a new instance on each pass of the loop)
    # make a group for storing bullets
    bullets = Group()  # make an instance of group called bullets
    aliens = Group()

    # create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # make an alien
    # alien = Alien(ai_settings, screen)

    # start the main loop for the game.
    while True:

        gf.check_events(ai_settings, screen, stats, sb,  play_button, ship,
                        aliens, bullets)
        # check for player input

        if stats.game_active:
            ship.update()
            # updates the position of the ship
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # update the any fired bullets
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
            # update the aliens position after the bullets

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)
        # use new positions to draw a new screen


run_game()
