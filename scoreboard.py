import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """A class to report scoring information."""
    
    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the initial score image.
        self.prep_score()

        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    
    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1)) 
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
    
     # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score and levels to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)


    def prep_high_score(self):
        """Turn the high score into a rendered image."""
    
    # Round the high score to the nearest 10 and convert it to an integer
        high_score = int(round(self.stats.high_score, -1))
    
    # Format the high score with commas as thousands separators
        high_score_str = "{:,}".format(high_score)
    
    # Render the high score string as an image
        self.high_score_image = self.font.render(
        high_score_str, True, self.text_color, self.ai_settings.bg_color
    )
    
    # Get the rectangle for the high score image
        self.high_score_rect = self.high_score_image.get_rect()
    
    # Center the high score image horizontally at the top of the screen
        self.high_score_rect.centerx = self.screen_rect.centerx
    
    # Align the top of the high score rectangle with the top of the score rectangle
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image."""
    
    # Render the level as an image
        self.level_image = self.font.render(
        str(self.stats.level), True, self.text_color, self.ai_settings.bg_color
        )
    
    # Get the rectangle for the level image
        self.level_rect = self.level_image.get_rect()
    
    # Position the level image to the right of the score image
        self.level_rect.right = self.score_rect.right
    
    # Position the level image below the score image
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are left."""
    
    # Create an empty group to hold the ship instances
        self.ships = Group()
    
    # Loop through the number of ships left and create a ship instance for each
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
        
        # Position each ship horizontally with a small margin to the left
            ship.rect.x = 10 + ship_number * ship.rect.width
        
        # Position each ship vertically with a small margin from the top
            ship.rect.y = 10
        
        # Add the ship to the group
            self.ships.add(ship)


    


    
