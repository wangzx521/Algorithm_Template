import turtle
import random

def draw_mountain(start, end, height, depth):
    if depth == 0:
        turtle.penup()
        turtle.goto(start[0], start[1])
        turtle.pendown()
        turtle.goto(end[0], end[1])
    else:
        mid = [(start[0] + end[0]) / 2, (start[1] + end[1]) / 2 + random.uniform(-height, height)]
        draw_mountain(start, mid, height / 2, depth - 1)
        draw_mountain(mid, end, height / 2, depth - 1)

def main():
    turtle.speed(0)  # 设置绘图速度为最快
    turtle.hideturtle()  # 隐藏乌龟光标
    turtle.penup()
    turtle.goto(-200, 0)  # 起始点
    turtle.pendown()

    start = [-200, 0]
    end = [200, 0]
    height = 100  # 初始高度
    depth = 8     # 递归深度

    draw_mountain(start, end, height, depth)
    start = [-300 , -10]
    end = [-300, -10]
    draw_mountain(start, end, height, depth)
    turtle.done()  # 完成绘制，保持窗口打开

if __name__ == "__main__":
    main()
