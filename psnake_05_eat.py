#먹이 먹기
#꼬리가 길어지기
#먹이 추가하기

import pygame
import random

# 변수 초기화
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PYSNAKE")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (120, 120, 120)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

CELL_SIZE = 40
COL_COUNT = SCREEN_WIDTH//CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT//CELL_SIZE

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
direction = DOWN

#점수
score = 0

#글꼴 설정
score_font = pygame.font.SysFont("comicsans",40)

s_pos = (COL_COUNT//2, ROW_COUNT//2)
bodies = [s_pos]

def draw(g_x, g_y, color = WHITE, bovder = 0):
    one_rect = (g_x * CELL_SIZE, g_y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color,one_rect, bovder)
#먹이 생성 함수
def add_food():
    while True:
        c_idx = random.randint(0, COL_COUNT-1)
        r_idx = random.randint(0, ROW_COUNT-1)
        f_pos = (c_idx, r_idx)
        if f_pos not in bodies or f_pos not in foods:
            foods.append(f_pos)
            break
foods = []
for _ in range(10):
    add_food()
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            direction = LEFT
        if event.key == pygame.K_RIGHT:
            direction = RIGHT
        if event.key == pygame.K_UP:
            direction = UP
        if event.key == pygame.K_DOWN:
            direction = DOWN

    head = bodies[0]
    c_idx = head[0]
    r_idx = head[1]
    if direction == LEFT:
        c_idx -= 1
    elif direction == RIGHT:
        c_idx += 1
    elif direction == UP:
        r_idx -= 1
    elif direction == DOWN:
        r_idx += 1
    head_pos = (c_idx, r_idx)
    bodies.insert(0, head_pos)

    #먹이 충돌 채크
    if head_pos in foods:
        foods.remove(head_pos)
        score += 10
        add_food()

    else:
        bodies.pop()

    screen.fill(BLACK)

    for c_idx in range(COL_COUNT):
        for r_idx in range(ROW_COUNT):
            draw(c_idx,r_idx,GRAY, 1)

    for food in foods:
        draw(food[0], food[1], GREEN)

    for body in bodies:
        draw(body[0], body[1],BLUE)

    #점수 출력
    score_img = score_font.render(f"SCORE: {score}", True, YELLOW)
    screen.blit(score_img,(10,10))

    pygame.display.update()
    clock.tick(5)

pygame.quit()