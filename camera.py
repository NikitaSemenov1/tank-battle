from pygame import Rect, Surface


class Camera:
    def __init__(self, size, big_size):
        self.surf = Surface(size)
        self.rect = Rect(0, 0, size[0], size[1])
        self.big_length = big_size[0]
        self.big_width = big_size[1]
        self.length = size[0]
        self.width = size[1]

    def update(self, pos):
        self.rect.x = pos[0] - (self.length // 2 - 20)
        self.rect.y = pos[1] - (self.width // 2 - 20)
        if pos[0] < self.length // 2 - 20:
            self.rect.x = 0
        if pos[1] < self.width // 2 - 20:
            self.rect.y = 0
        if pos[0] > self.big_length - self.length // 2 - 20:
            self.rect.x = self.big_length - self.length
        if pos[1] > self.big_width - self.width // 2 - 20:
            self.rect.y = self.big_width - self.width
