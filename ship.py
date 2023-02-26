import pygame

from settings import Settings


class Ship():

    def __init__(self, settings: Settings, screen: pygame.Surface):
        self.screen = screen
        self.ai_settings = settings

        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (80, 100))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # self.rect.width *= 0.5
        # self.rect.height *= 0.5

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def update(self, speed=''):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += speed or self.ai_settings.ship_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= speed or self.ai_settings.ship_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)
