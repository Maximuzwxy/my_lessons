import mcpi.minecraft as minecraft
from mcpi import block
mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
x = 0
y = 0
z = 0
while True:
    # 必须用剑右键敲击才能触发
    hits = mc.events.pollBlockHits()
    for h in hits:
        x, y, z = h.pos
        mc.setBlock(x, y, z, block.GOLD_BLOCK)
