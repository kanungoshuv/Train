from tkinter import Tk
from game_ui import create_ui
from game_logic import move_basket, update_objects
from game_state import update_score, update_lives, end_game

def main():
    """Main function to start the game."""
    root = Tk()
    root.title("Catch the Falling Objects")
    root.resizable(False, False)

    # Canvas dimensions
    canvas_width = 400
    canvas_height = 600
    object_size = 20
    basket_width = 80
    basket_speed = 20

    # Create UI components
    canvas, score_label, lives_label, restart_button = create_ui(root, canvas_width, canvas_height)

    # Game state variables
    score = 0
    lives = 3
    falling_objects = []

    # Basket
    basket = canvas.create_rectangle(
        (canvas_width - basket_width) // 2,
        canvas_height - 30,
        (canvas_width + basket_width) // 2,
        canvas_height - 10,
        fill="brown"
    )

    # Callbacks
    def restart_game():
        nonlocal score, lives, falling_objects
        score = 0
        lives = 3
        falling_objects.clear()
        canvas.delete("all")
        update_score(score_label, score)
        update_lives(lives_label, lives)

    def game_loop():
        nonlocal score, lives
        if lives > 0:
            score, lives = update_objects(
                canvas, falling_objects, basket, canvas_height, canvas_width, object_size,
                score, lives,
                {
                    "update_score": lambda s: update_score(score_label, s),
                    "update_lives": lambda l: update_lives(lives_label, l),
                    "end_game": lambda: end_game(canvas, canvas_width, canvas_height),
                }
            )
            root.after(50, game_loop)

    # Bind controls
    root.bind("<Left>", lambda e: move_basket(e, canvas, basket, basket_speed, canvas_width))
    root.bind("<Right>", lambda e: move_basket(e, canvas, basket, basket_speed, canvas_width))
    restart_button.config(command=restart_game)

    # Start the game loop
    game_loop()
    root.mainloop()

if __name__ == "__main__":
    main()
 
