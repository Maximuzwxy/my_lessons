import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
player = mc.player
water = 8

while True:
    pos = player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    block = mc.getBlock(x, y, z)

    # 判断player是否在水里
    if block == water:
        mc.postToChat("You are in the water")
        player.setPos(x, y+100, z)
    else:
        mc.postToChat("You are not in the water")