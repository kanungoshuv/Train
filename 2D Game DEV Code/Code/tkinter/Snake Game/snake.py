import tkinter as tk
import random

class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game")
        
        # Set up game constants
        self.GAME_WIDTH = 400
        self.GAME_HEIGHT = 400
        self.SPEED = 150
        self.SPACE_SIZE = 20
        self.SNAKE_COLOR = "#00FF00"
        self.FOOD_COLOR = "#FF0000"
        
        # Create the game canvas
        self.canvas = tk.Canvas(self.window, width=self.GAME_WIDTH, 
                              height=self.GAME_HEIGHT, bg="#000000")
        self.canvas.pack()
        
        # Create score display
        self.score = 0
        self.score_text = tk.Label(self.window, text=f"Score: {self.score}", font=('Arial', 12))
        self.score_text.pack()
        
        # Initialize game variables
        self.direction = 'right'
        self.snake_positions = []
        self.snake_squares = []
        self.food_position = []
        
        # Bind arrow keys
        self.window.bind('<Left>', lambda event: self.change_direction('left'))
        self.window.bind('<Right>', lambda event: self.change_direction('right'))
        self.window.bind('<Up>', lambda event: self.change_direction('up'))
        self.window.bind('<Down>', lambda event: self.change_direction('down'))
        
        # Start the game
        self.create_snake()
        self.create_food()
        self.next_turn()
        self.window.mainloop()

    def create_snake(self):
        # Starting position (center of screen)
        start_x = self.GAME_WIDTH / 2
        start_y = self.GAME_HEIGHT / 2
        
        # Create 3 snake segments
        for _ in range(3):
            self.snake_positions.append([start_x, start_y])
            square = self.canvas.create_rectangle(start_x, start_y, 
                                               start_x + self.SPACE_SIZE, 
                                               start_y + self.SPACE_SIZE, 
                                               fill=self.SNAKE_COLOR)
            self.snake_squares.append(square)
            start_x -= self.SPACE_SIZE

    def create_food(self):
        x = random.randint(0, (self.GAME_WIDTH - self.SPACE_SIZE) // 
                          self.SPACE_SIZE) * self.SPACE_SIZE
        y = random.randint(0, (self.GAME_HEIGHT - self.SPACE_SIZE) // 
                          self.SPACE_SIZE) * self.SPACE_SIZE
        
        self.food_position = [x, y]
        self.canvas.create_oval(x, y, x + self.SPACE_SIZE, y + self.SPACE_SIZE, 
                              fill=self.FOOD_COLOR, tag="food")

    def next_turn(self):
        # Get current head position
        head_x = self.snake_positions[0][0]
        head_y = self.snake_positions[0][1]
        
        # Update head position based on direction
        if self.direction == 'left':
            head_x -= self.SPACE_SIZE
        elif self.direction == 'right':
            head_x += self.SPACE_SIZE
        elif self.direction == 'up':
            head_y -= self.SPACE_SIZE
        elif self.direction == 'down':
            head_y += self.SPACE_SIZE
            
        # Insert new head
        self.snake_positions.insert(0, [head_x, head_y])
        
        # Create new head square
        square = self.canvas.create_rectangle(head_x, head_y, 
                                           head_x + self.SPACE_SIZE, 
                                           head_y + self.SPACE_SIZE, 
                                           fill=self.SNAKE_COLOR)
        self.snake_squares.insert(0, square)
        
        # Check for food collision
        if head_x == self.food_position[0] and head_y == self.food_position[1]:
            self.score += 1
            self.score_text.config(text=f"Score: {self.score}")
            self.canvas.delete("food")
            self.create_food()
        else:
            # Remove tail
            self.snake_positions.pop()
            self.canvas.delete(self.snake_squares.pop())
        
        # Check for collisions and continue game
        if self.check_collisions():
            self.game_over()
        else:
            self.window.after(self.SPEED, self.next_turn)

    def check_collisions(self):
        head_x = self.snake_positions[0][0]
        head_y = self.snake_positions[0][1]
        
        return (head_x < 0 or head_x >= self.GAME_WIDTH or 
                head_y < 0 or head_y >= self.GAME_HEIGHT or 
                self.snake_positions[0] in self.snake_positions[1:])

    def change_direction(self, new_direction):
        if ((new_direction == 'left' and self.direction != 'right') or
            (new_direction == 'right' and self.direction != 'left') or
            (new_direction == 'up' and self.direction != 'down') or
            (new_direction == 'down' and self.direction != 'up')):
            self.direction = new_direction

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(self.GAME_WIDTH/2, self.GAME_HEIGHT/2, 
                              text=f"Game Over! Score: {self.score}", 
                              font=('Arial', 16), fill="white")

if __name__ == "__main__":
    game = SnakeGame()