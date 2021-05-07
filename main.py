import turtle
from base_figures import *
from patterns import * 

width,height=4000,4000
turtle.tracer(False)

turtle.Screen().bgcolor("black")
s = turtle.getscreen()
s.screensize(width,height)
s.colormode(255)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
filler= turtle.Turtle()
filler.speed(0)

filler.fillcolor('black')
filler.begin_fill()
filler.setpos(height/2-height,width/2)
filler.forward(width)
filler.right(90)
filler.forward(height)
filler.right(90)
filler.forward(width)
filler.right(90)
filler.forward(height)
filler.end_fill()
filler.hideturtle()
s.update()


def fill_background(width, length):
    pass

length = 550
level = 4


t.pencolor(143,134,25)
david_star(t, double_bump, length, level)
turtle.update()

t.pencolor(225,213,72)
david_star(t, double_dip, length, level)
turtle.update()

t.pencolor(173,164,55)
david_star(t, dip, length, level)
turtle.update()

t.pencolor(230,222,142)
david_star(t, bump, length, level)
turtle.update()

input()

canvas = s.getcanvas()
canvas.postscript(file='fractal.ps', colormode='color')
