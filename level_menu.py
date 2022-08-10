from pygame import Surface
from pygame import font
from point import Point

class Menu:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.surf = Surface([width, height])

        self.points = []
        self.color = color
        self.surf.fill(color)
        self.it = 0
        font.init()


    def choise_up(self):
        if self.it != 0:
            self.it -=1

    def choise_down(self):
        if self.it != len(self.points):
            self.it +=1

    def add_point(self, name, xy,  color1, color2):
        self.punkts.append([len(self.points), name, xy,  color1, color2])