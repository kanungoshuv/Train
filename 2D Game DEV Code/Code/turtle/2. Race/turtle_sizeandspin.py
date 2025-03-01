import turtle
import threading
import time

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()

colors = ["red", "blue", "green"]
turtles = [turtle1, turtle2, turtle3]
positions = [(-100, 0), (0,0), (100,0)]

for i in range(3):
    turtles[i].shape("turtle")
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(positions[i])

# For Red turtle1, Blue turtle2, Green turtle3
chosen_turtle = turtle1

enable_spin = True
enable_size = False
def animate_turtle(t):
    for _ in range(15):
        if enable_size:
            t.shapesize(2 + _ * 0.2)
        if enable_spin:
            t.right(30)
        time.sleep(0.1)

animation_thread = threading.Thread(target=animate_turtle, args=(chosen_turtle,))
animation_thread.start()

turtle.done()

animation_thread.join()

