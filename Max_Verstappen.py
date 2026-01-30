import pygame
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Max Verstappen Tribute")
RED=(255,0,0)
BLUE=(0,0,255)
screen.fill(RED)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                screen.fill(BLUE)
            if event.key==pygame.K_RIGHT:
                screen.fill(RED)                       
    pygame.display.update()
