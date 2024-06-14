class Settings():
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1250
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=1
        self.bullet_color=60,60,60
        self.bullet_width=3
        self.bullet_height=15
        self.bullets_allowed=3
        self.alien_speed_factor = 0.5
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_drop_speed=10
        self.fleet_direction = 1

    