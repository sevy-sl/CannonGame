import random
import sys

import pygame
from pygame.color import THECOLORS

pygame.init()

screen = pygame.display.set_mode((640, 480))


class Cannon:
    def __init__(self):
        # TODO(1.1): создайте атрибуты пушки:
        #  * Цвет
        #  * Список точек
        #  Пусть пушка отображается как равнобедренный треугольник с высотой
        #  и основанием по 50px. Отображается в середине окна
        #  на нижней границе, см. схему в начале файла.
        self.guncolor = THECOLORS['green']
        self.dotpoints = [(295, 460), (320, 410), (345, 460)]

    def draw(self):
        # TODO(1.2): отобразите созданную в __init__ последовательность точек
        #  заданным цветом.
        pygame.draw.polygon(screen, self.guncolor, self.dotpoints, width=0)
        

class Bullet:
    def __init__(self):
        # TODO(2.1): создайте атрибуты снаряда.
        #  * Центр окружности снаряда
        #  * Радиус
        #  * Цвет
        #  * Скорость (для тестов использовать значение 3)
        self.cent = (321, 402)
        self.rad = 7
        self.bul_color = THECOLORS['green']
        self.bul_speed = 0.2

    def draw(self):
        # TODO(2.2): отобразите снаряд.
        pygame.draw.circle(screen, self.bul_color, self.cent, self.rad, width=0)

    def move(self):
        # TODO(2.3): реализуйте перемещение снаряда.
        #  Для этого нужно создать его новый центр со смещением speed по оси OY
        #  к началу коориднат.
        x, y = self.cent
        while y >= 10:
            y = y - self.bul_speed
            screen.fill(THECOLORS['black'])
            pygame.draw.circle(screen, self.bul_color, (x, y), self.rad, width=0)
            pygame.display.flip()


class Target:
    def __init__(self):
        # TODO(3.1): создайте атрибуты мишени.
        #  * Цвет
        #  * Скорость
        #  * Прямоугольник
        self.tar_color = THECOLORS['cyan']
        self.tar_speed = 8
        self.rct_atr = (2, 20, 100, 25)
        self.rct = pygame.Rect(self.rct_atr)

    def draw(self):
        # TODO(3.2): отобразите мишень.
        pygame.draw.rect(screen, self.tar_color, self.rct, width=0,)

    def move(self):
        # TODO(3.3): реализуйте движение мишени.
        #  При достижении края окна мишень должна менять направление движения
        #  на противположное. Это можно реализовать сменой знака сокрости.
        x, y, z, c = self.rct_atr
        if x < 539:
                self.rct.move_ip(self.tar_speed, 0)
                x += self.tar_speed
                if x == 538:
                    self.rct.move_ip(self.tar_speed, 0)
                    x -= self.tar_speed

        



colors = list(THECOLORS.values())
def get_random_color():
    return random.choice(colors)


cannon = Cannon()
target = Target()
bullet = Bullet()

while True:

    screen.fill(THECOLORS['black'])

    target.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bullet.move()
    # TODO(2.4): если снаряд достиг верхней границы окна, создать новый снаряд.

    # TODO(4.1): если мишень и снаряд пересеклись, сменить цвет мишени на
    #  случайный, создать новй снаряд.
    #  Для определения пересечения используйте метод прямоугольника:
    #    Rect.collidepoint(point)

    bullet.draw()
    cannon.draw()
    target.draw()

    pygame.display.flip()
    pygame.time.wait(33)