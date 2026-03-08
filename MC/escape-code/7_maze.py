from pythoncraft import player

x = 0
y = 0
z = 0

while True:
    if player.getBlock(x+1,y,z) == 0:
        x = x+1
    elif player.getBlock(x-1,y,z) == 0:
        x = x-1
    elif player.getBlock(x,y,z+1) == 0:
        z = z+1
    elif player.getBlock(x,y,z-1) == 0:
        z = z-1
    else:
        break
    player.setBlock(x,y,z,41)

player.say("Done")
