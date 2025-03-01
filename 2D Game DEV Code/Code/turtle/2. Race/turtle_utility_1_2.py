# -    -    -    -    -    -    -    -    -    -    -    -
# Author :  SpringBoard Team
#           [ Chelsea, Irma, Tuly, and Dr. Lindo ]
#
# Date   :  Summer 2021

# Update :
# Date   :  Summer 2023 [Peiyan Wu]
# -    -    -    -    -    -    -    -    -    -    -    -
import os
import time
import turtle
import random as rd
import turtle as tt
from datetime import datetime, timedelta

SPEED   = 1
SECONDS = 2
TIMER   = 1
DIFF    = 10
# method to action

def draw_perim():
    tt.penup()
    tt.hideturtle()
    tt.goto(-250,250)
    
    for i in range(4):
        tt.pendown()
        tt.forward(500)
        tt.right(90)
        
    
    
def getTurtle(x, y):
    g = turtle.turtles()
    for tr in g:
        xx, yy = tr.position()
        diff_x = abs(xx-x)
        diff_y = abs(yy-y)
        if diff_x < 10 and diff_y < 10:
            setposition(0,0)

def f_resetTurtles():
    g = turtle.turtles()
    for tr in g:
        tr.reset()
        tr.clear()
        tr.hideturtle()
    
def spinTurtle(t):
    direction = rd.randint(8,16)
    if t != False:
        for i in range(direction):
            t.left(45)

def f_playGame(t_list,level):
    current_time = datetime.now()
    game_time = current_time + timedelta(seconds=TIMER)
    print(game_time, current_time)

    while datetime.now() < game_time:
        for t in t_list:
            x,y = moveTurtle(t, level)
            if x > 250 or y > 250 or x < -250 or y < -250:
                f_drawBanner('A turtle has escaped !!')
                spinTurtle(t)
                f_gameOver()

    # if no turtles escaped then
    # retun 0 to level up
    return 0

def moveTurtle(t,level):
    m = 0
    x = 0
    y = 0
    if t != False:
        m = rd.randint(1,level) 
        t.forward(m)
        x, y = t.position()
    return x, y

def f_createTurtle(num_turtles):
    colors =['red','blue','green','black','orange']
    list_of_turtles = []

    for i in range(num_turtles):
        x = rd.randint(-150, 150)
        y = rd.randint(-150, 150)
        c = rd.choice(colors)

        t = turtle.Turtle()
        t.shape("turtle")
        t.color(c)
        t.shapesize(stretch_wid=2, stretch_len=2, outline=None)
        t.penup()
        t.setposition(x, y)  
        spinTurtle(t)
        t.onclick(getTurtle, btn=1, add=True)

        list_of_turtles.append(t)

    return list_of_turtles

def f_drawBanner(text):
    placebetsbanner = turtle.Turtle()
    placebetsbanner.penup()
    placebetsbanner.ht()
    placebetsbanner.setposition(-200, -200)
    placebetsbanner_text = text
    placebetsbanner.write(placebetsbanner_text, move=False, align="left", font=("Arial", 24, "normal"))
    time.sleep(SECONDS)
    placebetsbanner.clear()


def f_gameOver():
    f_drawBanner(" G a m e   O v e r   G o o d   B y e ")
    time.sleep(SECONDS)

    # End the Game by saying Good Bye
    turtle.bye()
    os._exit(0)
