# coding:utf-8

import sys
import pygame

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

    # 设置背景颜色
    bg_color = ai_settings.bg_color

    ship = Ship(settings=ai_settings, screen=screen)

    # 开始有序的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ship)

        ship.update()

        # 每次循环是都重绘屏幕
        gf.update_screen(ai_settings, screen, ship)


run_game()
