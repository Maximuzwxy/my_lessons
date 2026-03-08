from PIL import Image
import mcpi.minecraft as minecraft
import mcpi.block as block

# 颜色映射（RGB到羊毛data值）
wool_colors = {
    (255, 255, 255): 0,    # 白色 White
    (255, 192, 203): 6,    # 粉色 Pink
    (255, 255, 85): 4,     # 黄色 Yellow
    (160, 160, 160): 8,    # 浅灰 Light Gray
    (128, 128, 128): 7,    # 灰色 Gray
    (0, 0, 0): 15,         # 黑色 Black
    (255, 0, 0): 14,       # 红色 Red
    (255, 128, 0): 1,      # 橙色 Orange
    (255, 0, 255): 2,      # 品红 Magenta
    (128, 0, 255): 13,     # 紫色 Purple
    (0, 0, 255): 11,       # 蓝色 Blue
    (0, 255, 255): 9,      # 青色 Cyan
    (0, 255, 0): 5,        # 绿色 Green
    (128, 64, 0): 12,      # 棕色 Brown
    (0, 128, 0): 13,       # 深绿 Dark Green（与紫色同data，实际可选其一）
    (85, 255, 255): 3,     # 浅蓝 Light Blue
    # 你可以根据实际效果微调RGB
}

def closest_wool_color(rgb):
    # 简单最近距离匹配
    return min(wool_colors, key=lambda c: sum((a-b)**2 for a, b in zip(c, rgb)))

mc = minecraft.Minecraft.create()
x, y, z = mc.player.getTilePos()


# 读取图片并按高度150自适应缩放宽度
# img = Image.open('C:\CuLiu\\merry1.png').convert('RGB')
# 1000 ~ 1000
# img = Image.open('C:\CuLiu\\amy.png').convert('RGB')
# 3000 ~ 3000
# img = Image.open('C:\CuLiu\\keer.png').convert('RGB')
# 4000 ~ 4000
img = Image.open('C:\CuLiu\\photo\\mc.png').convert('RGB')


target_height = 150
orig_width, orig_height = img.size
target_width = int(orig_width * target_height / orig_height)
img = img.resize((target_width, target_height))

for i in range(img.width):
    for j in range(img.height):
        rgb = img.getpixel((i, j))
        wool_rgb = closest_wool_color(rgb)
        wool_data = wool_colors[wool_rgb]
        mc.setBlock(x + i, y + img.height - j, z, block.WOOL.id, wool_data)



