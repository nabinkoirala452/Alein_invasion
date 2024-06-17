import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def fire_bullet(ai_settings, screen, ship, bullets,sound):
    """
    Fire a bullet if limit not reached yet.
    """
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        sound.play_sound_effect("bullet")


def check_keydown_events(event, ai_settings, screen, stats,sb, play_button, ship, aliens,bullets,sound):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key==pygame.K_SPACE:
       fire_bullet(ai_settings, screen, ship, bullets,sound)
    elif event.key == pygame.K_p and not stats.game_active:
        start_game(ai_settings, screen, stats,sb,play_button, ship, aliens, bullets)

    

def check_keyup_events(event, stats,ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_q:
            read_high_score(stats,"w")
            #why this elif doesnot work in check-events function
            """ he error message indicates that you're trying to access the key attribute on an pygame.event.
            Event object where it doesn't exist. This error commonly occurs because the event being processed 
            is not a keyboard event,so it doesn't have a key attribute.To fix this issue, we need to ensure that
            we're only attempting to access event.key when the event is indeed a keyboard event.
            We can do this by checking the event's type first."""
            sys.exit()

def check_events(ai_settings, screen, stats,sb,play_button,ship,aliens,bullets,sound):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            read_high_score(stats,"w")
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats,sb, play_button, ship, aliens,bullets,sound)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, stats,ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats,sb,play_button, ship, aliens, bullets, mouse_x, mouse_y)

            

def start_game(ai_settings, screen, stats,sb,play_button, ship, aliens, bullets):
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True 
        
        # Reset the scoreboard images.
        sb.prep_images()
       # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def check_play_button(ai_settings, screen, stats,sb,play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        # Hide the mouse cursor.
        start_game(ai_settings, screen, stats,sb, play_button, ship, aliens, bullets)




def update_screen(ai_settings, screen,sb,stats, ship,aliens,bullets,play_button):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    #it will draw image to the screen speciefied by self.react
    ship.blitme()
    aliens.draw(screen)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Draw the score information.
    sb.show_score()
    # Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()
    

    
    # Make the most recently drawn screen visible.
    pygame.display.flip()


    
# functions.py

def update_bullets(ai_settings, screen,stats,sb,ship, aliens, bullets,sound):
    """
    Update position of bullets and get rid of old bullets.
    """
    # Update bullet positions.
    bullets.update()
    
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen,stats,sb, ship, aliens, bullets,sound)
    

def check_bullet_alien_collisions(ai_settings, screen,stats,sb, ship, aliens, bullets,sound):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        sound.play_sound_effect("explosion")
        for aliens in collisions.values():
            stats.score+=ai_settings.alien_points*len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
    
    # If all aliens are destroyed, remove existing bullets and create a new fleet.
    start_new_level(ai_settings,screen,ship,aliens,bullets,stats,sb)
       
        


    

# functions.py

def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

# functions.py

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)  # Assuming Alien class is defined somewhere
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * alien_height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    alien = Alien(ai_settings, screen) 
    # Determine the number of aliens in a row and number of rows.
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)  # Assuming this function is defined elsewhere
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
def update_aliens(ai_settings, sb,stats, screen, ship, aliens, bullets,sound):
    """Check if the fleet is at an edge, and then update the positions of all aliens in the fleet."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # Look for alien-ship collisions. 
    if pygame.sprite.spritecollideany(ship, aliens):
       ship_hit(ai_settings,sb,stats,screen,ship,aliens,bullets,sound)
    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, sb,stats, screen, ship, aliens, bullets,sound) 
    

def ship_hit(ai_settings,sb, stats, screen, ship, aliens, bullets,sound):

    """Respond to ship being hit by alien."""
    sound.play_sound_effect("ship")
    # Decrement ships_left.
    if stats.ships_left > 0:
        stats.ships_left -= 1
        
        #update scoreboard
        sb.prep_ships()
    
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
    
        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
    
        # Pause.
        sleep(1)
    else:
        sound.play_sound_effect("gameover")
        stats.game_active=False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, sb,stats, screen, ship, aliens, bullets,sound):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:

            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings,sb,stats, screen, ship, aliens, bullets,sound)
            break

def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def read_high_score(stats,mode):
    fp=open("highscore.txt",mode)
    if mode=="w":
        fp.write(str(stats.high_score))
    else:
        stats.high_score=int(fp.read())
    fp.close()

def start_new_level(ai_settings,screen,ship,aliens,bullets,stats,sb):
      if len(aliens) == 0:
        # If the entire fleet is destroyed, start a new level
        # Destroy existing bullets, speed up game, and create new fleet.
        bullets.empty()
        ai_settings.increase_speed()
         # Increase level.
        stats.level += 1 
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)


        






