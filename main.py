import random
import pygame as pg
import pygame
from math import *

pygame.init()
win = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('MARIOOO')

class obx:
    def __init__(self, pic, x, y, x_r, y_r):
        self.pic = pygame.image.load(pic)
        self.pic = pygame.transform.scale(self.pic, (x_r, y_r))
        self.rec = pg.Rect(x, y, x_r, y_r)
        self.mask = pygame.mask.from_surface(self.pic)
        self.rect = self.pic.get_rect(center=(x, 0))
        self.x = x
        self.y = y
        self.angle = 0
        self.vX = 0
        self.vY = 0
        self.rotate = 0
        self.al = random.randint(0, 360)
        self.player2 = self.pic
        self.bot2 = self.pic
        self.bot22 = self.pic
        self.bot32 = self.pic
        self.angle = 0
        self.speed = 0.2
        self.w = x_r
        self.h = y_r
        self.rect = pg.Rect(x, y, x_r, y_r)
        self.rotate = pg.transform.rotate(self.player2, -self.angle * 57)
        self.centr = self.rotate.get_rect(center=(self.x + self.w / 2, self.y + self.h / 2))
        self.mask = pg.mask.from_surface(self.rotate)


santa_sprite = [pygame.image.load("assets\kj6ik1.png"),
                pygame.image.load("assets\kj6ik2.png"),
                pygame.image.load("assets\kj6ik3.png"),
                pygame.image.load("assets\kj6ik4.png"),
                pygame.image.load("assets\kj6ik5.png"),
                pygame.image.load("assets\kj6ik6.png")]

zai_sprite = [pygame.image.load("assets\kanin1871.png"),
              pygame.image.load("assets\kanin1872.png"),
              pygame.image.load("assets\kanin1873.png"),
              pygame.image.load("assets\kanin1874.png"),
              pygame.image.load("assets\kanin1875.png"),
              pygame.image.load("assets\kanin1876.png"),
              pygame.image.load("assets\kanin1877.png"),
              pygame.image.load("assets\kanin1878.png"),
              pygame.image.load("assets\kanin1879.png"),
              pygame.image.load("assets\kanin18710.png"),
              pygame.image.load("assets\kanin18711.png"),
              pygame.image.load("assets\kanin18712.png"),
              pygame.image.load("assets\kanin18713.png"),
              pygame.image.load("assets\kanin18714.png"),
              pygame.image.load("assets\kanin18715.png"),
              pygame.image.load("assets\kanin18716.png")]

aim1 = obx('assets/bullet.png', 0, 0, 1920, 1080)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 450)
more = obx('assets\дом нг.jpg', 0, 0, 1920, 1080)
plSpeed = 1
run = True
santa_cnt = 1
zai_cnt = 1
santa_x = 0
zai_x = 1400
flag_santa = False
flag_zai = False
while run:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            run = False

    clock.tick(10)
    if santa_cnt >= len(santa_sprite):
        santa_cnt = 1
    santa = santa_sprite[santa_cnt]

    if flag_santa == True:
        santa_x -= 100
    if flag_santa == False:
        santa_x += 100
    if santa_x >= 1920:
        flag_santa = True
    if santa_x <= -800:
        flag_santa = False

    if santa_cnt == 1:
        santa_y = 440
    else:
        santa_y = 440


    if zai_cnt >= len(zai_sprite):
        zai_cnt = 1
    zai = zai_sprite[zai_cnt]
    
    if flag_zai == True:
        zai_x -= 10
    if flag_zai == False:
        zai_x += 10

    if zai_x >= 1920:
        flag_zai = True
    if zai_x <= -800:
        flag_zai = False

    if zai_cnt == 1:
        zai_y = 440
    else:
        zai_y = 440

    win.blit(more.pic, [more.x, more.y])
    win.blit(santa, (santa_x, santa_y))
    win.blit(zai, (zai_x, zai_y))
    santa_cnt += 1
    zai_cnt += 1
    pygame.display.update()
pg.quit()
