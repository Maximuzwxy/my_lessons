import mcpi.minecraft as minecraft
from mcpi import block
mc = minecraft.Minecraft.create()

# The position of light
# YOUR CODE HERE
x = 0
y = 0
z = 0

RED = 14
GREEN = 13

while True:
    # 必须用剑右键敲击才能触发
    hits = mc.events.pollBlockHits()
    for h in hits:
        hx, hy, hz = h.pos
        if hx == x and hy == y and hz == z:
            # YOUR CODE HERE
            # YOUR CODE HERE OVER
            pass

