import random as rd
import turtle
X = 0
Y = -300
turtle_list = []

def msg(x, y):
    print("You clicked the turtle", x, y)

def getTurtle(x, y):
    print("You released the turtle", x, y)
    g = turtle.turtles()
    for tr in g:
        xx, yy = tr.position()
        diff_x = abs(xx-x)
        diff_y = abs(yy-y)
        print(diff_x, diff_y)
        if diff_x < 10 and diff_y < 10:
            tr.setposition(0,-300)
    

def hideTurtle(x,y):
    print("You release the click ", x, y)
    turtle.ht()

def f_createTurtle(num_turtles):
    colors =['red','blue','green','black','orange']
    list_of_turtles = []

    for i in range(num_turtles):
        x = rd.randint(-200, 200)
        y = rd.randint(-100, 100)
        c = rd.choice(colors)

        t = turtle.Turtle()
        t.shape("turtle")
        t.color(c)
        t.shapesize(stretch_wid=2, stretch_len=2, outline=None)
        t.penup()
        t.setposition(x, y)  
        t.onclick(msg)
        t.onrelease(getTurtle, btn=1, add=True)
        list_of_turtles.append(t)
            
    return list_of_turtles


turtle_list = f_createTurtle(2)

'''
# methods to action
def fxn1(x,y):
    turtle.fillcolor("blue")

def fxn2(x,y):
    turtle.fillcolor("white")
	
# set screen and turtle
sc=turtle.Screen()
sc.setup(400,300)

turtle.shape("turtle")
turtle.turtlesize(2)
turtle.speed(1)

# allow user to click for some action
turtle.onclick(fxn1)

# allow user to release for some action
turtle.onrelease(fxn2)
'''

