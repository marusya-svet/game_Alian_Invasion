import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('../../../Desktop/project1/alian.bmp')
        self.rect = self.image.get_rect()

        self.rect.topright = self.screen_rect.topright

        self.y = float(self.rect.y)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <=0:
            return True

    def update(self):
        self.y += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.y = self.y