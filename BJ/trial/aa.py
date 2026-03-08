import pygame
import sys
import random
import time

# --- 1. 初始化和常量定义 ---

# 初始化 Pygame
pygame.init()

# 屏幕尺寸
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
GRID_SIZE = 20  # 每个格子的大小
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# 颜色定义 (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GREEN = (0, 150, 0)

# 方向向量
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# 游戏速度
GAME_SPEED = 10

# --- 2. 游戏对象和变量 ---

# 创建游戏窗口
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Python 贪食蛇')

# 创建时钟对象，用于控制游戏帧率
clock = pygame.time.Clock()

# 字体设置
font_style = pygame.font.SysFont("microsoftyahei", 30)
score_font = pygame.font.SysFont("comicsansms", 35)


def show_score(score):
    """在屏幕上显示当前分数"""
    value = score_font.render(f"分数: {score}", True, WHITE)
    screen.blit(value, [10, 10])


def draw_snake(snake_list):
    """绘制蛇的身体"""
    for x in snake_list:
        pygame.draw.rect(screen, DARK_GREEN, [x[0], x[1], GRID_SIZE, GRID_SIZE])
        # 为蛇的身体添加一个白色边框，使其更美观
        pygame.draw.rect(screen, GREEN, [x[0] + 1, x[1] + 1, GRID_SIZE - 2, GRID_SIZE - 2])


def show_message(msg, color, y_displace=0):
    """在屏幕中央显示消息"""
    mesg = font_style.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + y_displace))
    screen.blit(mesg, mesg_rect)


def game_loop():
    """游戏主循环"""
    game_over = False
    game_close = False

    # 蛇的初始位置和长度
    lead_x = SCREEN_WIDTH / 2
    lead_y = SCREEN_HEIGHT / 2
    snake_list = []
    snake_length = 1

    # 蛇的初始移动方向
    x1_change = 0
    y1_change = 0
    direction = None

    # 食物的初始位置
    food_x = round(random.randrange(0, SCREEN_WIDTH - GRID_SIZE) / GRID_SIZE) * GRID_SIZE
    food_y = round(random.randrange(0, SCREEN_HEIGHT - GRID_SIZE) / GRID_SIZE) * GRID_SIZE

    # --- 3. 游戏主循环 ---
    while not game_over:

        # --- 4. 游戏结束后的处理 ---
        while game_close:
            screen.fill(BLACK)
            show_message("游戏结束!", RED, y_displace=-50)
            show_message(f"你的分数: {snake_length - 1}", WHITE)
            show_message("按 C-重新开始 或 Q-退出", WHITE, y_displace=50)
            show_score(snake_length - 1)
            pygame.display.update()

            # 检查用户选择
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Q键退出
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # C键重新开始
                        game_loop()  # 重新调用游戏主函数
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        # --- 5. 事件处理 ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != RIGHT:
                    x1_change = -GRID_SIZE
                    y1_change = 0
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    x1_change = GRID_SIZE
                    y1_change = 0
                    direction = RIGHT
                elif event.key == pygame.K_UP and direction != DOWN:
                    y1_change = -GRID_SIZE
                    x1_change = 0
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    y1_change = GRID_SIZE
                    x1_change = 0
                    direction = DOWN

        # --- 6. 碰撞检测 ---
        # 1. 墙壁碰撞
        if lead_x >= SCREEN_WIDTH or lead_x < 0 or lead_y >= SCREEN_HEIGHT or lead_y < 0:
            game_close = True

        # 更新蛇头位置
        lead_x += x1_change
        lead_y += y1_change

        # --- 7. 游戏逻辑更新 ---
        screen.fill(BLACK)

        # 绘制食物
        pygame.draw.rect(screen, RED, [food_x, food_y, GRID_SIZE, GRID_SIZE])

        # 更新蛇的头部
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        # 如果蛇的长度超过了规定长度，删除尾部
        if len(snake_list) > snake_length:
            del snake_list[0]

        # 2. 自身碰撞
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # 绘制蛇
        draw_snake(snake_list)
        # 显示分数
        show_score(snake_length - 1)

        # 刷新屏幕
        pygame.display.update()

        # --- 8. 吃食物逻辑 ---
        if lead_x == food_x and lead_y == food_y:
            # 重新生成食物
            food_x = round(random.randrange(0, SCREEN_WIDTH - GRID_SIZE) / GRID_SIZE) * GRID_SIZE
            food_y = round(random.randrange(0, SCREEN_HEIGHT - GRID_SIZE) / GRID_SIZE) * GRID_SIZE
            # 蛇的长度增加
            snake_length += 1

        # 控制游戏速度
        clock.tick(GAME_SPEED)

    # --- 9. 退出游戏 ---
    pygame.quit()
    sys.exit()


# --- 启动游戏 ---
if __name__ == '__main__':
    game_loop()