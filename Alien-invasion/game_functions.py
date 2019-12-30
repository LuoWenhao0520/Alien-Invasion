import sys

import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    ''' keydpwn'''
    if event.key == pygame.K_RIGHT:
    # move the ship to the right
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
    # move to left
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        # create a bullet and add it to the group bullets
        fire_bullet(ai_settings, screen, ship, bullets)
    if event.key == pygame.K_ESCAPE:
        sys.exit()

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        # stop moving right
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
    # stop moving left
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    '''响应案件和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
                
            

def update_screen(ai_settings,screen,ship,bullets):
    '''更新屏幕上的图像'''
    screen.fill(ai_settings.bk_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    pygame.display.flip()

def update_bullets(bullets):
    ''' update the place of bullets and delte the missed bullets'''

    # update the place
    bullets.update()

    #delte the bullets
    for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)