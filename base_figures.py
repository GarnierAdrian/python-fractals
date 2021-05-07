from math import sqrt


def square(func, turtle, length, level):
    turtle.penup()
    turtle.right(180)
    turtle.forward(length/2)
    turtle.right(90)
    turtle.forward(length/2)
    turtle.right(90)
    turtle.pendown()
    turtle.right(90)
    func(turtle, level,length)
    turtle.left(90)
    func(turtle, level,length)
    turtle.left(90)
    func(turtle, level,length)
    turtle.left(90)
    func(turtle, level,length)
    turtle.penup()
    turtle.left(180)
    turtle.forward(length/2)
    turtle.right(90)
    turtle.forward(length/2)
    turtle.left(90)
    turtle.pendown()



def triangle(turtle, func, length, level):
    h = sqrt(length**2 + (length/2)**2)
    turtle.penup()
    turtle.left(90)
    turtle.forward(h/2)
    turtle.right(210)
    turtle.pendown()
    func(turtle, level,length)
    turtle.left(120)
    func(turtle, level,length)
    turtle.left(120)
    func(turtle, level,length)
    turtle.penup()
    turtle.left(150)
    turtle.forward(h/2)
    turtle.left(90)
    turtle.pendown()

def david_star(turtle, func, length, level):
    triangle(turtle, func, length, level)
    turtle.left(180)
    triangle(turtle, func, length, level)
    turtle.left(180)