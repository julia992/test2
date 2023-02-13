import pygame

class Ship():

    def __init__(self, screen):
        """Initialiez the ship and creates its initial position."""
        self.screen = screen

        # Load image ship and receiving rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Each new ship appears at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        """Draw the ship in current position."""
        self.screen.blit(self.image, self.rect)
