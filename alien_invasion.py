# coding:utf-8

import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")

    ship = Ship(settings=ai_settings, screen=screen)

    bullets: Group = Group()

    # 开始有序的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(
            settings=ai_settings,
            screen=screen,
            ship=ship,
            bullets=bullets,
        )

        gf.update_bullets(bullets)

        ship.update()

        # 每次循环是都重绘屏幕
        gf.update_screen(
            settings=ai_settings,
            screen=screen,
            ship=ship,
            bullets=bullets,
        )


run_game()
