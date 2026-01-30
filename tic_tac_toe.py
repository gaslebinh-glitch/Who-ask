import pygame,sys
pygame.init()
screen_width=600
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Tic Tac Toe")
screen.fill((255,255,255))
BLUE=(0,0,255)
GREEN=(0,255,0)
rows=3
cols=3
sq_size=screen_width//cols
line_width=10
circle_rad=sq_size//3
circle_width=10
board=[[0 for i in range(3)]for j in range(3)]
def draw_lines():
    pygame.draw.line(screen,(0,0,0),(0,sq_size),(screen_width,sq_size),line_width)
    pygame.draw.line(screen,(0,0,0),(0,2*sq_size),(screen_width,2*sq_size),line_width)
    pygame.draw.line(screen,(0,0,0),(sq_size,0),(sq_size,screen_height),line_width)
    pygame.draw.line(screen,(0,0,0),(2*sq_size,0),(2*sq_size,screen_height),line_width)
def draw_figures():
    for row in range(rows):
        for col in range(cols):
            if board[row][col]==2:
                pygame.draw.circle(screen,(255,0,0),(col*sq_size+sq_size//2,row*sq_size+sq_size//2),circle_rad,circle_width)
            elif board[row][col]==1:
                pygame.draw.line(screen,(0,0,255),(col*sq_size+sq_size//4,row*sq_size+sq_size//4),(col*sq_size+3*sq_size//4,row*sq_size+3*sq_size//4),line_width)
                pygame.draw.line(screen,(0,0,255),(col*sq_size+3*sq_size//4,row*sq_size+sq_size//4),(col*sq_size+sq_size//4,row*sq_size+3*sq_size//4),line_width)
def mark_square(row,col,player):
    board[row][col]=player
def available_square(row,col):
    return board[row][col]==0
def draw_vertical_winning_line(col):
    posX=col*sq_size+sq_size//2
    color= BLUE
    pygame.draw.line(screen,color,(posX,15),(posX,screen_height-15),line_width)
def draw_horizontal_winning_line(row):
    posY=row*sq_size+sq_size//2
    color= BLUE
    pygame.draw.line(screen,color,(15,posY),(screen_width-15,posY),line_width)
def draw_asc_diagonal():
    color= BLUE
    pygame.draw.line(screen,color,(15,screen_height-15),(screen_width-15,15),line_width)
def draw_desc_diagonal():
    color= BLUE
    pygame.draw.line(screen,color,(15,15),(screen_width-15,screen_height-15),line_width)
def check_win(player):
    for col in range(cols):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            draw_vertical_winning_line(col)
            return True
    for row in range(rows):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            draw_horizontal_winning_line(row)
            return True
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        draw_asc_diagonal()
        return True
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        draw_desc_diagonal()
        return True
    return False
def restart():
    screen.fill(GREEN)
    draw_lines()
    for row in range(rows):
        for col in range(cols):
            board[row][col]=0
player=1
game_over=False
draw_lines()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX=event.pos[0]
            mouseY=event.pos[1]
            clicked_row=mouseY//sq_size
            clicked_col=mouseX//sq_size
            if available_square(clicked_row,clicked_col):
                mark_square(clicked_row,clicked_col,player)
                if check_win(player):
                    game_over=True
                player=2 if player==1 else 1
                draw_figures()
                
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                restart()
                player=1
                game_over=False
    pygame.display.update()