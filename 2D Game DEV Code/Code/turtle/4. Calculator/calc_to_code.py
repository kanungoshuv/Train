import turtle
# import from calc_util:
# timi, timi_screen, num1, num2, ans, write_symbols, on_button_click, write_nums
# KEY IDEA: importing

timi.ht()
timi_screen.ht()

def create_outside():
    # create the outside border of the calculator starting from
    # x = -250, y = 250
    # the dimensions of the rectangle should be 500 by 500
    # fill in the color with blue
    # KEY IDEAS: for loops, turtle functions





def create_screen():
    # Create the screen starting from x = -200, y = 200
    # This is where the numbers will appear on the calculator.
    #
    # The dimensions of the rectangle should be 400 by 75
    # and you should fill in the color with grey.
    #
    # KEY IDEAS: for loops, conditionals, modulo (%), turtle functions
    
    


def create_operator_buttons():
    # Make four rectangles of dimensions 125 by 50 starting from
    # x = 75, y = 75.
    #
    # The starting points of each rectangle should be
    # 75 units away from the previous rectangle's starting point.
    #
    # You should use the double nested for loops that we learned earlier,
    # as well as conditionals and modulo to create the four buttons.
    #
    # Afterwards, create a rectangle of dimensions 55 by 25 starting
    # from x = 10, y = 75. Fill it in with the color red.
    #
    # KEY IDEAS: nested loops, conditionals, modulo (%), turtle functions
    




def create_number_buttons():
    # Create two lists to hold the coordinates of x and y coordinates
    # Name one list x_coor, and the other y_coor.
    # x_coor should have the values [-200, -125, -50] and
    # y_coor should have the values [75, 0, -75, -150].
    #
    # Then, using nested for loops, create the 12 buttons for
    # the numbers, decimal, and equal signs
    #
    # Fill each of them with the color white
    #
    # KEY IDEAS: lists, nested loops, indexing, turtle functions
            


create_outside()
create_screen()
create_operator_buttons()
create_number_buttons()
write_symbols()

turtle.onscreenclick(on_button_click, 1)
turtle.listen()
