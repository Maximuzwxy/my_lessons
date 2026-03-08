import tkinter as tk
import random
from tkinter import messagebox


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("贪食蛇游戏")
        self.root.resizable(False, False)

        # 游戏常量
        self.GRID_SIZE = 20
        self.GRID_WIDTH = 30
        self.GRID_HEIGHT = 20
        self.GAME_WIDTH = self.GRID_SIZE * self.GRID_WIDTH
        self.GAME_HEIGHT = self.GRID_SIZE * self.GRID_HEIGHT
        self.SPEED = 100  # 游戏速度（毫秒）

        # 初始化游戏状态
        self.score = 0
        self.direction = "Right"
        self.next_direction = "Right"
        self.game_over = False

        # 创建游戏界面
        self.setup_ui()

        # 初始化蛇和食物
        self.reset_game()

        # 绑定键盘事件
        self.root.bind("<KeyPress>", self.change_direction)

        # 开始游戏
        self.move_snake()

    def setup_ui(self):
        """设置游戏界面"""
        # 分数标签
        self.score_label = tk.Label(
            self.root,
            text=f"得分: 0",
            font=("Arial", 16, "bold")
        )
        self.score_label.pack(pady=5)

        # 游戏画布
        self.canvas = tk.Canvas(
            self.root,
            width=self.GAME_WIDTH,
            height=self.GAME_HEIGHT,
            bg="black",
            highlightthickness=0
        )
        self.canvas.pack(padx=10, pady=5)

        # 控制按钮框架
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # 重新开始按钮
        restart_btn = tk.Button(
            button_frame,
            text="重新开始",
            command=self.reset_game,
            font=("Arial", 10, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=20
        )
        restart_btn.grid(row=0, column=0, padx=10)

        # 退出按钮
        quit_btn = tk.Button(
            button_frame,
            text="退出游戏",
            command=self.root.quit,
            font=("Arial", 10, "bold"),
            bg="#f44336",
            fg="white",
            padx=20
        )
        quit_btn.grid(row=0, column=1, padx=10)

        # 游戏说明
        instructions = tk.Label(
            self.root,
            text="使用方向键或WASD控制蛇的移动\n按空格键暂停/继续游戏",
            font=("Arial", 10),
            fg="gray"
        )
        instructions.pack(pady=5)

    def reset_game(self):
        """重置游戏状态"""
        # 重置游戏变量
        self.score = 0
        self.direction = "Right"
        self.next_direction = "Right"
        self.game_over = False

        # 更新分数显示
        self.score_label.config(text=f"得分: {self.score}")

        # 初始化蛇 - 从中间开始，长度为3
        center_x = self.GRID_WIDTH // 2
        center_y = self.GRID_HEIGHT // 2
        self.snake = [
            (center_x, center_y),
            (center_x - 1, center_y),
            (center_x - 2, center_y)
        ]

        # 生成第一个食物
        self.food = self.generate_food()

        # 清空画布并重新绘制
        self.canvas.delete("all")
        self.draw_snake()
        self.draw_food()

        # 绘制网格（可选，调试用）
        # self.draw_grid()

        # 如果之前暂停了，重新开始移动
        if hasattr(self, 'game_paused'):
            self.move_snake()

    def draw_grid(self):
        """绘制网格（调试用）"""
        for i in range(0, self.GAME_WIDTH, self.GRID_SIZE):
            self.canvas.create_line(i, 0, i, self.GAME_HEIGHT, fill="#222", width=1)
        for i in range(0, self.GAME_HEIGHT, self.GRID_SIZE):
            self.canvas.create_line(0, i, self.GAME_WIDTH, i, fill="#222", width=1)

    def draw_snake(self):
        """绘制蛇"""
        self.canvas.delete("snake")

        # 绘制蛇头
        head_x, head_y = self.snake[0]
        self.canvas.create_rectangle(
            head_x * self.GRID_SIZE,
            head_y * self.GRID_SIZE,
            (head_x + 1) * self.GRID_SIZE,
            (head_y + 1) * self.GRID_SIZE,
            fill="#4CAF50",  # 绿色头部
            outline="#388E3C",
            width=2,
            tags="snake"
        )

        # 绘制蛇身
        for i, (x, y) in enumerate(self.snake[1:], 1):
            # 从头部到尾部颜色渐变
            color_intensity = 200 - (i * 5)
            if color_intensity < 50:
                color_intensity = 50

            color = f"#{color_intensity:02x}{color_intensity + 55:02x}00"

            self.canvas.create_rectangle(
                x * self.GRID_SIZE,
                y * self.GRID_SIZE,
                (x + 1) * self.GRID_SIZE,
                (y + 1) * self.GRID_SIZE,
                fill=color,
                outline="#555",
                width=1,
                tags="snake"
            )

    def draw_food(self):
        """绘制食物"""
        self.canvas.delete("food")
        food_x, food_y = self.food

        # 绘制一个红色的苹果形状
        self.canvas.create_oval(
            food_x * self.GRID_SIZE + 2,
            food_y * self.GRID_SIZE + 2,
            (food_x + 1) * self.GRID_SIZE - 2,
            (food_y + 1) * self.GRID_SIZE - 2,
            fill="#f44336",  # 红色
            outline="#d32f2f",
            width=2,
            tags="food"
        )

        # 添加一个小茎
        self.canvas.create_rectangle(
            food_x * self.GRID_SIZE + 9,
            food_y * self.GRID_SIZE - 3,
            food_x * self.GRID_SIZE + 11,
            food_y * self.GRID_SIZE + 2,
            fill="#8BC34A",  # 绿色
            outline="#689F38",
            width=1,
            tags="food"
        )

    def generate_food(self):
        """生成新食物的位置"""
        while True:
            food_x = random.randint(0, self.GRID_WIDTH - 1)
            food_y = random.randint(0, self.GRID_HEIGHT - 1)

            # 确保食物不会出现在蛇身上
            if (food_x, food_y) not in self.snake:
                return (food_x, food_y)

    def change_direction(self, event):
        """改变蛇的移动方向"""
        key = event.keysym

        # 方向键控制
        if key == "Up" and self.direction != "Down":
            self.next_direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.next_direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.next_direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.next_direction = "Right"

        # WASD控制
        elif key == "w" and self.direction != "Down":
            self.next_direction = "Up"
        elif key == "s" and self.direction != "Up":
            self.next_direction = "Down"
        elif key == "a" and self.direction != "Right":
            self.next_direction = "Left"
        elif key == "d" and self.direction != "Left":
            self.next_direction = "Right"

        # 空格键暂停/继续
        elif key == "space":
            if not self.game_over:
                if hasattr(self, 'game_paused'):
                    self.game_paused = not self.game_paused
                    if not self.game_paused:
                        self.move_snake()
                else:
                    self.game_paused = True

    def move_snake(self):
        """移动蛇"""
        if self.game_over or (hasattr(self, 'game_paused') and self.game_paused):
            return

        # 更新方向
        self.direction = self.next_direction

        # 获取当前蛇头位置
        head_x, head_y = self.snake[0]

        # 根据方向计算新的蛇头位置
        if self.direction == "Up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 1)
        elif self.direction == "Left":
            new_head = (head_x - 1, head_y)
        elif self.direction == "Right":
            new_head = (head_x + 1, head_y)

        # 检查是否撞墙
        if (new_head[0] < 0 or new_head[0] >= self.GRID_WIDTH or
                new_head[1] < 0 or new_head[1] >= self.GRID_HEIGHT):
            self.end_game("撞墙了！")
            return

        # 检查是否撞到自己
        if new_head in self.snake:
            self.end_game("撞到自己了！")
            return

        # 将新头部添加到蛇身
        self.snake.insert(0, new_head)

        # 检查是否吃到食物
        if new_head == self.food:
            # 增加分数
            self.score += 10
            self.score_label.config(text=f"得分: {self.score}")

            # 生成新食物
            self.food = self.generate_food()
            self.draw_food()

            # 每得100分增加速度
            if self.score % 100 == 0 and self.SPEED > 50:
                self.SPEED -= 5
        else:
            # 如果没有吃到食物，移除尾部
            self.snake.pop()

        # 重新绘制蛇
        self.draw_snake()

        # 继续游戏循环
        self.root.after(self.SPEED, self.move_snake)

    def end_game(self, reason):
        """结束游戏"""
        self.game_over = True

        # 显示游戏结束信息
        self.canvas.create_text(
            self.GAME_WIDTH // 2,
            self.GAME_HEIGHT // 2,
            text=f"游戏结束!\n{reason}\n最终得分: {self.score}",
            font=("Arial", 18, "bold"),
            fill="white",
            justify="center"
        )

        # 询问是否重新开始
        play_again = messagebox.askyesno("游戏结束", f"{reason}\n\n最终得分: {self.score}\n\n是否重新开始游戏？")

        if play_again:
            self.reset_game()
        else:
            # 不重新开始，但也不退出，让用户可以选择点击重新开始按钮
            pass


def main():
    # 创建主窗口
    root = tk.Tk()

    # 设置窗口居中
    window_width = 700
    window_height = 550
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # 启动游戏
    game = SnakeGame(root)

    # 启动主循环
    root.mainloop()


if __name__ == "__main__":
    main()