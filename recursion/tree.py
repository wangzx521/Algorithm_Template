import turtle
import math

def draw_clock(radius):
    # 画表盘
    turtle.penup()
    turtle.goto(- radius, -radius)
    turtle.pendown()
    turtle.circle(radius)

    # 画刻度
    for i in range(12):
        angle = 360 / 12 * i
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        turtle.penup()
        turtle.goto(x - radius, y)
        turtle.pendown()
        turtle.dot(5)
        turtle.setheading(angle)
        if i in [0, 3, 6, 9]:
            turtle.backward(radius / 4)
        else:
            turtle.backward(radius / 16)

    # 画时针
    turtle.penup()
    turtle.goto(-radius, 0)
    turtle.setheading(-60)
    turtle.right(10)
    turtle.pendown()
    turtle.forward(radius * 0.5)
    
    # 画分针
    turtle.penup()
    turtle.goto(-radius, 0)
    turtle.setheading(30)
    turtle.pendown()
    turtle.forward(radius * 0.8)

    # 画秒针
    turtle.penup()
    turtle.goto(-radius, 0)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(radius * 0.9)

def draw_heart(size):
    # 画心形
        turtle.begin_fill()
        turtle.left(140)
        turtle.forward(size)
        turtle.circle(-size/2, 200)
        turtle.left(120)
        turtle.circle(-size/2, 200)
        turtle.forward(size)
        turtle.end_fill()

def draw_clover(size):
    # 画第一个心形
    turtle.fillcolor('red')
    turtle.setheading(0)
    draw_heart(size)
    # 画第二个心形
    turtle.setheading(120)
    draw_heart(size)
    # 画第三个心形
    turtle.setheading(240)
    draw_heart(size)
turtle.tracer(0)
# 设置画布
turtle.speed(5)
turtle.pensize(2)

# 画钟表
turtle.penup()
turtle.goto(-150, 0)  # 将钟表放置在画布左侧
turtle.pendown()
draw_clock(100)

# 画三心草
turtle.penup()
turtle.goto(150, 0)  # 将三心草放置在画布右侧
turtle.pendown()
draw_clover(50)

# 结束
turtle.hideturtle()
turtle.done()
