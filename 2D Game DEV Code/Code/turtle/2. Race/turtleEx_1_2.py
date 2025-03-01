# This will use the turtle_utilty.py functions and methods
# to create a turtle game.
# Author :  SpringBoard Team
#           [ Chelsea, Irma, Tuly, and Dr. Lindo ]
#
# Date   :  Summer 2021
#
# -    -    -    -    -    -    -    -    -    -    -    -    
from turtle_utility_1_2 import draw_perim, f_createTurtle, f_gameOver, \
     f_drawBanner, f_playGame, f_resetTurtles

status  = 0
LEVEL   = 1
TURTLES = 4
turtle_list = []

while status == 0:
    draw_perim()
    turtle_list = f_createTurtle(TURTLES)
    f_drawBanner('Begin Playing in 2 Seconds !!')
    status = f_playGame(turtle_list, LEVEL)
    if status == 0:
        LEVEL   += 1
        TURTLES += 1
        f_resetTurtles()
        f_drawBanner('Great Job! Level Up To ' + str(LEVEL))
