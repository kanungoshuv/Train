import tkinter as tk

def create_ui(root, canvas_width, canvas_height):
    """Create the game canvas and UI components."""
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="lightblue")
    canvas.pack()

    # Score and lives labels
    score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
    score_label.pack(side="left", padx=20)

    lives_label = tk.Label(root, text="Lives: 3", font=("Arial", 14))
    lives_label.pack(side="right", padx=20)

    # Restart button
    restart_button = tk.Button(root, text="Restart")
    restart_button.pack(side="bottom", pady=10)

    return canvas, score_label, lives_label, restart_button

