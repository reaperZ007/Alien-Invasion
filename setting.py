class Settings:
    """A class to store all setting for alien invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_hieght = 800
        self.bg_color = (230,230,230)

        # ship settings
        self.ship_speed = 1.5
       # self.ship_limit = 3
        # Bullwt settings
       # self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 7

        # Alien settings
      #  self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        #how quickly game speeds up
        self.speedup_scale = 1.1
        #how quickly the alien point value increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that changes throughout the game"""

        self.ship_limit = 3
        self.bullet_speed = 3.0
        self.alien_speed= 1.0
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        #scoring 
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien points value"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)