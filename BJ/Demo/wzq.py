import pygame
import sys

# --- 1. 初始化和常量定义 ---

# 初始化 Pygame
pygame.init()

# 屏幕和棋盘尺寸
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BOARD_SIZE = 15  # 15x15 的棋盘
CELL_SIZE = SCREEN_WIDTH // (BOARD_SIZE + 1)  # 计算每个格子的大小，留出边距
MARGIN = CELL_SIZE // 2  # 棋盘边缘的边距

# 颜色定义 (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (205, 133, 63)  # 类似木质棋盘的颜色
LINE_COLOR = (50, 50, 50)
HIGHLIGHT_COLOR = (255, 0, 0)

# 游戏状态
BLACK_TURN = 1
WHITE_TURN = 2
GAME_OVER = 3

# 创建游戏窗口
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Python 五子棋')

# 创建时钟对象
clock = pygame.time.Clock()

# 字体设置
font_style = pygame.font.SysFont("microsoftyahei", 40)
small_font = pygame.font.SysFont("microsoftyahei", 25)


def draw_board():
    """绘制棋盘背景和网格线"""
    # 填充背景色
    screen.fill(BACKGROUND_COLOR)

    # 绘制网格线
    for i in range(1, BOARD_SIZE + 1):
        # 横线
        pygame.draw.line(screen, LINE_COLOR,
                         (MARGIN, MARGIN + i * CELL_SIZE),
                         (SCREEN_WIDTH - MARGIN, MARGIN + i * CELL_SIZE), 1)
        # 竖线
        pygame.draw.line(screen, LINE_COLOR,
                         (MARGIN + i * CELL_SIZE, MARGIN),
                         (MARGIN + i * CELL_SIZE, SCREEN_HEIGHT - MARGIN), 1)


def draw_pieces(board):
    """根据棋盘数据绘制所有棋子"""
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == BLACK_TURN:
                center_x = MARGIN + (col + 1) * CELL_SIZE
                center_y = MARGIN + (row + 1) * CELL_SIZE
                pygame.draw.circle(screen, BLACK, (center_x, center_y), CELL_SIZE // 2 - 2)
            elif board[row][col] == WHITE_TURN:
                center_x = MARGIN + (col + 1) * CELL_SIZE
                center_y = MARGIN + (row + 1) * CELL_SIZE
                pygame.draw.circle(screen, WHITE, (center_x, center_y), CELL_SIZE // 2 - 2)
                # 为白棋添加一个黑色边框，使其更清晰
                pygame.draw.circle(screen, LINE_COLOR, (center_x, center_y), CELL_SIZE // 2 - 2, 1)


def is_win(board, row, col):
    """检查在(row, col)落子后是否获胜"""
    player = board[row][col]
    if player == 0:
        return False

    # 检查的四个方向：水平、垂直、主对角线、副对角线
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for dr, dc in directions:
        count = 1  # 当前位置已经有一个棋子
        # 向正方向检查
        for i in range(1, 5):
            r, c = row + i * dr, col + i * dc
            if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
                count += 1
            else:
                break
        # 向反方向检查
        for i in range(1, 5):
            r, c = row - i * dr, col - i * dc
            if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
                count += 1
            else:
                break

        if count >= 5:
            return True
    return False


def show_message(msg, color, y_displace=0):
    """在屏幕中央显示消息"""
    mesg = font_style.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + y_displace))
    screen.blit(mesg, mesg_rect)


def game_loop():
    """游戏主循环"""
    # 初始化棋盘数据，0表示空，1表示黑棋，2表示白棋
    board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    current_player = BLACK_TURN
    game_state = BLACK_TURN  # 游戏状态：轮到黑棋、轮到白棋、游戏结束
    winner = None

    # --- 3. 游戏主循环 ---
    while True:
        # --- 4. 事件处理 ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_state == GAME_OVER:
                    # 按 R 键重新开始
                    game_loop()

            # 如果游戏未结束且是鼠标点击事件
            if event.type == pygame.MOUSEBUTTONDOWN and game_state != GAME_OVER:
                x, y = event.pos

                # 将屏幕坐标转换为棋盘网格坐标
                col = round((x - MARGIN) / CELL_SIZE) - 1
                row = round((y - MARGIN) / CELL_SIZE) - 1

                # 检查落子位置是否有效（在棋盘内且为空）
                if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] == 0:
                    # 在棋盘数据上记录落子
                    board[row][col] = current_player

                    # 检查是否获胜
                    if is_win(board, row, col):
                        game_state = GAME_OVER
                        winner = current_player
                    else:
                        # 切换玩家
                        current_player = WHITE_TURN if current_player == BLACK_TURN else BLACK_TURN

        # --- 5. 绘制游戏元素 ---
        draw_board()
        draw_pieces(board)

        # 显示当前轮到哪一方
        if game_state != GAME_OVER:
            turn_text = "黑方回合" if current_player == BLACK_TURN else "白方回合"
            text_surface = small_font.render(turn_text, True, BLACK)
            screen.blit(text_surface, (10, 10))

        # --- 6. 游戏结束处理 ---
        if game_state == GAME_OVER:
            screen.fill(BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), special_flags=pygame.BLEND_RGBA_MULT)
            winner_text = "黑方获胜!" if winner == BLACK_TURN else "白方获胜!"
            show_message(winner_text, WHITE, y_displace=-30)
            show_message("按 R 键重新开始", WHITE, y_displace=30)

        # 刷新屏幕
        pygame.display.update()
        clock.tick(30)


# --- 启动游戏 ---
if __name__ == '__main__':
    game_loop()