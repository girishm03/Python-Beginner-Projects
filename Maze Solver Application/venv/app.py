import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from matplotlib.widgets import Button


def parse_grid(grid_lines):
    return [[int(ch) for ch in row] for row in grid_lines]

LEVELS = [
    {
        "maze": parse_grid([
            "01000",
            "01010",
            "00010",
            "01110",
            "00000"
        ]),
        "start": (0, 0),
        "end": (4, 4)
    },
    {
        "maze": parse_grid([
            "010100",
            "010001",
            "000101",
            "011001",
            "000000",
            "011100"
        ]),
        "start": (0, 0),
        "end": (5, 5)
    },
    {
        "maze": parse_grid([
            "0010100",
            "0110101",
            "0000100",
            "0111101",
            "0100001",
            "0101111",
            "0000000"
        ]),
        "start": (0, 0),
        "end": (6, 6)
    },
    {
        "maze": parse_grid([
            "00000000",
            "01111110",
            "01010000",
            "01010111",
            "01010001",
            "01011101",
            "01000000",
            "01111110"
        ]),
        "start": (0, 0),
        "end": (7, 7)
    },
    {
        "maze": parse_grid([
            "010101000",
            "010101010",
            "010001010",
            "011101010",
            "000001010",
            "011111010",
            "010000010",
            "010111110",
            "000000000"
        ]),
        "start": (0, 0),
        "end": (8, 8)
    }
]

MOVES = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "w": (-1, 0),
    "s": (1, 0),
    "a": (0, -1),
    "d": (0, 1)
}


def is_safe(maze, row, col):
    return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == 0


class MazeGame:
    def __init__(self, levels):
        self.levels = levels
        self.level_index = 0
        self.fig, self.ax = plt.subplots(figsize=(7, 7))
        self.reset_ax = self.fig.add_axes([0.37, 0.01, 0.26, 0.05])
        self.reset_button = Button(self.reset_ax, "Reset")
        self.reset_button.on_clicked(self.reset_game)
        self.fig.canvas.mpl_connect("key_press_event", self.on_key)
        self.start_level()

    def start_level(self):
        level = self.levels[self.level_index]
        self.maze = level["maze"]
        self.start = level["start"]
        self.end = level["end"]
        self.player = self.start
        self.path = [self.start]
        self.level_complete = False
        self.win = False
        self.nrows = len(self.maze)
        self.ncols = len(self.maze[0])
        self.message = "Use arrow keys / WASD to move. R = restart, B = beginning, Q = quit."
        self.draw_maze()

    def draw_maze(self):
        self.ax.clear()
        self.ax.imshow(self.maze, cmap="binary", origin="upper")

        for row, col in self.path:
            self.ax.add_patch(Circle((col, row), 0.15, color="red", alpha=0.4))

        self.ax.add_patch(Rectangle((self.end[1] - 0.4, self.end[0] - 0.4), 0.8, 0.8,
                                   facecolor="green", alpha=0.5))
        self.ax.add_patch(Circle((self.player[1], self.player[0]), 0.3, color="blue"))

        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_xticks([x - 0.5 for x in range(1, self.ncols)], minor=True)
        self.ax.set_yticks([y - 0.5 for y in range(1, self.nrows)], minor=True)
        self.ax.grid(which="minor", color="black", linestyle="-", linewidth=1)

        level_text = f"Maze Level {self.level_index + 1}/{len(self.levels)} (Normal)"
        if self.win:
            title = "Congrats! You have completed all the levels. If you want to try again please click on reset."
        elif self.level_complete:
            title = f"{level_text} — Level complete! Press N for next level, B for beginning, or Reset."
        else:
            title = f"{level_text} — {self.message}"

        self.ax.set_title(title)
        self.fig.canvas.draw_idle()

    def on_key(self, event):
        key = event.key.lower() if event.key else ""

        if key in ("q", "escape"):
            plt.close(self.fig)
            return

        if key == "r":
            self.start_level()
            return

        if key == "b":
            self.go_to_beginning()
            return

        if key == "n" and self.level_complete:
            self.next_level()
            return

        if self.win:
            return

        if key in MOVES:
            dr, dc = MOVES[key]
            self.move(dr, dc)

    def move(self, dr, dc):
        new_row = self.player[0] + dr
        new_col = self.player[1] + dc

        if is_safe(self.maze, new_row, new_col):
            self.player = (new_row, new_col)
            self.path.append(self.player)
            if self.player == self.end:
                self.complete_level()
        else:
            self.message = "Blocked! Use a different direction."

        self.draw_maze()

    def complete_level(self):
        self.level_complete = True
        if self.level_index == len(self.levels) - 1:
            self.win = True
            self.message = "Congrats! You have completed all the levels. If you want to try again please click on reset."
        else:
            self.message = "Level finished! Press N to continue or B for beginning."

        self.draw_maze()

    def next_level(self):
        if self.level_index < len(self.levels) - 1:
            self.level_index += 1
            self.start_level()

    def go_to_beginning(self):
        self.level_index = 0
        self.start_level()

    def reset_game(self, event):
        self.go_to_beginning()


def main():
    game = MazeGame(LEVELS)
    plt.show()


if __name__ == "__main__":
    main()
