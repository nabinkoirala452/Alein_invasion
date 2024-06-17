import pygame
from pygame.sprite import Group
from settings import Settings
from alien import Alien
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button 
from scoreboard import Scoreboard
from sound import SoundManager


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    # Make an alien.
    sound=SoundManager(ai_settings.sounddict)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button=Button(ai_settings,screen,"Play")
    # Create an instance to store game statistics and create a scoreboard.

    stats=GameStats(ai_settings)
    gf.read_high_score(stats,"r")
    sb=Scoreboard(ai_settings,screen,stats)
    ship = Ship(ai_settings,screen)
    bullets=Group()
    aliens = Group()
    # Create the fleet of aliens. 
    gf.create_fleet(ai_settings, screen, ship,aliens)





    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,bullets,sound)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen,stats,sb, ship, aliens, bullets,sound)
            gf.update_aliens(ai_settings,sb,stats,screen,ship,aliens,bullets,sound)
        gf.update_screen(ai_settings,screen,sb,stats,ship,aliens,bullets,play_button)

run_game()
