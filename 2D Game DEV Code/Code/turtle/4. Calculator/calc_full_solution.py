import turtle

num1 = '0'
num2 = '0'
ans = '0'

timi = turtle.Turtle()
timi_screen = turtle.Turtle()

timi.ht()
timi_screen.ht()

def create_outside():
    
    timi.penup()
    timi.goto(-250, 250)
    timi.pendown()

    
    timi.fillcolor('blue')
    timi.begin_fill()
    for i in range(4):
        timi.forward(500)
        timi.right(90)
    timi.end_fill()




def create_screen():
    
    timi.penup()
    timi.goto(-200, 200)
    timi.pendown()

    timi.fillcolor('light gray')
    timi.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            timi.forward(400)
            timi.right(90)
        else:
            timi.forward(75)
            timi.right(90)
    timi.end_fill()



def create_operator_buttons():
    
    x = 75
    y = 75
    
    for i in range(4):
        timi.penup()
        timi.goto(x, y)
        timi.pendown()
        
        timi.fillcolor('white')
        timi.begin_fill()
        for j in range(4):
            if j % 2 == 0:
                timi.forward(125)
                timi.right(90)
            else:
                timi.forward(50)
                timi.right(90)
        timi.end_fill()
        
        y -= 75


    x = 10
    y = 75

    timi.penup()
    timi.goto(x, y)
    timi.pendown()

    timi.fillcolor('red')
    timi.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            timi.forward(55)
            timi.right(90)
        else:
            timi.forward(25)
            timi.right(90)
    timi.end_fill()



def create_number_buttons():
    
    x_coor = [-200, -125, -50]
    y_coor = [75, 0, -75, -150]

    for i in range(3):
        timi.penup()
        for j in range(4):
            timi.goto(x_coor[i], y_coor[j])
            timi.pendown()
            
            timi.fillcolor('white')
            timi.begin_fill()
            for j in range(4):
                timi.forward(50)
                timi.right(90)
            timi.penup()
            timi.end_fill()
            

def write_symbols():

    x_coor = [-175, -100, -25, 137.5]
    y_coor = [50, -25, -100, -175]
    symbols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ".", "=", "+", "-", "x", "÷"]

    for i in range(4):
        timi.penup()
        for j in range(4):
            timi.goto(x_coor[j], y_coor[i])
            timi.pendown

            # 9, 8, 7, +
            if i == 0:
                # Write +
                if j == 3:
                    timi.write(symbols[12], font = ('Arial', 15, 'normal'))
                # Write 9
                if j == 2:
                    timi.write(symbols[9], font = ('Arial', 15, 'normal'))
                # Write 8
                if j == 1:
                    timi.write(symbols[8], font = ('Arial', 15, 'normal'))
                # Write 7
                if j == 0:
                    timi.write(symbols[7], font = ('Arial', 15, 'normal'))

            # 6, 5, 4, -
            elif i == 1:
                # Write -
                if j == 3:
                    timi.write(symbols[13], font = ('Arial', 15, 'normal'))
                # Write 6
                if j == 2:
                    timi.write(symbols[6], font = ('Arial', 15, 'normal'))
                # Write 5
                if j == 1:
                    timi.write(symbols[5], font = ('Arial', 15, 'normal'))
                # Write 4
                if j == 0:
                    timi.write(symbols[4], font = ('Arial', 15, 'normal'))

            # 3, 2, 1, x
            elif i == 2:
                # Write x
                if j == 3:
                    timi.write(symbols[14], font = ('Arial', 15, 'normal'))
                # Write 3
                if j == 2:
                    timi.write(symbols[3], font = ('Arial', 15, 'normal'))
                # Write 2
                if j == 1:
                    timi.write(symbols[2], font = ('Arial', 15, 'normal'))
                # Write 1
                if j == 0:
                    timi.write(symbols[1], font = ('Arial', 15, 'normal'))

            # 0, ., =, ÷
            elif i == 3:
                # Write ÷
                if j == 3:
                    timi.write(symbols[15], font = ('Arial', 15, 'normal'))
                # Write =
                if j == 2:
                    timi.write(symbols[11], font = ('Arial', 15, 'normal'))
                # Write .
                if j == 1:
                    timi.write(symbols[10], font = ('Arial', 15, 'normal'))
                # Write 0
                if j == 0:
                    timi.write(symbols[0], font = ('Arial', 15, 'normal'))



