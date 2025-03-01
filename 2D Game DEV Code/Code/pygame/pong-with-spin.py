import pygame
import random
import math

# Initialze 
pygame.init()
pygame.font.init()

SCREENWIDTH = 1366
SCREENHEIGHT = 768
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
screen.fill("black")
clock = pygame.time.Clock()
running = True

white = (255, 255, 255)
red = (255, 0, 0)

class Hitter1:
    def __init__(self):
        self.x = 10
        self.y = SCREENHEIGHT / 2
        self.width = 10
        self.height = 150
        self.color = white
        #self.yfactor = 1

        self.rectTop = pygame.Rect(self.x, self.y, self.width, self.height*0.2)
        self.rectangle = pygame.Rect(self.x, self.y + self.height*0.2, self.width, self.height*0.6)
        self.rectBot = pygame.Rect(self.x, self.y + self.height*0.8, self.width, self.height*0.2)

        self.rectTopDisplay = pygame.draw.rect(screen, red, self.rectTop)
        self.rectangleDisplay = pygame.draw.rect(screen, white, self.rectangle)
        self.rectBotDisplay = pygame.draw.rect(screen, red, self.rectBot)
        
    def update(self):
        if (self.y <= 0):
            self.y = 0
        elif (self.y + self.height >= SCREENHEIGHT):	
            self.y = SCREENHEIGHT - self.height

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= 1 #* self.yfactor
        if keys[pygame.K_s]:
            self.y += 1 #* self.yfactor

        self.rectTop = pygame.Rect(self.x, self.y, self.width, self.height*0.2)
        self.rectangle = pygame.Rect(self.x, self.y + self.height*0.2, self.width, self.height*0.6)
        self.rectBot = pygame.Rect(self.x, self.y + self.height*0.8, self.width, self.height*0.2)

        
    def display(self):
        self.rectangleDisplay = pygame.draw.rect(screen, white, self.rectangle)
        self.rectTopDisplay = pygame.draw.rect(screen, red, self.rectTop)
        self.rectBotDisplay = pygame.draw.rect(screen, red, self.rectBot)

    def getTopRect(self):
        return self.rectTop
    
    def getMidRect(self):
        return self.rectangle

    def getBotRect(self):
        return self.rectBot

    
class Hitter2:
    def __init__(self):
        self.x = SCREENWIDTH - 20
        self.y = SCREENHEIGHT / 2
        self.width = 10
        self.height = 150
        self.color = white
        #self.yfactor = 1

        self.rectTop = pygame.Rect(self.x, self.y, self.width, self.height*0.2)
        self.rectangle = pygame.Rect(self.x, self.y + self.height*0.2, self.width, self.height*0.6)
        self.rectBot = pygame.Rect(self.x, self.y + self.height*0.8, self.width, self.height*0.2)

        self.rectTopDisplay = pygame.draw.rect(screen, red, self.rectTop)
        self.rectangleDisplay = pygame.draw.rect(screen, white, self.rectangle)
        self.rectBotDisplay = pygame.draw.rect(screen, red, self.rectBot)

    def update(self):
        if (self.y <= 0):
            self.y = 0
        elif (self.y + self.height >= SCREENHEIGHT):	
            self.y = SCREENHEIGHT - self.height

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= 1 #* self.yfactor
        if keys[pygame.K_DOWN]:
            self.y += 1 #* self.yfactor

        self.rectTop = pygame.Rect(self.x, self.y, self.width, self.height*0.2)
        self.rectangle = pygame.Rect(self.x, self.y + self.height*0.2, self.width, self.height*0.6)
        self.rectBot = pygame.Rect(self.x, self.y + self.height*0.8, self.width, self.height*0.2)

        
    def display(self):
        self.rectangleDisplay = pygame.draw.rect(screen, white, self.rectangle)
        self.rectTopDisplay = pygame.draw.rect(screen, red, self.rectTop)
        self.rectBotDisplay = pygame.draw.rect(screen, red, self.rectBot)

    def getTopRect(self):
        return self.rectTop
    
    def getMidRect(self):
        return self.rectangle

    def getBotRect(self):
        return self.rectBot


class Ball:
    def __init__(self):
        self.x = SCREENWIDTH / 2
        self.y = SCREENHEIGHT / 2
        self.radius = 10
        self.speed = 1
        self.ospeed = 1 #keep track of original speed so that we can reset the ball to this number
        self.angle = math.pi / 2
        self.oangle = math.pi / 2 #keep track of original angle so that we can reset the ball to this number
        self.color = white
        self.xfactor = -1
        self.yfactor = -1
        self.ballon = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


    def display(self):
        self.ballon = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


    def update(self):
        delta_x = self.speed * math.sin(self.angle)
        delta_y = self.speed * math.cos(self.angle)

        self.x += delta_x * self.xfactor
        self.y += delta_y * self.yfactor
        
        if (self.y <= 0 or self.y >= SCREENHEIGHT):
            self.yfactor *= -1

        if (self.x <= 0 or self.x >= SCREENWIDTH):
            self.reset()
            
    def hit(self, case):
        if case == 1:
            self.xfactor *= -1
            
        if case == 2:
            self.xfactor *= -1
            self.yfactor = 1
            self.angle = math.pi/2 + random.uniform((math.pi/8), (2*math.pi/8))
            #self.angle -= random.uniform(0.001, (math.pi/2)-0.001)
            
        if case == 3:
            self.xfactor *= -1
            self.yfactor = 1
            self.angle = math.pi/2 - random.uniform((math.pi/8), (2*math.pi/8))
            #self.angle += random.uniform(0.001, (math.pi/2)-0.001)
            
        self.speed *= 1.01

    def reset(self):
        self.x = SCREENWIDTH / 2
        self.y = SCREENHEIGHT / 2
        self.xfactor *= -1
        self.speed = self.ospeed
        self.angle = self.oangle

    def getRect(self):
        return self.ballon



def main():
    running = True

    ball = Ball()
    Player1 = Hitter1()
    Player2 = Hitter2()


    playerList = [Player1, Player2]

    while running:
        font = pygame.font.Font(None, 36)
        
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        divider = pygame.Rect(SCREENWIDTH / 2, 0, 10, SCREENHEIGHT)
        div_display = pygame.draw.rect(screen, white, divider)

        
        for player in playerList:
            if pygame.Rect.colliderect(ball.ballon, player.rectangle):
                ball.hit(1)
            if pygame.Rect.colliderect(ball.ballon, player.rectTop):
                ball.hit(2)
            if pygame.Rect.colliderect(ball.ballon, player.rectBot):
                ball.hit(3)
        
        
        ball.update()
        Player1.update()
        Player2.update()


        ball.display()
        Player1.display()
        Player2.display()


        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
    pygame.quit()
    
