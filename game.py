import pygame
from tank import Tank
from block import Block
from camera import Camera
from data.data_script import *


def start_game(level_name, window):

    tank_speed = game_settings["tank_speed"]

    fin = open(level_name)
    level_size = list(map(int, fin.readline().split()))
    length = level_size[1] * 40
    width = level_size[0] * 40
    size = [length, width + 40]

    screen = pygame.Surface((length, width))

    blue_info_line = pygame.Surface([630, 40])
    red_info_line = pygame.Surface([630, 40])

    pygame.font.init()
    name = pygame.font.SysFont("FreeSans", 24)
    name1 = name.render("Player 1", True, [0, 0, 255])
    name2 = name.render("Player 2", True, [255, 0, 0])

    red_tank = Tank([1200, 40], [40, 40], tank_speed, "red", [[615, 10]])
    blue_tank = Tank([40, 40], [40, 40], tank_speed, "blue", [[615, 10]])

    for i in range(4):
        blue_tank.add_life()
        red_tank.add_life()

    level = []

    for i in range(level_size[0]):
        line = fin.readline()
        level.append(line)

    block_group = pygame.sprite.Group()
    wall = pygame.sprite.Group()
    unbreakable_wall = pygame.sprite.Group()

    for i in range(level_size[0]):
        for j in range(level_size[1]):
            if level[i][j] == "1":
                block = Block(j * 40, i * 40)
                block_group.add(block)
                if i != 0 and i != level_size[0] - 1 and j != 0 and j != level_size[1] - 1:
                    wall.add(block)
                else:
                    unbreakable_wall.add(block)

    red_tank.rect.x = length - 80
    red_tank.rect.y = 40
    blue_tank.rect.x = 40
    blue_tank.rect.y = 40
    red_tank.life_num = 3
    red_tank.isAlive = True
    blue_tank.life_num = 3
    blue_tank.isAlive = True

    red_tank.s_right = False
    red_tank.s_up = False
    red_tank.s_left = True
    red_tank.s_down = False
    red_tank.image = red_tank.image_left

    blue_tank.s_right = True
    blue_tank.sup = False
    blue_tank.s_left = False
    blue_tank.s_down = False
    blue_tank.image = blue_tank.image_right

    pygame.mixer.init()
    pygame.mixer.music.load("data/audio/mi.mp3")
    pygame.mixer.music.play(-1)

    border = pygame.Surface([20, 720])
    border.fill([255, 127, 127])

    camera_blue = Camera([630, 680], [length, width])
    camera_red = Camera([630, 680], [length, width])

    lose_surf = pygame.Surface([630, 680])
    lose_surf.fill([0, 0, 0])

    clock = pygame.time.Clock()
    window.blit(border, [630, 0])
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = False
                    pygame.mixer.music.stop()
                if event.key == pygame.K_UP:
                    red_tank.up = True
                if event.key == pygame.K_DOWN:
                    red_tank.down = True
                if event.key == pygame.K_LEFT:
                    red_tank.left = True
                if event.key == pygame.K_RIGHT:
                    red_tank.right = True
                if event.key == pygame.K_KP_ENTER and red_tank.isAlive:
                    red_tank.shoot()
                    red_tank.collide_bullets(unbreakable_wall, wall, blue_tank)

                if event.key == pygame.K_w:
                    blue_tank.up = True
                if event.key == pygame.K_s:
                    blue_tank.down = True
                if event.key == pygame.K_a:
                    blue_tank.left = True
                if event.key == pygame.K_d:
                    blue_tank.right = True
                if event.key == pygame.K_SPACE and blue_tank.isAlive:
                    blue_tank.shoot()
                    blue_tank.collide_bullets(unbreakable_wall, wall, red_tank)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    red_tank.up = False
                if event.key == pygame.K_DOWN:
                    red_tank.down = False
                if event.key == pygame.K_LEFT:
                    red_tank.left = False
                if event.key == pygame.K_RIGHT:
                    red_tank.right = False

                if event.key == pygame.K_w:
                    blue_tank.up = False
                if event.key == pygame.K_s:
                    blue_tank.down = False
                if event.key == pygame.K_a:
                    blue_tank.left = False
                if event.key == pygame.K_d:
                    blue_tank.right = False

        screen.fill([0, 255, 0])

        blue_info_line.fill([255, 0, 0])
        red_info_line.fill([0, 0, 255])
        blue_info_line.blit(name1, [3, 3])
        red_info_line.blit(name2, [3, 3])

        red_tank.move(5)
        red_tank.collide(wall, unbreakable_wall, blue_tank)
        red_tank.collide_bullets(unbreakable_wall, wall, blue_tank)
        red_tank.draw(screen, red_info_line)

        blue_tank.move(5)
        blue_tank.collide(wall, unbreakable_wall, red_tank)
        blue_tank.collide_bullets(unbreakable_wall, wall, red_tank)
        blue_tank.draw(screen, blue_info_line)
        wall.draw(screen)
        unbreakable_wall.draw(screen)
        camera_blue.update([blue_tank.rect.x, blue_tank.rect.y])
        camera_blue.surf = screen.subsurface(camera_blue.rect)

        camera_red.update([red_tank.rect.x, red_tank.rect.y])
        camera_red.surf = screen.subsurface(camera_red.rect)

        window.blit(blue_info_line, [0, 0])
        window.blit(red_info_line, [650, 0])
        window.blit(camera_blue.surf, [0, 40])
        window.blit(camera_red.surf, [650, 40])

        if not blue_tank.isAlive:
            window.blit(lose_surf, [0, 40])
        if not red_tank.isAlive:
            window.blit(lose_surf, [650, 40])

        pygame.display.flip()

        clock.tick(60)
