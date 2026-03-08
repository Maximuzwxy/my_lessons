import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

while True:
    # 必须用剑右键敲击才能触发
    hits = mc.events.pollBlockHits()
    for h in hits:
        x, y, z = h.pos
        # YOUR CODE HERE
