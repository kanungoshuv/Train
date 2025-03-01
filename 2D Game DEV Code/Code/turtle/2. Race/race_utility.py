# Utility Functions for creating Turtle Races
# Create Instances of the Turtle then race them in
# in main.py.
# Author: Dr. Steven C. Lindo
# July 18, 2021
# -    -    -    -    -    -    -    -    -    -    -
# History
# Name  Date        Description
# scl   7/18/2021   Initial Draft of the utility
# -    -    -    -    -    -    -    -    -    -    -
import time
import turtle
import random as rd
import pandas as pd

SECONDS = 2
start_x = -300
start_y = -50

def f_draw_finish():

    pos_x = start_x + 50
    
    # draw starting line and finish line
    mypen = turtle.Turtle()
    mypen.color("black")
    mypen.pensize(1)
    mypen.left(90)

    while pos_x < 250:
        mypen.penup()
        mypen.setposition(pos_x, -50)

        for i in range(10):
            mypen.forward(15)
            mypen.penup()
            mypen.forward(5)
            mypen.pendown()

        pos_x += 50

    mypen.hideturtle()

def f_createTurtle(c, num):
    player1 = turtle.Turtle()
    player1.color(c)
    player1.shape("turtle")
    player1.shapesize(stretch_wid=2, stretch_len=2, outline=None)
    player1.penup()
    player1.setposition(start_x, start_y + (num * 42))
    player1.pendown()

    return player1

def spinTurtle(t):
    if t != False:
        for i in range(8):
            t.left(45)

def moveTurtle(t):
    x = 0
    if t != False:
        x, y = t.position()
        x = x + rd.randint(0,5)    
        t.setposition(x, y)
    return x

def f_drawBanner(text):
    placebetsbanner = turtle.Turtle()
    placebetsbanner.penup()
    placebetsbanner.setposition(-200, -75)
    placebetsbanner_text = text
    placebetsbanner.write(placebetsbanner_text, move=False, align="left", font=("Arial", 24, "normal"))
    placebetsbanner.hideturtle()
    time.sleep(SECONDS)
    placebetsbanner.clear()
   
def f_startRace(t1, t2, t3, t4):

    f_drawBanner("The race is about to begin ")
    time.sleep(SECONDS)
    spinTurtle(t1)
    spinTurtle(t2)
    spinTurtle(t3)
    spinTurtle(t4)
    f_drawBanner(" G o    T u r t l e s   G o ")

    while True:
        x = moveTurtle(t1)
        if x > 200:
            f_drawBanner("The Winner is Turtle 1")
            time.sleep(SECONDS)
            break;
        x = moveTurtle(t2)
        if x > 200:
            f_drawBanner("The Winner is Turtle 2")
            time.sleep(SECONDS)
            break;
        x = moveTurtle(t3)
        if x > 200:
            f_drawBanner("The Winner is Turtle 3")
            time.sleep(SECONDS)
            break;
        x = moveTurtle(t4)        
        if x > 200:
            f_drawBanner("The Winner is Turtle 4")
            time.sleep(SECONDS)
            break;

    f_drawBanner(" G a m e   O v e r   G o o d   B y e ")
    time.sleep(SECONDS)

    # End the Game by saying Good Bye
    turtle.bye()
