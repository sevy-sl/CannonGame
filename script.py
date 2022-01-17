import random
import sys
import pygame
from pygame.color import THECOLORS

pygame.init()


screen = pygame.display.set_mode((640, 480))


class Cannon:
    
    def __init__(self):
        self.guncolor = THECOLORS['green']
        self.dotpoints = [(295, 460), (320, 410), (345, 460)]

    def draw(self):
        pygame.draw.polygon(screen, self.guncolor, self.dotpoints, 0)
        

class Bullet:
    
    def __init__(self):
        self.bul_rect = pygame.Rect([316, 400, 9, 9])
        self.bul_color = THECOLORS['green']
        self.bul_speed = 15

    def draw(self):
        pygame.draw.rect(screen, self.bul_color, self.bul_rect, 0)

    def shoot(self):
        if self.bul_rect[1] > 10:
            self.bul_rect.move_ip(0, -self.bul_speed)
            Bullet.draw(self)
            if self.bul_rect[1] == 10:
                return
    
    def reload(self):
        now_ypos = 400 - self.bul_rect[1]     
        self.bul_rect.move_ip(0, now_ypos)


class Target:
    
    def __init__(self):
        self.tar_color = THECOLORS['cyan']
        self.tar_speed = 7
        self.numforback = 534
        self.numforforw = 2
        self.tar_rect = pygame.Rect(2, 30, 100, 25)

    def draw(self):
        pygame.draw.rect(screen, self.tar_color, self.tar_rect, 0)

    def move(self):
        
        def move_back():
            if self.numforback == 2:
                try:
                    self.numforforw -= 532
                    self.numforback += 532  
                    move_forw()
                finally:
                    return
            self.numforback -= self.tar_speed
            self.tar_rect.move_ip(-self.tar_speed, 0)
        def move_forw():
            if self.numforforw == 534:
                try:
                    move_back()
                finally:
                    return
            self.numforforw += self.tar_speed
            self.tar_rect.move_ip(self.tar_speed, 0)
        move_forw()
        


cannon = Cannon()
target = Target()
bullet = Bullet()

while True:

    screen.fill(THECOLORS['black'])
    target.move()

    def hit():
        colors = list(THECOLORS.values())
        if pygame.Rect.colliderect(target.tar_rect, bullet.bul_rect) == True:    
            target.tar_color = random.choice(colors)
            bullet.reload()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                bullet.reload()
    
    if pygame.key.get_pressed()[pygame.K_UP]:
        bullet.shoot()
        hit()  

    bullet.draw()
    cannon.draw()
    target.draw()

    pygame.display.flip()
    pygame.time.wait(33)