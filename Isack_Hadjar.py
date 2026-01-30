from tkinter import font
import pygame, sys,random
pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
snake_block = 10
snake_speed = 10
x_head=screen_width/2
y_head=screen_height/2
x_head_change=0
y_head_change=0
randfoodX=random.randrange(0,screen_width-10)
surplus_foodX=randfoodX%10
fX=round(randfoodX-surplus_foodX)
randfoodY=random.randrange(0,screen_height-10)
surplus_foodY=randfoodY%10
fY=round(randfoodY-surplus_foodY)
score=0
def score_display(score):
    font=pygame.font.SysFont("Arial",25,True,True)
    value=font.render("Score: "+str(score),True,BLUE)
    screen.blit(value,[0,0])
score_display(score)
game_close=False
while True:
    while game_close==True:
        mesg=font.render("You Lost! Press C-Play Again or Q-Quit",True,RED) 
        screen.blit(mesg,[screen_width/6,screen_height/3])
        score_display(score)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key==pygame.K_c:
                    game_close=False
                    x_head=screen_width/2
                    y_head=screen_height/2
                    x_head_change=0
                    y_head_change=0
snake_bolc=[]
snake_length=1
snake_bolc=[]
snake_length=1
def our_snake(snake_block,snake_bolc):
    for x in snake_bolc:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_head_change = snake_speed
                y_head_change = 0
            elif event.key == pygame.K_RIGHT:   
                x_head_change = -snake_speed
                y_head_change = 0
            elif event.key == pygame.K_UP:
                x_head_change = 0
                y_head_change = -snake_speed
            elif event.key == pygame.K_DOWN:
                x_head_change = 0
                y_head_change = snake_speed
    x_head += x_head_change
    y_head += y_head_change
    snake_head = []
    snake_head.append(x_head)
    snake_head.append(y_head)
    snake_bolc.append(snake_head)
    if len(snake_bolc) > snake_length:
        del snake_bolc[0]
    our_snake(snake_block,snake_bolc)
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, [x_head, y_head, snake_block, snake_block])
    pygame.draw.rect(screen, RED, [fX, fY, snake_block, snake_block])
    if x_head == fX and y_head == fY:
        randfoodX=random.randrange(0,screen_width-10)
        surplus_foodX=randfoodX%10
        fX=round(randfoodX-surplus_foodX)
        randfoodY=random.randrange(0,screen_height-10)
        surplus_foodY=randfoodY%10
        fY=round(randfoodY-surplus_foodY)
        snake_length += 1
    if x_head >= screen_width or x_head < 0 or y_head >= screen_height or y_head < 0:
        pygame.quit()
        sys.exit()
    pygame.display.update()
    clock.tick(snake_speed)
    pygame.display.update()
    