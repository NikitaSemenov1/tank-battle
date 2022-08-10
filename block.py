from pygame.sprite import Sprite
from pygame import image
from data.data_script import *


class Block(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = image.load(images["block"])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y