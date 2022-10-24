import pygame

class Ship():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('../../../Desktop/project1/rocket_1.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_down and self.rect.down < self.screen_rect.down:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.up>0:
            self.y -= self.settings.ship_speed
        self.rect.y = self.y
    def blitme(self):
        self.screen.blit(self.image, self.rect)