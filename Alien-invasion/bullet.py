import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    '''对一个飞船发射子弹进行管理的类'''

    def __init__(self, ai_settings, screen, ship):
        '''bulid a bullet in the place of the ship'''
        super(Bullet, self).__init__()
        self.screen = screen

        #在(0,0) 处创建一个子弹矩形，再设置其正确位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #储存用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        ''' moving up the bullet'''
        # update the min num of the bullet place
        self.y -= self.speed_factor
        #update the rect of the bullet place
        self.rect.y = self.y

    def draw_bullet(self):
        ''' draw a bullet in the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)