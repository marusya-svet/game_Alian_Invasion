class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (51, 102, 153)
        self.ship_speed = 2
        self.ship_limit = 3

        self.bullet_speed = 2
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        self.alien_speed = 1.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1