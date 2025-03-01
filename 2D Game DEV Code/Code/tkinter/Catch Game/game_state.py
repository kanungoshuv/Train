def update_score(score_label, score):
    """Update the score display."""
    score_label.config(text=f"Score: {score}")

def update_lives(lives_label, lives):
    """Update the lives display."""
    lives_label.config(text=f"Lives: {lives}")

def end_game(canvas, canvas_width, canvas_height):
    """Handle game over."""
    canvas.create_text(
        canvas_width // 2,
        canvas_height // 2,
        text="GAME OVER",
        font=("Arial", 24),
        fill="red"
    )

