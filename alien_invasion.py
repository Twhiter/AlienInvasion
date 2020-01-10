import sys
import pygame
from pygame.sprite import Group
from alien import Alien

from settings import Settings
from ship import Ship
from game_status import GameStatus
import game_functions as gf


def run_game():
    """ 初始化游戏并创建一个屏幕对象 """

    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("大战外星人")

    #创建一艘飞船
    ship = Ship(ai_settings, screen)

    #创建一个用于储存子弹的编组
    bullets = Group()

    #创建一个外星人编组
    aliens = Group()

    #创造外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #创造
    #开始游戏主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
        gf.update_aliens(ai_settings,ship,aliens)
        gf.update_screen(ai_settings, screen, ship,aliens,bullets)


run_game()



