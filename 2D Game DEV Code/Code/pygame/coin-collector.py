import pygame
import random

# pygame initializers
pygame.init()
pygame.font.init()

# screen, clock, fps initializers
WIDTH = 1366
HEIGHT = 768
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
fps = 60

# timer setup
timerevent = pygame.USEREVENT + 1
pygame.time.set_timer(timerevent, 1000)

# colors
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# player class for creating instance of user controlled rectangle
class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        
        self.body = pygame.Rect(x, y, width, height)
        self.displayBody = pygame.draw.rect(screen, self.color, self.body)

    def display(self):
        self.displayBody = pygame.draw.rect(screen, self.color, self.body)

# coin class for creating multiple instances of coins that will be collected
class Coin:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.body = pygame.Rect(x, y, width, height)
        self.displayBody = pygame.draw.rect(screen, yellow, self.body)

    def display(self):
        self.displayBody = pygame.draw.rect(screen, yellow, self.body)

# main
def main():
    running = True
    game_over = False
    
    # initializes player and score counter
    mouz = Player(0, 0, 25, 25, red)
    score = 0
    countdown = 30

    # create an array to make sure there is only one coin on screen at a time
    coins = []
    
    while running:
        # initialize font for score counter and timer, and update background
        font = pygame.font.Font(None, 36)
        screen.fill("black")

        # event handling
        for event in pygame.event.get():
            # quit application
            if event.type == pygame.QUIT:
                running = False

            # countdown timer handling
            elif event.type == timerevent:
                countdown -= 1
                if countdown == 0:
                    game_over = True                

        # run the game whilst not in game_over state
        if not game_over:
            # make the player rectangle follow the mouse and display it
            pygame.mouse.set_visible(False)
            pos = pygame.mouse.get_pos()
            mouz.body.center = pos
            mouz.display()

            # if there are no coins on the screen, create a coin in a random
            # position on the screen and add it to the array so we know there is
            # a coin on screen
            if (len(coins) == 0):
                coin = Coin(random.randint(0,WIDTH - 100), random.randint(0,HEIGHT - 100), 25, 25)
                coins.append(coin)

            # display the coin outside conditionals so it always shows until
            # the user hovers over it, thus collecting it
            coins[0].display()

            # if there is a coin on the screen, detect when the user hovers over it
            # with the mouse and delete it whilst incrementing the score 
            if (len(coins) == 1):
                if mouz.body.colliderect(coins[0].body):
                    del coins[0]
                    score += 1
            
            # display the score
            score_text = font.render(f'Score: {score}', True, (255, 255, 255))
            screen.blit(score_text, (10, 10))

            # display timer
            countdown_text = font.render(f'Time: {countdown}', True, (255, 255, 255))
            screen.blit(countdown_text, (10, 40))

            # update game state
            pygame.display.flip()

        # when the game is in game_over state, display the final score 
        elif game_over:
            screen.fill("black")
            final_score = font.render(f'Final Score: {score}', True, (255, 255, 255))
            screen.blit(final_score, (WIDTH / 2, HEIGHT / 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False
        
        # update game state
        #pygame.display.flip()

        #clock.tick(fps)



if __name__ == "__main__":
    main()
    pygame.quit()
        
    
    
