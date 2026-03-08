import random
import time

from mcpi import minecraft
from mcpi import block
from mcpi import entity

mc = minecraft.Minecraft.create()

# blocks = [block.STONE.id, block.GRASS.id, block.WOOD.id, block.GLASS.id, block.GOLD_BLOCK.id]
blocks = [1, 2, 17, 20, 41]

time.sleep(3)

x,y,z = mc.player.getTilePos()

# 依次生成blocks
# for i in blocks:
#     mc.setBlock()
#     time.sleep(1)
#     x = x + 1

# x方向生成block
# for i in range():
#     mc.setBlock()
#     time.sleep(1)

# 每隔一个生成block
# for i in range():
#     if i % 2 == 0:
#         mc.setBlock()
#     else:
#         mc.setBlock()
#     time.sleep(0.2)

# for i in range():
#     mc.setBlock()
#     time.sleep(0.2)

# 3种block交替生成
# for i in range():
#     if i % 3 == 0:
#         mc.setBlock()
#     elif i % 3 == 1:
#         mc.setBlock()
#     elif i % 3 == 2:
#         mc.setBlock()
#     time.sleep(0.2)

# 平面
# for i in range():
#     for j in range():
#         mc.setBlock()
#         time.sleep(0.1)

# 墙
# for i in range():
#     for j in range():
#         mc.setBlock()
#         time.sleep(0.1)

# 立方体
# for i in range():
#     for j in range():
#         for k in range():
#             mc.setBlock()
#             time.sleep(0.1)


# falling chicken in lava or water
# for i in range():
#     mc.spawnEntity()
#     time.sleep(0.1)

# stairs
# for i in range():
#     mc.setBlock()
#     time.sleep(0.1)

# for j in range():
#     for i in range():
#         mc.setBlock()
#         time.sleep(0.1)

# 实体楼梯
# for i in range():
#     for j in range():
#         mc.setBlock()
#         time.sleep(0.1)

# for k in range():
#     for i in range():
#         for j in range():
#             mc.setBlock()
#             time.sleep(0.1)

# Pyramid-setBlock
# def pyramid(n):
#     for i in range():
#         for j in range():
#             for k in range():
#                 mc.setBlock()
#                 time.sleep(0.1)
# pyramid(10)

# setBlocks
# mc.setBlocks()

# what will happen
# mc.setBlocks()

# platform under
# n = 5
# mc.setBlocks()
#
# Pyramid-setBlocks
# n = 5
# for i in range():
#     mc.setBlocks()  # 建造⼀层⾦字
#     time.sleep(0.5)

# rainbow street
# for i in range():  # 获取玩家坐标
#     c1 = random.randint()  #获取第⼀个随机颜⾊
#     mc.setBlocks()
#
#     c2 = random.randint()  #获取第⼆个随机颜⾊
#     mc.setBlocks()
#
#     # code


