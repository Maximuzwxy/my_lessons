import turtle
import random
import time

# t = turtle.Turtle()
# t.speed(0)
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
#
# for i in range(100):
#     t.pencolor(random.choice(colors))
#     t.forward(i * 2)
#     t.left(45)
#     time.sleep(0.1)
#
# turtle.done()


# 定义一个画五角星的函数
def draw_star(x, y, size):
    t.penup()           # 抬起画笔，准备移动到新位置
    t.goto(x, y)        # 移动到指定坐标
    t.pendown()         # 放下画笔，开始绘制
    for _ in range(5):  # 五角星有5个角
        t.forward(size) # 向前画一条边
        t.right(144)    # 每次右转144度，形成五角星

# 创建一个 Turtle 对象
t = turtle.Turtle()
t.speed(0)  # 设置最快速度

# 随机画10个五角星
for _ in range(20):
    x = random.randint(-200, 200)   # 随机x坐标
    y = random.randint(-150, 150)   # 随机y坐标
    size = random.randint(20, 60)   # 随机大小
    draw_star(x, y, size)           # 调用函数画五角星
    time.sleep(0.5)

turtle.done()  # 结束绘图，显示窗口
