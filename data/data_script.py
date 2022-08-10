images = {}
game_settings = {}

img_file = open("data\sources")
gameSettings_file = open("data\game_settings")

line = None
while True:
    line = img_file.readline()
    if line == "":
        break
    key, value = line.split()
    images[key] = value

line = None
while True:
    line = gameSettings_file.readline()
    if line == "":
        break
    key, value = line.split()
    game_settings[key] = value