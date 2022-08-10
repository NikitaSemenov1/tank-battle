from pygame import Surface
from point import Point


class Menu:
    def __init__(self, size, color):
        self.width = size[1]
        self.length = size[0]
        self.surf = Surface([self.length, self.width])
        self.points = []
        self.color = color
        self.surf.fill(color)
        self.it = 0

    def draw(self):
        self.surf.fill(self.color)
        for p in self.points:
            if p.i == self.it:
                p.set_color(1)
                self.surf.blit(p.surf, p.xy)
            else:
                p.set_color(0)
                self.surf.blit(p.surf, p.xy)

    def choose_up(self):
        self.it -= 1
        self.it %= len(self.points)

    def choose_down(self):
        self.it += 1
        self.it %= len(self.points)

    def add_point(self,  name, xy,  color1, color2, size):
        self.points.append(Point(len(self.points), name, xy,  color1, color2, size))