def on_button_click(x, y):
    
    x_coor = [-200, -125, -50, 75]
    y_coor = [75, 0, -75, -150]

    global num1, num2, ans
    queryCheck = None
    
    if num1[-1] == '+' or num1[-1] == '-' or num1[-1] == '*' or num1[-1] == '/':
        queryCheck = True
    else:
        queryCheck = False

    # Click clear
    if (x > 10) and (x < 66) and (y < 75) and (y > 49):
        num1 = '0'
        num2 = '0'
        write_nums(num1[1:])

    
    # Click +
    if (x > x_coor[3]) and (x < x_coor[3] + 126) and (y < y_coor[0]) and (y > y_coor[0] - 51):
        if not queryCheck:
            num1 += '+'
    
    # Click 9
    if (x > x_coor[2]) and (x < x_coor[2] + 51) and (y < y_coor[0]) and (y > y_coor[0] - 51):
        if queryCheck:
            num2 += '9'
            write_nums(num2[1:])
        else:
            num1 += '9'
            write_nums(num1[1:])
    
    # Click 8
    if (x > x_coor[1]) and (x < x_coor[1] + 51) and (y < y_coor[0]) and (y > y_coor[0] - 51):
        if queryCheck:
            num2 += '8'
            write_nums(num2[1:])
        else:
            num1 += '8'
            write_nums(num1[1:])
    
    # Click 7
    if (x > x_coor[0]) and (x < x_coor[0] + 51) and (y < y_coor[0]) and (y > y_coor[0] - 51):
        if queryCheck:
            num2 += '7'
            write_nums(num2[1:])
        else:
            num1 += '7'
            write_nums(num1[1:])
    
    # Click -
    if (x > x_coor[3]) and (x < x_coor[3] + 126) and (y < y_coor[1]) and (y > y_coor[1] - 51):
        if not queryCheck:
            num1 += '-'
    
    # Click 6
    if (x > x_coor[2]) and (x < x_coor[2] + 51) and (y < y_coor[1]) and (y > y_coor[1] - 51):
        if queryCheck:
            num2 += '6'
            write_nums(num2[1:])
        else:
            num1 += '6'
            write_nums(num1[1:])
    
    # Click 5
    if (x > x_coor[1]) and (x < x_coor[1] + 51) and (y < y_coor[1]) and (y > y_coor[1] - 51):
        if queryCheck:
            num2 += '5'
            write_nums(num2[1:])
        else:
            num1 += '5'
            write_nums(num1[1:])
    
    # Click 4
    if (x > x_coor[0]) and (x < x_coor[0] + 51) and (y < y_coor[1]) and (y > y_coor[1] - 51):
        if queryCheck:
            num2 += '4'
            write_nums(num2[1:])
        else:
            num1 += '4'
            write_nums(num1[1:])
    
    # Click x
    if (x > x_coor[3]) and (x < x_coor[3] + 126) and (y < y_coor[2]) and (y > y_coor[2] - 51):
        if not queryCheck:
            num1 += '*'
    
    # Click 3
    if (x > x_coor[2]) and (x < x_coor[2] + 51) and (y < y_coor[2]) and (y > y_coor[2] - 51):
        if queryCheck:
            num2 += '3'
            write_nums(num2[1:])
        else:
            num1 += '3'
            write_nums(num1[1:])
    
    # Click 2
    if (x > x_coor[1]) and (x < x_coor[1] + 51) and (y < y_coor[2]) and (y > y_coor[2] - 51):
        if queryCheck:
            num2 += '2'
            write_nums(num2[1:])
        else:
            num1 += '2'
            write_nums(num1[1:])
    
    # Click 1
    if (x > x_coor[0]) and (x < x_coor[0] + 51) and (y < y_coor[2]) and (y > y_coor[2] - 51):
        if queryCheck:
            num2 += '1'
            write_nums(num2[1:])
        else:
            num1 += '1'
            write_nums(num1[1:])
    
    # Click ÷
    if (x > x_coor[3]) and (x < x_coor[3] + 126) and (y < y_coor[3]) and (y > y_coor[3] - 51):
        if not queryCheck:
            num1 += '/'
    
    # Click =
    if (x > x_coor[2]) and (x < x_coor[2] + 51) and (y < y_coor[3]) and (y > y_coor[3] - 51):
        n1 = num1[:-1]
        sym = num1[-1]
        n2 = num2

        query1 = float(n1)
        query2 = float(n2)
        result = 0

        if sym == '+':
            result = query1 + query2
        elif sym == '-':
            result = query1 - query2
        elif sym == '*':
            result = query1 * query2
        else:
            result = query1 / query2

        ans = str(result)

        timi_screen.clear()
        timi_screen.penup()
        timi_screen.goto(-198, 162.5)
        timi_screen.pendown()
        timi_screen.write(ans, font = ('Arial', 20, 'normal'))
        
        num1 = '0'
        num2 = '0'
        
    
    # Click .
    if (x > x_coor[1]) and (x < x_coor[1] + 51) and (y < y_coor[3]) and (y > y_coor[3] - 51):
        if queryCheck and ('.' not in num2):
            num2 += '.'
            write_nums(num2)
        if (not queryCheck) and ('.' not in num1):
            num1 += '.'
            write_nums(num1)
    
    # Click 0
    if (x > x_coor[0]) and (x < x_coor[0] + 51) and (y < y_coor[3]) and (y > y_coor[3] - 51):
        if queryCheck:
            num2 += '0'
            write_nums(num2)
        else:
            num1 += '0'
            write_nums(num1)

    print(f"num1: {num1}")
    print(f"num2: {num2}")
    print(f"ans: {ans}")


def write_nums(string):
    timi_screen.clear()
    timi_screen.penup()
    timi_screen.goto(-198, 162.5)
    timi_screen.pendown()
    timi_screen.write(string, font = ('Arial', 20, 'normal'))    


create_outside()
create_screen()
create_operator_buttons()
create_number_buttons()
write_symbols()

turtle.onscreenclick(on_button_click, 1)
turtle.listen()
