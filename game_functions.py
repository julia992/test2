import sys

import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responds to key presses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Create new bullet and include it in groups bullets.
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
                
def check_keyup_events(event, ship):
    """Responds to key release."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
                
def check_events(ai_settings, screen, ship, bullets):
    """Handles keystrokes and mouse events."""
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
                # Move the ship right.
                ship.rect.centerx += 1
       
def update_screen(ai_settings, screen, ship, bullets):
    """Refreshes the screen image and displays the new screen."""
    screen.fill(ai_settings.bg_color)
    #All bullets display behind ships and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Display the last rendered screen.
    pygame.display.flip()
