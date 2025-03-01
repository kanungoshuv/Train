# Python Turtle Memory Game
# By Springboard Incubators
# Author: Brendan Ofori

import turtle
import time
import random
import os

t = turtle.Turtle()
running = True

def create_circle(x, y):
    random_num = random.randint(0, 9)
    # ADD CODE 1: Select a color for the circles using the turtle named t
    t.penup()   
    t.goto(x, y)
    t.pendown()
    t.circle(45)
    t.penup()
    t.goto(x - 10, y + 22.5)
    t.pendown()
    t.write(random_num, font = ('Arial', 30, 'normal'))
    return random_num


def make_level(num_level):
    x_vals = [-220, -110, 0, 110, 220]
    y_val = 225
       
    correct = []

    if num_level == 31:
        t.penup()
        t.setposition(-200, -200)
        t.color("black")
        t.write(f"Congrats! You won!", font = ('Arial', 20, 'normal'))
        time.sleep(5)
        turtle.bye()
        os._exit(0)

    for a in range(num_level):
        # ADD CODE 2: For each of the following, you are given a conditional.
        # We are trying to make it so that after every 5 levels, we go
        # down a line and begin writing the next circles.
        # The first line has been filled out for you
        if a < 5:
            y_val = 225

        elif :
            y_val = 125 

        elif :
            y_val = 25

        elif :
            y_val = -75

        elif :
            y_val = -175

        elif :
            y_val = -275

            
        r = create_circle(x_vals[a % 5], y_val)
        correct.append(r)

    time.sleep(3)
    t.clear()

    for b in range(num_level):
        guess = ""
        guess_int = 0
        b_plus_one = b + 1
        
        if b == 0:
            guess = turtle.textinput("Guess", f"Enter the {b_plus_one}st number that appeared:")
            guess_int = int(guess)
            
        elif b == 1:
            guess = turtle.textinput("Guess", f"Enter the {b_plus_one}nd number that appeared:")
            guess_int = int(guess)

        elif b == 2:
            guess = turtle.textinput("Guess", f"Enter the {b_plus_one}rd number that appeared:")
            guess_int = int(guess)

        else:
            guess = turtle.textinput("Guess", f"Enter the {b_plus_one}th number that appeared:")
            guess_int = int(guess)
            
        if guess_int != correct[b]:
            t.penup()
            t.setposition(-200, -200)
            t.color("black")
            t.write(f"Game Over. Your final score was {num_level}.", font = ('Arial', 20, 'normal'))
            time.sleep(5)
            turtle.bye()
            os._exit(0)
    

def main():
    # ADD CODE 3: Create a variable to keep track of the level and set it
    # equal to 0.
    
    while running:
        # ADD CODE 4:
        # STEP 1 - Using make_level and the variable you created,
        # write a line of code that starts the game.
        # STEP 2 - Look at the statement: var += 1 and
        # delete the hashtag next to it.
        # STEP 3 - Replace var with the name of the variable you made
        # in "ADD CODE 3".
        
        # MAKE LEVEL ON THIS LINE (DELETE ME)
        
        #var += 1

        

if __name__ == "__main__":
    main()
    



