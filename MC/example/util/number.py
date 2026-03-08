def show_single(mc, num, pos_x, pos_y, pos_z):
    if num == '1':
        for i in range(5):
            mc.setBlock(pos_x, pos_y + i, pos_z, 41)

    elif num == '2':
        for y in range(5):
            for x in range(3):
                if y == 1 and x <= 1:
                    continue
                if y == 3 and x >= 1:
                    continue
                mc.setBlock(pos_x + x, pos_y + y, pos_z, 41)

    elif num == '3':
        for y in range(5):
            for x in range(3):
                if y == 1 and x >= 1:
                    continue
                if y == 3 and x >= 1:
                    continue
                mc.setBlock(pos_x + x, pos_y + y, pos_z, 41)

    elif num == '4':
        for y in range(5):
            for x in range(3):
                if y == 0 and x >= 1:
                    continue
                if y == 1 and x >= 1:
                    continue
                if x == 1 and y >= 3:
                    continue
                mc.setBlock(pos_x + x, pos_y + y, pos_z, 41)

    elif num == '5':
        for y in range(5):
            for x in range(3):
                if y == 1 and x >= 1:
                    continue
                if y == 3 and x <= 1:
                    continue
                mc.setBlock(pos_x + x, pos_y + y, pos_z, 41)

    elif num == '6':
        for y in range(5):
            for x in range(3):
                if y == 1 and x == 1:
                    continue
                if y == 3 and x <= 1:
                    continue
                mc.setBlock(pos_x + x, pos_y + y, pos_z, 41)

    elif num == '7':
        for y in range(5):
            for x in range(3):
                if y <= 3 and x >= 1:
                    continue
                mc.setBlock(pos_x + x, pos_y + y, pos_z, 41)

    elif num == '8':
        for y in range(5):
            for x in range(3):
                if y == 1 and x == 1:
                    continue
                if y == 3 and x == 1:
                    continue
                mc.setBlock(pos_x + x, pos_y + y, pos_z, 41)

    elif num == '9':
        for y in range(5):
            for x in range(3):
                if y == 1 and x >= 1:
                    continue
                if y == 3 and x == 1:
                    continue
                mc.setBlock(pos_x + x, pos_y + y, pos_z, 41)
    elif num == '0':
        for y in range(5):
            for x in range(3):
                if 1<=y<=3 and x == 1:
                    continue
                mc.setBlock(pos_x + x, pos_y + y, pos_z, 41)


def show(mc, num, x, y, z):
    z += 5
    # clean
    mc.setBlocks(x-20,y,z,x+20,y+5,z,0)

    # build
    for i in str(num)[::-1]:
        show_single(mc, i, x, y, z)
        x += 4

