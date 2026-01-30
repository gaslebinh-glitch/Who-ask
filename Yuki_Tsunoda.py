import pygame,sys
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
RED= (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
screen.fill(WHITE)
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pygame.draw.rect(screen, RED, (50, 50, 100, 100))
            elif event.key == pygame.K_RIGHT:
                pygame.draw.circle(screen, GREEN, (300, 200), 50)   
            elif event.key == pygame.K_UP:
                pygame.draw.line(screen, BLUE, (0, 0), (640, 480), 5)
            elif event.key == pygame.K_DOWN:
                pygame.draw.ellipse(screen, (0, 255, 0), (400, 300, 100, 50))