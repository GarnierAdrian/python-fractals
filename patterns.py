def dip(turtle, level=0, len=10):
    if(level==0):
        turtle.forward(len)
    else:
        dip(turtle,level-1,len/3)
        turtle.right(90)
        dip(turtle,level-1,len/3)
        turtle.left(90)
        dip(turtle,level-1,len/3)
        turtle.left(90)
        dip(turtle,level-1,len/3)
        turtle.right(90)
        dip(turtle,level-1,len/3)

def bump(turtle, level=0, len=10):
    if(level==0):
        turtle.forward(len)
    else:
        bump(turtle,level-1,len/3)
        turtle.left(90)
        bump(turtle,level-1,len/3)
        turtle.right(90)
        bump(turtle,level-1,len/3)
        turtle.right(90)
        bump(turtle,level-1,len/3)
        turtle.left(90)
        bump(turtle,level-1,len/3)

def double_bump(turtle, level=0, len=10):
    if(level==0):
        turtle.forward(len)
    else:
        turtle.left(90)
        bump(turtle,level-1,len/3)
        turtle.right(90)
        bump(turtle,level-1,len/3)
        turtle.right(90)
        bump(turtle,level-1,len/3)
        turtle.left(90)
        bump(turtle,level-1,len/3)
        turtle.left(90)
        bump(turtle,level-1,len/3)
        turtle.right(90)
        bump(turtle,level-1,len/3)
        turtle.right(90)
        bump(turtle,level-1,len/3)
        turtle.left(90)

def double_dip(turtle, level=0, len=10):
    if(level==0):
        turtle.forward(len)
    else:
        turtle.right(90)
        bump(turtle,level-1,len/3)
        turtle.left(90)
        bump(turtle,level-1,len/3)
        turtle.left(90)
        bump(turtle,level-1,len/3)
        turtle.right(90)
        bump(turtle,level-1,len/3)
        turtle.right(90)
        bump(turtle,level-1,len/3)
        turtle.left(90)
        bump(turtle,level-1,len/3)
        turtle.left(90)
        bump(turtle,level-1,len/3)
        turtle.right(90)
        
def swiggle(turtle, level=0, len=10):
    if(level==0):
        turtle.forward(len)
    else:
        turtle.left(90)
        swiggle(turtle,level-1, len/2)
        turtle.right(90)
        swiggle(turtle,level-1, len/2)
        turtle.right(90)
        swiggle(turtle,level-1, len/2)
        swiggle(turtle,level-1, len/2)
        turtle.left(90)
        swiggle(turtle,level-1, len/2)
        turtle.left(90)
        swiggle(turtle,level-1, len/2)
        turtle.right(90)

def spike(turtle, level=0, len=10):
    if(level==0):
        turtle.forward(len)
    else:
        turtle.right(60)
        spike(turtle,level-1, len/2)
        turtle.left(120)
        spike(turtle,level-1, len/2)
        turtle.right(60)

def reverse_spike(turtle, level=0, len=10):
    if(level==0):
        turtle.forward(len)
    else:
        turtle.left(60)
        reverse_spike(turtle,level-1, len/2)
        turtle.right(120)
        reverse_spike(turtle,level-1, len/2)
        turtle.left(60)
