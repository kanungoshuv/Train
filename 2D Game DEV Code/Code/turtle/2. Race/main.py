# My Turtle Race Program
# My Name is:
# -    -    -    -    -    -    -    -    -    -    -

# let us use the SpringBoard turtle race_utility
# as our framework to code this game.
from race_utility import f_draw_finish
from race_utility import f_createTurtle
from race_utility import f_startRace


# Three Steps: Add your lines of code here
# -    -    -    -    -    -    -    -    -    -    -

# Step 1: draw the markers as lines
f_draw_finish()

# Step 2: create one or 4 turtles eg. f_createTurtle('color', 1)
turtle1 = f_createTurtle('red', 1)
turtle2 = f_createTurtle('blue', 2)
turtle4 = f_createTurtle('orange', 4)


# Step 3: start the race
f_startRace(turtle1, turtle2, False, turtle4)


