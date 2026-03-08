import pygame
import sys
import os

# 初始化Pygame
pygame.init()

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)
GREEN = (0, 200, 0, 150)  # 半透明绿色，用于高亮
RED = (255, 0, 0, 150)  # 半透明红色，用于危险移动
BLUE = (0, 100, 255, 150)  # 半透明蓝色，用于最后移动

# 游戏设置
BOARD_SIZE = 8
SQUARE_SIZE = 80
WINDOW_SIZE = SQUARE_SIZE * BOARD_SIZE + 200
INFO_PANEL_WIDTH = 200

# 创建窗口
screen = pygame.display.set_mode((WINDOW_SIZE, SQUARE_SIZE * BOARD_SIZE))
pygame.display.set_caption("国际象棋")

# 字体
font = pygame.font.SysFont(None, 24)
title_font = pygame.font.SysFont(None, 36)
info_font = pygame.font.SysFont(None, 20)


class Piece:
    def __init__(self, type, color, position):
        self.type = type
        self.color = color
        self.position = position
        self.has_moved = False

    def __repr__(self):
        return f"{self.color[0].upper()}{self.type.upper()}"

    def get_image_name(self):
        """获取棋子图片文件名"""
        return f"{self.color}_{self.type}.png"


class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.current_player = "white"
        self.selected_piece = None
        self.valid_moves = []
        self.last_move = None
        self.check = False
        self.checkmate = False
        self.stalemate = False
        self.move_history = []
        self.captured_pieces = {"white": [], "black": []}

        # 初始化棋子
        self.setup_pieces()

    def setup_pieces(self):
        """设置初始棋盘"""
        # 摆放黑棋
        self.board[0][0] = Piece("rook", "black", (0, 0))
        self.board[0][1] = Piece("knight", "black", (0, 1))
        self.board[0][2] = Piece("bishop", "black", (0, 2))
        self.board[0][3] = Piece("queen", "black", (0, 3))
        self.board[0][4] = Piece("king", "black", (0, 4))
        self.board[0][5] = Piece("bishop", "black", (0, 5))
        self.board[0][6] = Piece("knight", "black", (0, 6))
        self.board[0][7] = Piece("rook", "black", (0, 7))

        for i in range(8):
            self.board[1][i] = Piece("pawn", "black", (1, i))

        # 摆放白棋
        self.board[7][0] = Piece("rook", "white", (7, 0))
        self.board[7][1] = Piece("knight", "white", (7, 1))
        self.board[7][2] = Piece("bishop", "white", (7, 2))
        self.board[7][3] = Piece("queen", "white", (7, 3))
        self.board[7][4] = Piece("king", "white", (7, 4))
        self.board[7][5] = Piece("bishop", "white", (7, 5))
        self.board[7][6] = Piece("knight", "white", (7, 6))
        self.board[7][7] = Piece("rook", "white", (7, 7))

        for i in range(8):
            self.board[6][i] = Piece("pawn", "white", (6, i))

    def get_piece(self, position):
        """获取指定位置的棋子"""
        row, col = position
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        return None

    def is_valid_position(self, position):
        """检查位置是否在棋盘内"""
        row, col = position
        return 0 <= row < 8 and 0 <= col < 8

    def get_all_valid_moves(self, color):
        """获取某个颜色所有棋子的所有合法移动"""
        all_moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color == color:
                    moves = self.get_piece_moves((row, col))
                    all_moves.extend([((row, col), move) for move in moves])
        return all_moves

    def is_in_check(self, color):
        """检查某方是否被将军"""
        # 找到国王的位置
        king_pos = None
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.type == "king" and piece.color == color:
                    king_pos = (row, col)
                    break
            if king_pos:
                break

        if not king_pos:
            return False

        # 检查对方是否有棋子可以攻击国王
        opponent_color = "black" if color == "white" else "white"
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color == opponent_color:
                    if king_pos in self.get_piece_attacks((row, col)):
                        return True
        return False

    def get_piece_attacks(self, position):
        """获取棋子可以攻击的位置（不考虑是否会导致自己被将军）"""
        row, col = position
        piece = self.get_piece(position)
        if not piece:
            return []

        attacks = []
        if piece.type == "pawn":
            # 兵的攻击方向
            direction = -1 if piece.color == "white" else 1
            # 左前方
            if self.is_valid_position((row + direction, col - 1)):
                attacks.append((row + direction, col - 1))
            # 右前方
            if self.is_valid_position((row + direction, col + 1)):
                attacks.append((row + direction, col + 1))

        elif piece.type == "knight":
            # 马的8个L形移动
            moves = [
                (row + 2, col + 1), (row + 2, col - 1),
                (row - 2, col + 1), (row - 2, col - 1),
                (row + 1, col + 2), (row + 1, col - 2),
                (row - 1, col + 2), (row - 1, col - 2)
            ]
            for move in moves:
                if self.is_valid_position(move):
                    attacks.append(move)

        elif piece.type == "bishop" or piece.type == "queen":
            # 主教的斜线移动
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while self.is_valid_position((r, c)):
                    attacks.append((r, c))
                    if self.get_piece((r, c)):
                        break
                    r += dr
                    c += dc

        if piece.type == "rook" or piece.type == "queen":
            # 车的直线移动
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while self.is_valid_position((r, c)):
                    attacks.append((r, c))
                    if self.get_piece((r, c)):
                        break
                    r += dr
                    c += dc

        elif piece.type == "king":
            # 国王的8个方向移动
            moves = [
                (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                (row, col - 1), (row, col + 1),
                (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
            ]
            for move in moves:
                if self.is_valid_position(move):
                    attacks.append(move)

        return attacks

    def get_piece_moves(self, position):
        """获取棋子的合法移动（考虑将军）"""
        row, col = position
        piece = self.get_piece(position)
        if not piece or piece.color != self.current_player:
            return []

        moves = []

        if piece.type == "pawn":
            # 兵的移动
            direction = -1 if piece.color == "white" else 1
            start_row = 6 if piece.color == "white" else 1

            # 向前移动一格
            if self.is_valid_position((row + direction, col)) and not self.get_piece((row + direction, col)):
                moves.append((row + direction, col))

                # 向前移动两格（第一次移动）
                if row == start_row and not self.get_piece((row + 2 * direction, col)):
                    moves.append((row + 2 * direction, col))

            # 吃子
            for dc in [-1, 1]:
                target_pos = (row + direction, col + dc)
                if self.is_valid_position(target_pos):
                    target_piece = self.get_piece(target_pos)
                    if target_piece and target_piece.color != piece.color:
                        moves.append(target_pos)

        elif piece.type == "knight":
            # 马的L形移动
            knight_moves = [
                (row + 2, col + 1), (row + 2, col - 1),
                (row - 2, col + 1), (row - 2, col - 1),
                (row + 1, col + 2), (row + 1, col - 2),
                (row - 1, col + 2), (row - 1, col - 2)
            ]
            for move in knight_moves:
                if self.is_valid_position(move):
                    target_piece = self.get_piece(move)
                    if not target_piece or target_piece.color != piece.color:
                        moves.append(move)

        elif piece.type == "bishop":
            # 主教的斜线移动
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while self.is_valid_position((r, c)):
                    target_piece = self.get_piece((r, c))
                    if not target_piece:
                        moves.append((r, c))
                    elif target_piece.color != piece.color:
                        moves.append((r, c))
                        break
                    else:
                        break
                    r += dr
                    c += dc

        elif piece.type == "rook":
            # 车的直线移动
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while self.is_valid_position((r, c)):
                    target_piece = self.get_piece((r, c))
                    if not target_piece:
                        moves.append((r, c))
                    elif target_piece.color != piece.color:
                        moves.append((r, c))
                        break
                    else:
                        break
                    r += dr
                    c += dc

        elif piece.type == "queen":
            # 皇后的所有方向移动
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while self.is_valid_position((r, c)):
                    target_piece = self.get_piece((r, c))
                    if not target_piece:
                        moves.append((r, c))
                    elif target_piece.color != piece.color:
                        moves.append((r, c))
                        break
                    else:
                        break
                    r += dr
                    c += dc

        elif piece.type == "king":
            # 国王的移动
            king_moves = [
                (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                (row, col - 1), (row, col + 1),
                (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
            ]
            for move in king_moves:
                if self.is_valid_position(move):
                    target_piece = self.get_piece(move)
                    if not target_piece or target_piece.color != piece.color:
                        moves.append(move)

            # 王车易位
            if not piece.has_moved and not self.is_in_check(piece.color):
                # 短易位（国王侧）
                rook = self.get_piece((row, 7))
                if rook and rook.type == "rook" and not rook.has_moved:
                    if (not self.get_piece((row, 5)) and
                            not self.get_piece((row, 6)) and
                            not self.is_position_under_attack((row, 5), piece.color) and
                            not self.is_position_under_attack((row, 6), piece.color)):
                        moves.append((row, 6))

                # 长易位（皇后侧）
                rook = self.get_piece((row, 0))
                if rook and rook.type == "rook" and not rook.has_moved:
                    if (not self.get_piece((row, 1)) and
                            not self.get_piece((row, 2)) and
                            not self.get_piece((row, 3)) and
                            not self.is_position_under_attack((row, 2), piece.color) and
                            not self.is_position_under_attack((row, 3), piece.color)):
                        moves.append((row, 2))

        # 过滤掉会导致自己被将军的移动
        valid_moves = []
        for move in moves:
            # 模拟移动
            original_piece = self.get_piece(move)
            self.move_piece_simulate(position, move)

            # 检查移动后是否被将军
            if not self.is_in_check(piece.color):
                valid_moves.append(move)

            # 撤销模拟移动
            self.undo_move_simulate(position, move, original_piece)

        return valid_moves

    def is_position_under_attack(self, position, color):
        """检查某个位置是否被对方攻击"""
        opponent_color = "black" if color == "white" else "white"

        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color == opponent_color:
                    if position in self.get_piece_attacks((row, col)):
                        return True
        return False

    def move_piece_simulate(self, from_pos, to_pos):
        """模拟移动棋子（不记录历史）"""
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        piece = self.board[from_row][from_col]
        captured_piece = self.board[to_row][to_col]

        # 执行移动
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = None

        if piece:
            piece.position = (to_row, to_col)

            # 王车易位
            if piece.type == "king" and abs(to_col - from_col) == 2:
                # 短易位
                if to_col > from_col:
                    rook = self.board[to_row][7]
                    if rook:
                        self.board[to_row][5] = rook
                        self.board[to_row][7] = None
                        rook.position = (to_row, 5)
                # 长易位
                else:
                    rook = self.board[to_row][0]
                    if rook:
                        self.board[to_row][3] = rook
                        self.board[to_row][0] = None
                        rook.position = (to_row, 3)

        return captured_piece

    def undo_move_simulate(self, from_pos, to_pos, original_piece):
        """撤销模拟移动"""
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        piece = self.board[to_row][to_col]

        # 撤销移动
        self.board[from_row][from_col] = piece
        self.board[to_row][to_col] = original_piece

        if piece:
            piece.position = (from_row, from_col)

            # 撤销王车易位
            if piece.type == "king" and abs(to_col - from_col) == 2:
                # 撤销短易位
                if to_col > from_col:
                    rook = self.board[from_row][5]
                    if rook:
                        self.board[from_row][7] = rook
                        self.board[from_row][5] = None
                        rook.position = (from_row, 7)
                # 撤销长易位
                else:
                    rook = self.board[from_row][3]
                    if rook:
                        self.board[from_row][0] = rook
                        self.board[from_row][3] = None
                        rook.position = (from_row, 0)

    def move_piece(self, from_pos, to_pos):
        """移动棋子"""
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        piece = self.board[from_row][from_col]
        captured_piece = self.board[to_row][to_col]

        if not piece:
            return False

        # 记录移动
        move_record = {
            "from": from_pos,
            "to": to_pos,
            "piece": piece,
            "captured": captured_piece,
            "had_moved": piece.has_moved
        }

        # 执行移动
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = None
        piece.position = (to_row, to_col)
        piece.has_moved = True

        # 处理王车易位
        if piece.type == "king" and abs(to_col - from_col) == 2:
            # 短易位
            if to_col > from_col:
                rook = self.board[to_row][7]
                if rook:
                    self.board[to_row][5] = rook
                    self.board[to_row][7] = None
                    rook.position = (to_row, 5)
                    rook.has_moved = True
            # 长易位
            else:
                rook = self.board[to_row][0]
                if rook:
                    self.board[to_row][3] = rook
                    self.board[to_row][0] = None
                    rook.position = (to_row, 3)
                    rook.has_moved = True

        # 兵的升变
        if piece.type == "pawn" and (to_row == 0 or to_row == 7):
            # 自动升变为皇后
            piece.type = "queen"

        # 记录被吃的棋子
        if captured_piece:
            self.captured_pieces[self.current_player].append(captured_piece)

        # 记录移动历史
        self.move_history.append(move_record)
        self.last_move = (from_pos, to_pos)

        # 切换玩家
        self.current_player = "black" if self.current_player == "white" else "white"

        # 检查将军和将死
        self.check = self.is_in_check(self.current_player)

        # 检查将死
        if self.check:
            all_moves = self.get_all_valid_moves(self.current_player)
            if len(all_moves) == 0:
                self.checkmate = True

        # 检查和棋
        if not self.check:
            all_moves = self.get_all_valid_moves(self.current_player)
            if len(all_moves) == 0:
                self.stalemate = True

        return True

    def select_piece(self, position):
        """选择棋子"""
        piece = self.get_piece(position)

        if piece and piece.color == self.current_player:
            self.selected_piece = position
            self.valid_moves = self.get_piece_moves(position)
            return True
        return False

    def is_game_over(self):
        """检查游戏是否结束"""
        return self.checkmate or self.stalemate

    def get_game_state(self):
        """获取游戏状态文本"""
        if self.checkmate:
            winner = "白方" if self.current_player == "black" else "黑方"
            return f"将死！{winner}获胜！"
        elif self.stalemate:
            return "和棋！"
        elif self.check:
            return f"{'白方' if self.current_player == 'white' else '黑方'}被将军！"
        else:
            return f"轮到{'白方' if self.current_player == 'white' else '黑方'}走棋"

    def draw(self, screen, images):
        """绘制棋盘和棋子"""
        # 绘制棋盘
        for row in range(8):
            for col in range(8):
                color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
                pygame.draw.rect(screen, color,
                                 (col * SQUARE_SIZE, row * SQUARE_SIZE,
                                  SQUARE_SIZE, SQUARE_SIZE))

        # 高亮最后一步移动
        if self.last_move:
            from_pos, to_pos = self.last_move
            for pos in [from_pos, to_pos]:
                row, col = pos
                s = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
                s.fill(BLUE)
                screen.blit(s, (col * SQUARE_SIZE, row * SQUARE_SIZE))

        # 高亮被选中的棋子
        if self.selected_piece:
            row, col = self.selected_piece
            s = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
            s.fill(GREEN)
            screen.blit(s, (col * SQUARE_SIZE, row * SQUARE_SIZE))

        # 高亮合法移动
        for move in self.valid_moves:
            row, col = move
            s = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
            # 检查这个位置是否有对方棋子
            piece = self.get_piece(move)
            if piece and piece.color != self.current_player:
                s.fill(RED)  # 吃子用红色高亮
            else:
                s.fill((0, 255, 0, 100))  # 普通移动用浅绿色高亮
            screen.blit(s, (col * SQUARE_SIZE, row * SQUARE_SIZE))

        # 绘制棋子
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece:
                    image = images.get(piece.get_image_name())
                    if image:
                        screen.blit(image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
                    else:
                        # 如果没有图片，用文字代替
                        piece_chars = {
                            "king": "♔♚", "queen": "♕♛", "rook": "♖♜",
                            "bishop": "♗♝", "knight": "♘♞", "pawn": "♙♟"
                        }
                        char_index = 0 if piece.color == "white" else 1
                        char = piece_chars[piece.type][char_index]
                        text = font.render(char, True, BLACK if piece.color == "white" else WHITE)
                        text_rect = text.get_rect(center=(
                            col * SQUARE_SIZE + SQUARE_SIZE // 2,
                            row * SQUARE_SIZE + SQUARE_SIZE // 2
                        ))
                        screen.blit(text, text_rect)

        # 绘制信息面板
        info_panel_x = 8 * SQUARE_SIZE
        pygame.draw.rect(screen, (50, 50, 50),
                         (info_panel_x, 0, INFO_PANEL_WIDTH, 8 * SQUARE_SIZE))

        # 显示游戏状态
        state_text = self.get_game_state()
        state_surface = title_font.render(state_text, True, WHITE)
        screen.blit(state_surface, (info_panel_x + 10, 20))

        # 显示当前玩家
        player_text = f"当前玩家: {'白方' if self.current_player == 'white' else '黑方'}"
        player_surface = font.render(player_text, True, WHITE)
        screen.blit(player_surface, (info_panel_x + 10, 70))

        # 显示被吃掉的棋子
        white_captured = self.captured_pieces["white"]
        black_captured = self.captured_pieces["black"]

        white_text = font.render("白方吃掉:", True, WHITE)
        screen.blit(white_text, (info_panel_x + 10, 120))

        for i, piece in enumerate(white_captured[:10]):
            piece_text = info_font.render(f"{piece.type} ({piece.color})", True, WHITE)
            screen.blit(piece_text, (info_panel_x + 20, 150 + i * 20))

        black_text = font.render("黑方吃掉:", True, WHITE)
        screen.blit(black_text, (info_panel_x + 10, 350))

        for i, piece in enumerate(black_captured[:10]):
            piece_text = info_font.render(f"{piece.type} ({piece.color})", True, WHITE)
            screen.blit(piece_text, (info_panel_x + 20, 380 + i * 20))

        # 显示移动历史
        history_text = font.render("最近移动:", True, WHITE)
        screen.blit(history_text, (info_panel_x + 10, 550))

        for i, move in enumerate(self.move_history[-5:]):
            from_pos = move["from"]
            to_pos = move["to"]
            piece = move["piece"]
            move_str = f"{piece.color[0]}{piece.type[0]} {chr(97 + from_pos[1])}{8 - from_pos[0]}→{chr(97 + to_pos[1])}{8 - to_pos[0]}"
            move_surface = info_font.render(move_str, True, WHITE)
            screen.blit(move_surface, (info_panel_x + 20, 580 + i * 20))

        # 显示操作说明
        instructions = [
            "操作说明:",
            "- 点击棋子选择",
            "- 点击高亮格子移动",
            "- R: 重新开始游戏",
            "- U: 撤销一步",
            "- ESC: 退出游戏"
        ]

        for i, line in enumerate(instructions):
            instr_surface = info_font.render(line, True, WHITE)
            screen.blit(instr_surface, (info_panel_x + 10, 680 + i * 20))


def load_piece_images():
    """加载棋子图片"""
    images = {}

    # 棋子类型和颜色
    piece_types = ["king", "queen", "rook", "bishop", "knight", "pawn"]
    colors = ["white", "black"]

    for color in colors:
        for piece_type in piece_types:
            filename = f"{color}_{piece_type}.png"
            # 尝试加载图片文件
            try:
                # 这里我们创建简单的占位图片
                image = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)

                # 绘制圆形棋子
                piece_color = WHITE if color == "white" else (50, 50, 50)
                border_color = (200, 200, 200) if color == "white" else BLACK

                pygame.draw.circle(image, piece_color,
                                   (SQUARE_SIZE // 2, SQUARE_SIZE // 2),
                                   SQUARE_SIZE // 2 - 5)
                pygame.draw.circle(image, border_color,
                                   (SQUARE_SIZE // 2, SQUARE_SIZE // 2),
                                   SQUARE_SIZE // 2 - 5, 2)

                # 添加棋子文字
                piece_chars = {
                    "king": "K", "queen": "Q", "rook": "R",
                    "bishop": "B", "knight": "N", "pawn": "P"
                }
                char = piece_chars[piece_type]
                text_color = BLACK if color == "white" else WHITE
                text = font.render(char, True, text_color)
                text_rect = text.get_rect(center=(SQUARE_SIZE // 2, SQUARE_SIZE // 2))
                image.blit(text, text_rect)

                images[filename] = image

            except Exception as e:
                print(f"无法加载图片 {filename}: {e}")

    return images


def main():
    clock = pygame.time.Clock()
    board = ChessBoard()
    images = load_piece_images()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    # 重新开始游戏
                    board = ChessBoard()
                elif event.key == pygame.K_u:
                    # 撤销一步
                    if board.move_history:
                        last_move = board.move_history.pop()

                        # 恢复棋盘状态
                        from_pos = last_move["from"]
                        to_pos = last_move["to"]
                        piece = last_move["piece"]
                        captured = last_move["captured"]
                        had_moved = last_move["had_moved"]

                        # 移动棋子回原处
                        from_row, from_col = from_pos
                        to_row, to_col = to_pos

                        board.board[from_row][from_col] = piece
                        board.board[to_row][to_col] = captured
                        piece.position = from_pos
                        piece.has_moved = had_moved

                        # 撤销王车易位
                        if piece.type == "king" and abs(to_col - from_col) == 2:
                            if to_col > from_col:  # 短易位
                                rook = board.board[to_row][5]
                                if rook:
                                    board.board[to_row][7] = rook
                                    board.board[to_row][5] = None
                                    rook.position = (to_row, 7)
                                    rook.has_moved = False
                            else:  # 长易位
                                rook = board.board[to_row][3]
                                if rook:
                                    board.board[to_row][0] = rook
                                    board.board[to_row][3] = None
                                    rook.position = (to_row, 0)
                                    rook.has_moved = False

                        # 从被吃棋子列表中移除
                        if captured:
                            for player in ["white", "black"]:
                                if captured in board.captured_pieces[player]:
                                    board.captured_pieces[player].remove(captured)

                        # 切换玩家
                        board.current_player = "white" if board.current_player == "black" else "white"

                        # 更新游戏状态
                        board.selected_piece = None
                        board.valid_moves = []
                        board.check = board.is_in_check(board.current_player)
                        board.checkmate = False
                        board.stalemate = False

                        if board.move_history:
                            board.last_move = (board.move_history[-1]["from"], board.move_history[-1]["to"])
                        else:
                            board.last_move = None

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos

                # 检查是否点击了棋盘区域
                if x < 8 * SQUARE_SIZE:
                    col = x // SQUARE_SIZE
                    row = y // SQUARE_SIZE
                    position = (row, col)

                    if board.selected_piece:
                        # 如果已经选择了棋子，尝试移动
                        if position in board.valid_moves:
                            board.move_piece(board.selected_piece, position)
                            board.selected_piece = None
                            board.valid_moves = []
                        else:
                            # 尝试选择其他棋子
                            board.select_piece(position)
                    else:
                        # 选择棋子
                        board.select_piece(position)

        # 绘制
        screen.fill((30, 30, 30))
        board.draw(screen, images)

        # 显示游戏结束信息
        if board.is_game_over():
            game_over_text = title_font.render(board.get_game_state(), True, RED)
            text_rect = game_over_text.get_rect(center=(4 * SQUARE_SIZE, 4 * SQUARE_SIZE))

            # 创建半透明背景
            s = pygame.Surface((6 * SQUARE_SIZE, 3 * SQUARE_SIZE), pygame.SRCALPHA)
            s.fill((0, 0, 0, 200))
            screen.blit(s, (SQUARE_SIZE, 3.5 * SQUARE_SIZE))

            screen.blit(game_over_text, text_rect)

            restart_text = font.render("按R键重新开始游戏", True, WHITE)
            restart_rect = restart_text.get_rect(center=(4 * SQUARE_SIZE, 5 * SQUARE_SIZE))
            screen.blit(restart_text, restart_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()