def to_string(n , base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_string(n // base , base) + convert_string[n % base]
print(to_string(10, 2))

import turtle

#用海龟绘图递归绘制螺旋线
def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)

my_turtle = turtle.Turtle()
my_win = turtle.Screen()
draw_spiral(my_turtle,100)
my_win.exitonclick()

