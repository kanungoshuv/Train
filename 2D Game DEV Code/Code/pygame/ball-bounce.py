import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
screen.fill("black")
clock = pygame.time.Clock()

white = (255, 255, 255)


class Ball:
    def __init__(self, x, y, radius, speed, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xfactor = 1
        self.yfactor = 1
        self.ballon = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def display(self):
        self.ballon = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


    def update(self):
        self.x += self.speed * self.xfactor
        self.y += self.speed * self.yfactor

        if (self.y <= 0 or self.y >= 720):
            self.yfactor *= -1

        if (self.x <= 0 or self.x >= 1280):
            self.xfactor *= -1


def main():
    running = True

    ball = Ball(640, 360, 10, 2, white)

    while running:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        ball.display()
        ball.update()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
    pygame.quit()
    
