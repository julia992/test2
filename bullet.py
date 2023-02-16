import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class for manage bullets from ship."""

def __init__(self, ai_settings, screen, ship):
    """Create a bullet at now position of ship."""
    super().__init__()
    self.screen = screen

    #Create bullet in position (0,0) and destination correct position.
    self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                            ai_settings.bullet_height)
    self.rect.centerx = ship.rect.centerx
    self.rect.top = ship.rect.top

    #Bullet position is stored in real format.
    self.y = float(self.rect.y)

    self.color = ai_settings.bullet_color
    self.speed_factor = ai_settings.bullet_speed_factor

def update(self):
    """Move the bullet on display up."""
    #Update bullet position in real formate.
    self.y -= self.speed_factor
    #Update rectangle position.
    self.rect.y = self.y

def draw_bullet(self):
    """Display the bullet."""
    pygame.draw.rect(self.screen, self.color, self.rect)
    
