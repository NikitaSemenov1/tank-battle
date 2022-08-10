from pygame.sprite import Sprite, collide_rect
from pygame import image
from data.data_script import *


class Bullet(Sprite):
    def __init__(self, speed):
        Sprite.__init__(self)
        self.img_down = image.load(images["bul_down"])
        self.img_right = image.load(images["bul_right"])
        self.img_up = image.load(images["bul_up"])
        self.img_left = image.load(images["bul_left"])
        self.image = self.img_right
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.x_vel = 0
        self.y_vel = 0
        self.speed = speed
        self.f = False
        self.sh_time = 0

    def shoot(self, x, y, left, up, right, down):

        if left:
            self.x_vel = -self.speed
            self.y_vel = 0
            self.rect.x = x - 20
            self.rect.y = y + 18
            self.image = self.img_left
        elif up:
            self.x_vel = 0
            self.y_vel = -self.speed
            self.rect.x = x + 18
            self.rect.y = y - 20
            self.image = self.img_up
        elif right:
            self.x_vel = self.speed
            self.y_vel = 0
            self.rect.x = x + 40
            self.rect.y = y + 18
            self.image = self.img_right
        elif down:
            self.x_vel = 0
            self.y_vel = self.speed
            self.rect.x = x + 18
            self.rect.y = y + 40
            self.image = self.img_down

    def move(self):

        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

    def collide(self, group1, group2, tank):
        f = False
        for block in group1:
            if collide_rect(self, block):
                f = True
        for block in group2:
            if collide_rect(self, block):
                group2.remove(block)
                f = True

        if collide_rect(self, tank) and tank.isAlive:
            tank.life_num -= 1
            if tank.life_num == 0:
                tank.isAlive = False
            f = True
        return f

    def draw(self, screen):

        screen.blit(self.image, [self.rect.x, self.rect.y])
