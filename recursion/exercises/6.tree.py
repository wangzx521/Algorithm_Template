from turtle import *
import random
def tree(branch_len, t):
    if branch_len <3:
        return
    if branch_len < 6:
        t.color("green")
    t.width(5 * branch_len / 20)
    t.forward(branch_len)
    angle1 = 15 + 30 * random.random()
    t.right(angle1)
    tree(branch_len - random.randint(3, 4), t)
    t.left(angle1)
    angle2 = 15 + 30 * random.random()
    t.left(angle2)
    tree(branch_len - random.randint(3, 4), t)
    t.right(angle2 )
    t.backward(branch_len)
    t.color("black")
    
my_Turtle = Turtle()
my_Turtle.left(90)
my_window = Screen()
tree(30, my_Turtle)

my_window.exitonclick()