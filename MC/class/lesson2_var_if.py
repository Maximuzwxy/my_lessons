import time
import random

from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()
player = mc.player

def build_random_plane(x, y, z, n):
    # 选4种常用方块
    blocks = [block.STONE.id, block.GRASS.id, block.WOOD.id, block.GLASS.id]
    x, y, z = mc.player.getTilePos()
    for i in range(n):
        for j in range(n):
            b = random.choice(blocks)
            mc.setBlock(x + i, y - 1, z + j, b)

def build_lava(x, y, z, n):
    x, y, z = mc.player.getTilePos()
    for i in range(n):
        for j in range(n):
            mc.setBlock(x + i, y - 1, z + j, block.LAVA)


time.sleep(3)
x, y, z = player.getTilePos()


# gold trap
# mc.setBlock(x, y, z, block.GOLD_BLOCK)
# mc.setBlock(x+1, y, z, block.GOLD_BLOCK)
# mc.setBlock(x, y, z+1, block.GOLD_BLOCK)
# mc.setBlock(x+1, y, z+1, block.GOLD_BLOCK)

# lava set block
# build_lava(x, y, z, 10)

# while True:
#     x, y, z = mc.player.getTilePos()
#     if mc.getBlock(x, y, z) == block.LAVA.id:
#         mc.postToChat('Danger!')
#         time.sleep(1)
#         player.setPos(x, y + 1, z)
#         mc.setBlock(x, y, z, block.STONE)
#     time.sleep(0.5)


# water jump
# while True:
#     x, y, z = player.getTilePos()
#     if mc.getBlock(x, y, z) == block.WATER.id:
#         mc.postToChat('You are in water! JUMP!')
#         player.setPos(x, y + 50, z)
#     else:
#         mc.postToChat('You are safe')
#     time.sleep(0.5)

# block reporter
build_random_plane(x, y, z, 15)

while True:
    x, y, z = player.getTilePos()
    b = mc.getBlock(x, y - 1, z)

    if b == block.STONE.id:
        mc.postToChat('on stone')
    elif b == block.GRASS.id:
        mc.postToChat('on grass')
    elif b == block.WOOD.id:
        mc.postToChat('on wood')
    elif b == block.GLASS.id:
        mc.postToChat('on glass')
    else:
        mc.postToChat('other block')

    time.sleep(0.5)

