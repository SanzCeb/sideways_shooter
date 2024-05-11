class Settings:
    def __init__(self, ss_game):
        """Store the game settings of Sideways Shooter"""
        screen_rect = ss_game.screen.get_rect()
        
        # Screen settings
        self.screen_width, self.screen_height = screen_rect.size
        self.bg_color = (230, 230, 230)