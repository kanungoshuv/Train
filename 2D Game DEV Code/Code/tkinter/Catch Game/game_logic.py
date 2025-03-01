import random

def create_object(canvas, canvas_width, object_size):
    """Create a new falling object."""
    x = random.randint(0, canvas_width - object_size)
    return canvas.create_oval(x, 0, x + object_size, object_size, fill="red")

def move_basket(event, canvas, basket, basket_speed, canvas_width):
    """Move the basket left or right based on user input."""
    if event.keysym == "Left":
        canvas.move(basket, -basket_speed, 0)
    elif event.keysym == "Right":
        canvas.move(basket, basket_speed, 0)

    # Prevent the basket from moving out of bounds
    x1, _, x2, _ = canvas.coords(basket)
    if x1 < 0:
        canvas.move(basket, -x1, 0)
    elif x2 > canvas_width:
        canvas.move(basket, canvas_width - x2, 0)

def update_objects(canvas, falling_objects, basket, canvas_height, canvas_width, object_size, score, lives, callbacks):
    """Update the positions of falling objects and check for collisions."""
    objects_to_remove = []
    for obj in falling_objects:
        canvas.move(obj, 0, 10)  # Move the object down
        x1, y1, x2, y2 = canvas.coords(obj)
        bx1, by1, bx2, by2 = canvas.coords(basket)

        # Check if the object is caught
        if y2 >= by1 and bx1 < x1 < bx2:
            score += 10
            canvas.delete(obj)
            objects_to_remove.append(obj)
            callbacks["update_score"](score)

        # Check if the object falls out of bounds
        elif y1 > canvas_height:
            lives -= 1
            canvas.delete(obj)
            objects_to_remove.append(obj)
            callbacks["update_lives"](lives)

            if lives <= 0:
                callbacks["end_game"]()

    # Remove the collected objects
    for obj in objects_to_remove:
        falling_objects.remove(obj)

    # Add a new object randomly
    if random.randint(1, 20) == 1:
        falling_objects.append(create_object(canvas, canvas_width, object_size))

    return score, lives

