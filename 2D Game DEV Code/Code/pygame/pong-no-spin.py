import pygame
import random

# Initialze 
pygame.init()
SCREENWIDTH = 1366
SCREENHEIGHT = 768
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT), pygame.RESIZABLE)
screen.fill("black")
clock = pygame.time.Clock()
running = True

white = (255, 255, 255)

class Hitter1:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = white
        self.yfactor = 1

        self.rectangle = pygame.Rect(x, y, width, height)
        self.rectangleDisplay = pygame.draw.rect(screen, white, self.rectangle)

    def movement(self):
        if (self.y <= 0):
            self.y = 0
        elif (self.y + self.height >= SCREENHEIGHT):	
            self.y = SCREENHEIGHT - self.height

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= 1.25 * self.yfactor
        if keys[pygame.K_s]:
            self.y += 1.25 * self.yfactor

        self.rectangle = pygame.Rect(self.x, self.y, self.width, self.height)

    def display(self):
        self.rectangleDisplay = pygame.draw.rect(screen, white, self.rectangle)

    def getRect(self):
        return self.rectangle

    
class Hitter2:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = white
        self.yfactor = 1

        self.rectangle = pygame.Rect(x, y, width, height)
        self.rectangleDisplay = pygame.draw.rect(screen, white, self.rectangle)

    def movement(self):
        if (self.y <= 0):
            self.y = 0
        elif (self.y + self.height >= SCREENHEIGHT):	
            self.y = SCREENHEIGHT - self.height

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= 1.25 * self.yfactor
        if keys[pygame.K_DOWN]:
            self.y += 1.25 * self.yfactor

        self.rectangle = pygame.Rect(self.x, self.y, self.width, self.height)

    def display(self):
        self.rectangleDisplay = pygame.draw.rect(screen, white, self.rectangle)

    def getRect(self):
        return self.rectangle


class Ball:
    def __init__(self, x, y, radius, speed, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.ospeed = speed #keep track of original speed so that we can reset the ball to this number
        self.color = color
        self.xfactor = 1
        self.yfactor = 1
        self.ballon = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def display(self):
        self.ballon = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


    def update(self):
        self.x += self.speed * self.xfactor
        self.y += self.speed * self.yfactor

        if (self.y <= 0 or self.y >= SCREENHEIGHT):
            self.yfactor *= -1

        if (self.x <= 0 or self.x >= SCREENWIDTH):
            self.reset()
            
    def hit(self):
        self.xfactor *= -1
        self.speed *= 1.01

    def reset(self):
        self.x = SCREENWIDTH / 2
        self.y = SCREENHEIGHT / 2
        self.speed = self.ospeed

    def getRect(self):
        return self.ballon


def main():
    running = True

    ball = Ball(SCREENWIDTH / 2, SCREENHEIGHT / 2, 10, 1, white)
    Player1 = Hitter1(10, SCREENHEIGHT / 2, 5, 100, white)
    Player2 = Hitter2(SCREENWIDTH - 10, SCREENHEIGHT / 2, 5, 100, white)

    playerList = [Player1, Player2]

    while running:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        for player in playerList:
            if pygame.Rect.colliderect(ball.getRect(), player.getRect()):
                ball.hit()
        
        
        ball.update()
        Player1.movement()
        Player2.movement()


        ball.display()
        Player1.display()
        Player2.display()


        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
    pygame.quit()
    
