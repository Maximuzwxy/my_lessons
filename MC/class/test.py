# import time
#
# from mcpi import minecraft
# from mcpi import block
#
# mc = minecraft.Minecraft.create('192.168.66.207')
# player = mc.player
#
# time.sleep(1)
#
# # 生成坐标
# x, y, z = player.getTilePos()
#
# # while True:
# #     x, y, z = mc.player.getTilePos()
# #     if mc.getBlock(x, y, z) == 10:
# #         mc.postToChat('Danger!')
# #         time.sleep(1)
# #         player.setPos(x, y + 1, z)
# #         mc.setBlock(x, y, z, 1)
# #     time.sleep(0.5)
#
#
# while True:
#     x, y, z = player.getTilePos()
#     b = mc.getBlock(x, y - 1, z)
#
#     if b == 1:
#         mc.postToChat('on stone')
#     elif b == 2:
#         mc.postToChat('on grass')
#     elif b == 17:
#         mc.postToChat('on wood')
#     elif b == 20:
#         mc.postToChat('on glass')
#     else:
#         mc.postToChat('other block')
#
#     time.sleep(0.5)
#

# a = 0
# while True:
#     print('hello')
#     a = a + 1
#     if a > 6:
#         break

# a = 0
# while a < 6:
#     a = a + 1
#     print('hello')

for i in range(6):
    print('hello')

