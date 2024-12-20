import turtle
START = "S"
OBSTAClE = "+"
TRIED = "."
DEAD_END = "-"
PART_OF_FILE = "0"
class Maze:
    def __init__(self, maze_filename) -> None:
        with open(maze_filename, "r") as f:
            self.maze_list = [
                [ch for ch in line.strip()]
                for line in f.readlines()
                ]
            self.rows_in_maze = len(self.maze_list)
            self.columns_in_maze = len(self.maze_list[0])
            for row_idx , row in enumerate(self.maze_list):
                if START in row:
                    self.start_row = row_idx
                    self.start_col = row.index(START) 
                    break
            self.x_translate = -self.columns_in_maze / 2
            self.y_translate = self.rows_in_maze / 2
            self.t = turtle.Turtle()
            self.t.shape("turtle")
            self.wn = turtle.Screen()
            self.wn.setworldcoordinates(
                -(self.columns_in_maze - 1) / 2 - 0.5,
                -(self.rows_in_maze - 1) / 2 - 0.5,
                (self.columns_in_maze - 1) / 2 + 0.5,
                (self.rows_in_maze - 1) / 2 + 0.5
            )
    def draw_maze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTAClE:
                    self.draw_centered_box(x + self.x_translate,
                                           -y + self.y_translate,
                                             "gray")
        self.t.color("black")
        self.t.fillcolor("blue")
        self.wn.update()
        self.wn.tracer(1)
    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x - 0.5 , y - 0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
    def update_position(self, row, col, val = None):
        if val :
            self.maze_list[row][col] = val
        self.move_turtle(col, row)
        if val == PART_OF_PATH:
            color = "green"
        elif val == OBSTAClE:
            color = "red"
        elif val == TRIED:
            color = "black"
        elif val == DEAD_END:
            color = "red"
        else:
            color = None
        if color:
            self.dotr444