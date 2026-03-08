from pythoncraft import player

for y in range(4):
    for x in range(-3+y, 4-y):
        for z in range(1+y, 8-y):
            if x == -3+y or x == 3-y or z == 1+y or z == 7-y:
                player.setBlock(x,y,z,24)

player.say("Done")



