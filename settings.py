class Settings:
    def __init__(self, ss_game):
        """Store the game settings of Sideways Shooter"""        
        # Screen settings
        self.screen_width, self.screen_height = ss_game.screen.get_size()
        self.bg_color = (230, 230, 230)

        # Bullet settings
        self.bullet_width, self.bullet_height = (15, 3)
        self.bullet_speed = 2.5
        self.bullet_color = (60, 60, 60)

        # Alien settings
        self.fleet_density = 0.5
        # Direction can be 1 or -1
        self.fleet_sideway_speed = 10

        # Ship settings
        self.max_ship_hit = 3

        # How quickly the game speeds up.
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.fleet_speed = 1.0

        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
    
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.fleet_speed *= self.speedup_scale