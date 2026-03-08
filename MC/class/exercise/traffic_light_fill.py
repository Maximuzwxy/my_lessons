import time

from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()
player = mc.player

time.sleep(3)

RED = 14
GREEN = 13

# platform xyz
px, py, pz = -946, 19, -17

# # Task0: build a platform
# def build_platform(n):
#     # clear blocks
#     mc.setBlocks()
#     # rebuild platform
#     mc.setBlocks()
# build_platform(18)
#
# # Task1: build the lane
# # car start position
# sx, sy, sz = px + 4, py, pz + 4
# def build_lane():
#     mc.setBlocks()
#     mc.setBlocks()
#     mc.setBlocks()
#     mc.setBlocks()
# build_lane()
#
# # Task2: build the moving car demo
# cx, cy, cz =
# def init_car():
#     mc.setBlock()
#
# def car_move_demo():
#     global cx, cy, cz
#
#     while True:
#         mc.setBlock()
#         cx += 1
#         mc.setBlock()
#         time.sleep(0.2)
#
#         if cx >= sx + 10:
#             mc.setBlock()
#             cx = sx
#
# init_car()
# # car_move_demo()
#
# # Task3: build the moving car
# dx, dz = 0, 0
# def car_move():
#     global cx, cy, cz
#     global dx, dz
#     if cx == sx and cz == sz:
#
#     elif cx == sx + 10 and cz == sz:
#
#     elif cx == sx + 10 and cz == sz + 10:
#
#     elif cx == sx and cz == sz + 10:
#
#
#     mc.setBlock()
#     cx += dx
#     cz += dz
#     mc.setBlock()
#
# def test_car():
#     while True:
#         car_move()
#         time.sleep(0.2)
# # test_car()
#
# # Task4: Build the traffic light, get xyz
# # light xyz
# lx, ly, lz = px + 3, py + 1, pz + 3
#
# def build_light(x, y, z):
#     # A
#     mc.setBlock()
#     # B
#     mc.setBlock()
#     # LIGHT
#     mc.setBlock()
# build_light(lx, ly, lz)
#
# # Task5: Change the light
# light_green = False
#
# while True:
#     # 必须用剑右键敲击才能触发
#     hits = mc.events.pollBlockHits()
#     for h in hits:
#         hx, hy, hz = h.pos
#         if hx == lx and hy == ly + 2 and hz == lz:
#             b = mc.getBlockWithData()
#             mc.postToChat(f'x y z: {hx} {hy} {hz}')
#
#             if b.data == GREEN:
#                 mc.setBlock()
#                 light_green =
#             elif b.data == RED:
#                 mc.setBlock()
#                 light_green =
#
#     if light_green:
#
#
#     time.sleep(0.2)




