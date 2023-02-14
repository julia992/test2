import sys

import pygame

def check_events():
    """Handles keystrokes and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Refreshes the screen image and displays the new screen."""
    # The screen is redrawn on each iteration of the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Display the last rendered screen.
    pygame.display.flip()
