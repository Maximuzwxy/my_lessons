import time

from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create('192.168.66.207')
# mc = minecraft.Minecraft.create()
player = mc.player

time.sleep(3)

# 生成坐标
x, y, z = player.getTilePos()

def gen_tile(x, y, z, n):
    for i in range(n):
        mc.setBlock(x + i, y, z, block.WOOL.id, 14)
        time.sleep(0.1)
    for i in range(n):
        mc.setBlock(x, y + i, z, block.WOOL.id, 13)
        time.sleep(0.1)
    for i in range(n):
        mc.setBlock(x, y, z + i, block.WOOL.id, 11)
        time.sleep(0.1)
    mc.setBlock(x, y, z, block.WOOL.id)

gen_tile(x, y, z, 20)


# setBlock
# mc.setBlock(x, y, z, block.GRASS)         # 2
# mc.setBlock(x, y, z, block.STONE)         # 1
# mc.setBlock(x, y, z, block.WOOL)          # 35
# mc.setBlock(x, y, z, block.GOLD_BLOCK)    # 41
# mc.setBlock(x, y, z, block.GLASS)         # 20
# mc.setBlock(x, y, z, block.DIAMOND_BLOCK) # 57
# mc.setBlock(x, y, z, block.REDSTONE_ORE)  # 73
# mc.setBlock(x, y, z, block.BEDROCK)       # 7
# mc.setBlock(x, y, z, block.AIR)           # 0
# mc.setBlock(x, y, z, block.WOOD)          # 17

mc.setBlock(x + 1, y, z, block.GRASS)
time.sleep(1)
mc.setBlock(x, y, z + 1, block.GRASS)
time.sleep(1)
mc.setBlock(x, y + 3, z, block.GRASS)










# x, y, z = player.getTilePos()
# player.setPos(x, y + 300, z)
#
# while True:
#     x, y, z = player.getTilePos()
#     time.sleep(0.1)
#     if mc.getBlock(x, y, z) != block.FLOWER_YELLOW.id:
#         mc.setBlock(x, y, z, block.FLOWER_YELLOW)
#     else:
#         print('no')



