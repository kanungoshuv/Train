import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)



def main():
    running = True


    while running:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        pygame.mouse.set_visible(False)
        mouz = pygame.Rect(0, 0, 25, 25)
        pos = pygame.mouse.get_pos()
        mouz.center = pos


        pygame.draw.rect(screen, red, mouz)


        pygame.display.flip()
        
    

if __name__ == "__main__":
    main()
    pygame.quit()
