import turtle
def draw_triangle(points, color, my_Turtle):
    my_Turtle.fillcolor(color)
    my_Turtle.up()
    my_Turtle.goto(points[0][0], points[0][1])
    my_Turtle.down()
    my_Turtle.begin_fill()
    my_Turtle.goto(points[1][0], points[1][1])
    my_Turtle.goto(points[2][0], points[2][1])
    my_Turtle.goto(points[0][0], points[0][1])
    my_Turtle.end_fill()

def get_mid(p1, p2):
    return [(p1[0] + p2[0]) / 2 , (p1[1] + p2[1]) / 2]

def sieropinski(points, degree, my_Turtle):
    colormap = ["red", "green", "blue", "yellow", "orange", "green"]
    draw_triangle(points, colormap[degree], my_Turtle)
    if degree > 0:
        sieropinski([points[0],get_mid(points[0],points[1]), get_mid(points[0], points[2])], degree - 1, my_Turtle)
        sieropinski([points[1],get_mid(points[1],points[0]), get_mid(points[1], points[2])], degree - 1, my_Turtle)
        sieropinski([points[2],get_mid(points[2],points[0]), get_mid(points[2], points[1])], degree - 1, my_Turtle)
def main():
    my_Turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_points = [[-100,-50] , [0, 50] , [100, -50]]
    sieropinski(my_points, 5, my_Turtle)
    my_win.exitonclick()
main()