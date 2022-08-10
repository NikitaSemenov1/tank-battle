from pygame import font


class Point:
    def __init__(self, i, name, xy,  color1, color2, size):
        self.xy = xy
        self.i = i
        self.name = name
        self.colors = [color1, color2]
        font.init()
        self.p_font = font.SysFont("FreeSans", size)
        self.surf = self.p_font.render(self.name, 1, self.colors[0])

    def set_color(self, color_i):
        self.surf = self.p_font.render(self.name, 1, self.colors[color_i])
