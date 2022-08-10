from pygame.sprite import Sprite, collide_rect, Group
from pygame import image
from bullet import Bullet
from pygame import mixer
from time import time
from data.data_script import *


class Tank(Sprite):
    def __init__(self, pos, size, speed,  color_key, life_positions):
        Sprite.__init__(self)
        mixer.init()
        self.speed = speed
        self.length = size[0]
        self.width = size[1]
        self.image_up = image.load(images[color_key + "Tank_up"])
        self.image_right = image.load(images[color_key + "Tank_right"])
        self.image_down = image.load(images[color_key + "Tank_down"])
        self.image_left = image.load(images[color_key + "Tank_left"])
        self.image = self.image_up
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.s_left = False
        self.s_up = False
        self.s_right = False
        self.s_down = False
        self.life = image.load(images[color_key + "_life"])
        self.life_num = len(life_positions)
        self.life_positions = life_positions
        self.isAlive = True

        self.bullets = Group()
        self.sh_time = time()

    def add_life(self):
        self.life_positions.append([self.life_positions[len(self.life_positions) - 1][0] - 15,
                                   self.life_positions[len(self.life_positions) - 1][1]])
        self.life_num = len(self.life_positions)

    def move(self, speed):
        if self.isAlive:
            if self.right:
                self.s_left = False
                self.s_up = False
                self.s_right = True
                self.s_down = False

                self.image = self.image_right
                self.rect.x += speed

            elif self.left:
                self.s_left = True
                self.s_up = False
                self.s_right = False
                self.s_down = False

                self.image = self.image_left
                self.rect.x -= speed

            elif self.up:
                self.s_left = False
                self.s_up = True
                self.s_right = False
                self.s_down = False

                self.image = self.image_up
                self.rect.y -= speed

            elif self.down:
                self.s_left = False
                self.s_up = False
                self.s_right = False
                self.s_down = True

                self.image = self.image_down
                self.rect.y += speed

        for bul in self.bullets:
            bul.move()

    def _collide(self, collide_list):
        for sprite in collide_list:
            if collide_rect(self, sprite):
                if self.right:
                    self.rect.right = sprite.rect.left
                elif self.left:
                    self.rect.left = sprite.rect.right
                elif self.up:
                    self.rect.top = sprite.rect.bottom
                elif self.down:
                    self.rect.bottom = sprite.rect.top

    def collide(self, block_group, group2, tank):
        check_collide_list = []
        if self.isAlive:
            check_collide_list.extend(block_group)
            check_collide_list.extend(group2)
        if tank.isAlive:
            check_collide_list.append(tank)

        self._collide(check_collide_list)

    def draw(self, screen, info_line):
        if self.isAlive:
            screen.blit(self.image, [self.rect.x, self.rect.y])

        for bul in self.bullets:
            bul.draw(screen)

        for i in range(self.life_num):
            info_line.blit(self.life, self.life_positions[i])

    def shoot(self):
        if time() - self.sh_time >= 0.5:
            # self.shot_snd.play()
            bul = Bullet(int(game_settings["bullet_speed"]))
            self.bullets.add(bul)
            bul.shoot(self.rect.x, self.rect.y, self.s_left, self.s_up, self.s_right, self.s_down)
            self.sh_time = time()

    def collide_bullets(self, group1, group2, tank):
        for bul in self.bullets:
            if bul.collide(group1, group2, tank):
                self.bullets.remove(bul)
