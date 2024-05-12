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