#먹이 그리기
#화면에 무작위로 먹이 10개 그리기
#먹이는 뱀 위치나 이전 먹이 위치에 그릴 수 없다.

import random
import pygame
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("pysnake")

GRAY = (120, 120, 120)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (250, 250, 250)

CELL_SIZE = 40
COL_COUNT = SCREEN_WIDTH//CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT//CELL_SIZE

bodies = [(COL_COUNT // 2, ROW_COUNT // 2)]

foods = []
for _ in range(10):
    while True:
        c_idx = random.randint(0, COL_COUNT-1)
        r_idx = random.randint(0, ROW_COUNT-1)
        f_pos = (c_idx, r_idx)
        #먹이의 위치가 뱀과 이전 먹이와 겹치는지 확인
        if f_pos not in bodies or f_pos not in foods:
            foods.append(f_pos)
            break

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    for c_idx in range(COL_COUNT):
        for r_idx in range(ROW_COUNT):
            one_rect = (c_idx*CELL_SIZE, r_idx*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, one_rect,1)
    #먹이 그리기
    for food in foods:
        f_rect = (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, WHITE, f_rect)


    for one in bodies:
        b_rect = (one[0]*CELL_SIZE,one[1]*CELL_SIZE,CELL_SIZE,CELL_SIZE)
        pygame.draw.rect(screen, BLUE, b_rect)

    pygame.display.update()

pygame.quit()
