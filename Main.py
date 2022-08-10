import pygame
from menu import Menu
from game import start_game
from data.data_script import *


WINDOWS_SIZE = (1280, 720)

level_sources = open("data/level_sources")
level_source = level_sources.readline()
level_source = level_source[:-1]
levels = level_sources.readlines()
for i in range(len(levels)):
    levels[i] = levels[i][:-1]
for level in levels:
    print(level)
level_i = int(input("Enter the num of level: "))
level_source += levels[level_i - 1]


pygame.init()

window = pygame.display.set_mode(WINDOWS_SIZE, pygame.FULLSCREEN)
pygame.display.set_caption("Tank battle")
icon = pygame.image.load(images["redTank_up"])
pygame.display.set_icon(icon)

menu = Menu(WINDOWS_SIZE, [127, 127, 127])

menu.add_point("Play", (0, 0), [255, 0, 255], [127, 0, 0], 50)
menu.add_point("Exit", (0, 50), [255, 0, 255], [127, 0, 0], 50)

menu_f = True

while menu_f:

    menu.draw()
    window.blit(menu.surf, [0, 0])
    pygame.display.flip()

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_KP_ENTER:
                if menu.it == 0:
                    start_game(level_source, window)
                elif menu.it == len(menu.points) - 1:
                    menu_f = False
            elif ev.key == pygame.K_DOWN:
                menu.choose_down()
            elif ev.key == pygame.K_UP:
                menu.choose_up()

pygame.quit()
