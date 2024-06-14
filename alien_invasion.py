import pygame
from pygame.sprite import Group
from settings import Settings
from alien import Alien
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    # Make an alien.

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    bullets=Group()
    aliens = Group()
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship,aliens)





    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets) 
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
        gf.update_aliens(ai_settings, aliens)
        

run_game()
