import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    ''' Build a Ship '''
    ship = Ship(ai_settings,screen)
    # create a group to store bullet
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        
        gf.update_bullets(bullets)
        print(len(bullets))
        gf.update_screen(ai_settings,screen,ship,bullets)
        pygame.display.flip()

run_game()