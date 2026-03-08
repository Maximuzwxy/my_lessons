import random
import time

from mcpi import minecraft
from mcpi import block
from mcpi import entity

# mc = minecraft.Minecraft.create('192.168.66.207')
mc = minecraft.Minecraft.create()

time.sleep(3)

x,y,z = mc.player.getTilePos()

# x方向生成block
# for i in range(10):
#     mc.setBlock(x + i, y, z, 41)
#     time.sleep(1)

# 每隔一个生成block
# for i in range(0, 20, 2):
#     mc.setBlock(x + i, y, z, 41)
#     time.sleep(0.2)

# 3种block交替生成
# for i in range(20):
#     if i % 3 == 0:
#         mc.setBlock(x + i, y, z, 41)
#     elif i % 3 == 1:
#         mc.setBlock(x + i, y, z, 57)
#     elif i % 3 == 2:
#         mc.setBlock(x + i, y, z, 73)
#     time.sleep(0.2)

# for i in range(16):
#     mc.setBlock(x + i, y, z, 35, i)

# 平面
# for i in range(10):
#     for j in range(10):
#         mc.setBlock(x + j, y, z + i, 41)
#         time.sleep(0.1)

# 墙
# for i in range(10):
#     for j in range(10):
#         mc.setBlock(x + j, y + i, z, 41)
#         time.sleep(0.1)

# 立方体
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             mc.setBlock(x + k, y + i, z + j, 41)
#             time.sleep(0.1)

# falling chicken in lava or water
for i in range(20):
    mc.spawnEntity(x, y + i, z, entity.CHICKEN)
    time.sleep(0.1)

# stairs
# for i in range(30):
#     mc.setBlock(x + i, y + i, z, 41)
#     time.sleep(0.1)

# for j in range(3):
#     for i in range(30):
#         mc.setBlock(x + i, y + i, z + j, 41)
#         time.sleep(0.1)

# Pyramid-setBlocks
# n = 5
# for i in range(n, -1, -1):
#     mc.setBlocks(x - i, y - 1 - i, z - i, x + i, y - 1 - i, z + i, 41)  # 建造⼀层⾦字
#     time.sleep(0.1)

# random teleport--near
# radius = 200
# while True:
#     dx = random.randint(-radius, radius)
#     dy = random.randint(-20, 50)
#     dz = random.randint(-radius, radius)
#
#     mc.setBlock(x + dx, y + dy, z + dz, 0)
#     mc.setBlock(x + dx, y + dy + 1, z + dz, 0)
#     player.setPos(x + dx, y + dy, z + dz)
#
#     time.sleep(5)

# flower walker-yellow
# while True:
#     x, y, z = player.getTilePos()
#     mc.setBlock(x, y, z, 37)
#     time.sleep(0.1)

# flower walker-random color
# while True:
#     x, y, z = player.getTilePos()
#     mc.setBlock(x, y, z, 38, random.randint(0, 9))
#     time.sleep(0.2)

# flower walker-flower sea
# while True:
#     x, y, z = player.getTilePos()
#     dx = random.randint(-5, 5)
#     dz = random.randint(-5, 5)
#     mc.setBlock(x + dx, y, z + dz, 38, random.randint(0, 9))
#     time.sleep(0.01)

