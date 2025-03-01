# Python Turtle Memory Game
# By Springboard Incubators
# Author: Brendan Ofori

import turtle
import time
import random
import os

t = turtle.Turtle()
running = True

# Create a circle with a random number from 1 to 9
def create_circle(x, y):
    random_num = random.randint(0, 9)
    t.color("red")
    t.penup()   
    t.goto(x, y)
    t.pendown()
    t.circle(45)
    t.penup()
    t.goto(x - 10, y + 22.5)
    t.pendown()
    t.write(random_num, font = ('Arial', 30, 'normal'))
    return random_num

# Creates and handles the events of each level as it increases
def make_level(num_level):
    # List of available x-coordinates and starting y-coordinate
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

    # Display the circles with random numbers that need to be guessed
    for a in range(num_level):
        if a < 5:
            y_val = 225
            
        elif a >= 5 and a < 10:
            y_val = 125 

        elif a >= 10 and a < 15:
            y_val = 25

        elif a >= 15 and a < 20:
            y_val = -75

        elif a >= 20 and a < 25:
            y_val = -175

        elif a >= 25 and a < 30:
            y_val = -275

            
        r = create_circle(x_vals[a % 5], y_val)
        correct.append(r)

    # Freeze the screen to give chance to memorize
    time.sleep(3)
    t.clear()

    # Guess Handling
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
            
        # Game Over
        if guess_int != correct[b]:
            t.penup()
            t.setposition(-200, -200)
            t.color("black")
            t.write(f"Game Over. Your final score was {num_level}.", font = ('Arial', 20, 'normal'))
            time.sleep(5)
            turtle.bye()
            os._exit(0)
    

def main():
    level = 1
    
    while running:
        make_level(level)
        level += 1

        

if __name__ == "__main__":
    main()
    



