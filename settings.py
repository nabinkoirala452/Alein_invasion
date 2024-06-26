class Settings():
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
    
        """Initialize the game's static settings."""
    # Screen settings
        self.screen_height = 600
        self.screen_width = 1250
        self.bg_color = (230, 230, 230)
    
        # Ship settings
        self.ship_limit = 3
    
    # Bullet settings
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

    # How quickly the alien point values increase 
        self.score_scale = 1.5

    
    # Alien settings
        self.fleet_drop_speed = 8
    
    # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.sounddict={'explosion':'sounds/alien.wav','bullet':'sounds/bullet.mp3',"ship":"sounds/ship.mp3","gameover":"sounds/gameover.mp3"}
    
    # Initialize dynamic settings
        self.initialize_dynamic_settings()

      # Shield properties
        self.shield_radius = 30  # Adjust the radius as needed
        self.shield_color = (0, 0, 255)  # Blue color for the shield
        self.shield_thickness = 3  # Thickness of the shield circle


    


    def initialize_dynamic_settings(self):

        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #scoring
        self.alien_points=50
    
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points=int(self.alien_points * self.score_scale)
        



        
    