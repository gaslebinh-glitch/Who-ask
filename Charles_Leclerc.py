import pygame,sys
pygame.init()
screen = pygame.display.set_mode((640, 480))
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
pygame.draw.rect(screen, RED, (50, 50, 100, 100))
pygame.draw.circle(screen, GREEN, (300, 200), 50)
pygame.draw.line(screen, BLUE, (0, 0), (640, 480), 5)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()