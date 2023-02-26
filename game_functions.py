import sys
import pygame
from pygame.event import Event
from pygame import sprite
from ship import Ship
from settings import Settings
from bullet import Bullet


def check_events(
        settings: Settings,
        screen: pygame.Surface,
        ship: Ship,
        bullets: pygame.sprite.Group,
):
    """响应键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, bullets, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(
    event: Event,
    settings: Settings,
    screen: pygame.Surface,
    bullets: sprite.Group,
    ship: Ship
):
    """keydown"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(
            bullets=bullets,
            settings=settings,
            screen=screen,
            ship=ship,
        )


def check_keyup_events(event: Event, ship: Ship):
    """keyup"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(
    settings: Settings,
    screen: pygame.Surface,
    ship: Ship,
    bullets: pygame.sprite.Group
):
    # 每次循环是都重绘屏幕
    screen.fill(settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets: pygame.sprite.Group):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(bullets, settings, screen, ship):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)
