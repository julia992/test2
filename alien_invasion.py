import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
#Initilizian game and create object of display.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
#Create the ship.
    ship = Ship(screen)

#Choose main color background.
    bg_color = (230, 230, 230)

#Start tne main range of game.
    while True:
    
#Monitor display and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

#Screen is drawn with each transition of the loop.
                screen.fill(ai_settings.bg_color)
                ship.blitme()


#Display last drawn screen.
                pygame.display.flip()
         
run_game()
