from pythoncraft import player

for x in range(-2, 3):
    for z in range(-1,3):
        block_id = player.getBlock(x,0,z)
        if block_id == 95:
            player.setBlock(x,1,z,41)

player.say("Done")