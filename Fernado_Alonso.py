import pygame, sys
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.display.set_caption('Need for Speed')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
PLAYER_SIZE = 50
ENEMY_SIZE = 30
PLAYER_POS = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_SIZE]
ENEMY_COUNT = 5
PLAYER_SPEED = 10
ENEMY_SPEED = 3
enemy_list = []
score = 0
lives = 3 


for i in range(ENEMY_COUNT):
    enemy_pos = [random.randint(0, SCREEN_WIDTH - ENEMY_SIZE), random.randint(-SCREEN_HEIGHT - ENEMY_SIZE * 2, 0)]
    enemy_list.append(enemy_pos)
    
def draw_object():
    screen.fill(BLACK)
    # vẽ người chơi
    pygame.draw.rect(screen, WHITE, [PLAYER_POS[0], PLAYER_POS[1], PLAYER_SIZE, PLAYER_SIZE])
    # vẽ enemy
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, RED, [enemy_pos[0], enemy_pos[1], ENEMY_SIZE, ENEMY_SIZE])
        
def update_enemy():
    global score
    for i in range(len(enemy_list)):
        if enemy_list[i][1] < SCREEN_HEIGHT:
            enemy_list[i][1] += ENEMY_SPEED
        else:
            score += 1
            enemy_list[i][0] = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)
            enemy_list[i][1] = random.randint(-SCREEN_HEIGHT - ENEMY_SIZE * 2, 0)

def handle_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return True
    
    key = pygame.key.get_pressed()
    
    if key[pygame.K_LEFT] and PLAYER_POS[0] > 0:
        PLAYER_POS[0] -= PLAYER_SPEED
    if key[pygame.K_RIGHT] and PLAYER_POS[0] < SCREEN_WIDTH - PLAYER_SIZE:
        PLAYER_POS[0] += PLAYER_SPEED
    
    return False

def detect_collision(obj1_pos, obj2_pos):
    obj1_x, obj1_y = obj1_pos[0], obj1_pos[1]
    obj2_x, obj2_y = obj2_pos[0], obj2_pos[1]
    
    if (obj1_x >= obj2_x and obj1_x < (obj2_x + ENEMY_SIZE)) or (obj2_x >= obj1_x and obj2_x < (obj1_x + PLAYER_SIZE)):
        if (obj1_y >= obj2_y and obj1_y < (obj2_y + ENEMY_SIZE)) or (obj2_y >= obj1_y and obj2_y < (obj1_y + PLAYER_SIZE)):
            return True
    return False
def check_collision():
    global lives    
    enemies_to_reset = []
    for i in range(len(enemy_list)):
        enemy_pos = enemy_list[i]
        if detect_collision(PLAYER_POS, enemy_pos):
            lives -= 1 
            enemies_to_reset.append(i)    
        for i in range(len(enemy_list)):
            if i in enemies_to_reset:
               enemy_list[i][0] = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)
               enemy_list[i][1] = random.randint(-SCREEN_HEIGHT - ENEMY_SIZE * 2, 0)
    
game_over = False
while not game_over:
    game_over = handle_event()
    update_enemy()
    check_collision()
    if lives <= 0:
        game_over = True
    draw_object()
    font = pygame.font.SysFont("arial", 35)
    score_text = font.render("Score: " + str(score), True, GREEN)
    screen.blit(score_text, (10, 10))
    lives_text = font.render("Lives: " + str(lives), True, BLUE)
    screen.blit(lives_text, (10, 50))
    pygame.display.update()