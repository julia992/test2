class Settings():
    """Class for save all options for game Alien Invasion."""

    def __init__(self):
        """Initilization options game."""
        #Settings screen
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (0, 0, 255)
        #Settings ship
        ship_speed_factor = 1.5
