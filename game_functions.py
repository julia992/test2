import sys

import pygame

def check_events(ship):
    """Handles keystrokes and mouse events."""
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship right.
                ship.rect.centerx +=1
       
def update_screen(ai_settings, screen, ship):
    """Refreshes the screen image and displays the new screen."""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Display the last rendered screen.
    pygame.display.flip()
