#만들기

import random
import pygame

#화면 그리기
pygame.init()
SCREEN_WDIGHT = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WDIGHT,SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PYSNAKE")
clock = pygame.time.Clock()

#변수 초기화
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
CELL_SIZE = 40
COL_COUNT = SCREEN_WDIGHT//CELL_SIZE
ROW_COUNT =SCREEN_HEIGHT//CELL_SIZE

GAMEOVER = False
#점수 초기화
score = 0

#폰트 설정
score_font = pygame.font.SysFont("comicsans", 40)
gameover_font = pygame.font.SysFont("comicsans", 80)

#뱀 좌표 리스트
bodies = [(COL_COUNT//2, ROW_COUNT//2)]

LEFT,RIGHT,UP,DOWN=0,1,2,3
direction = DOWN


#먹이 10개 리스트 만들기
foods = []
#먹이 추가 함수 add_food 만들기
def add_food():
    while True:
        c_idx = random.randint(0, COL_COUNT-1)
        r_idx = random.randint(0,ROW_COUNT-1)
        f_pos = (c_idx, r_idx)
        if f_pos not in foods and f_pos not in bodies:
            foods.append(f_pos)
            break

for _ in range(10):
    add_food()
#게임 루프
while True:
    #키 처리
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

    c_idx, r_idx = head[0], head[1]
    if direction == LEFT and not GAMEOVER:
        c_idx -= 1
    elif direction == RIGHT and not GAMEOVER:
        c_idx += 1
    elif direction == DOWN and not GAMEOVER:
        r_idx += 1
    elif direction == UP and not GAMEOVER:
        r_idx -= 1

    head_pos = (c_idx, r_idx)
    #충돌 감지
    if head_pos in bodies or c_idx < 0 or c_idx >= COL_COUNT or r_idx < 0  or r_idx >= ROW_COUNT:
        GAMEOVER = True


    bodies.insert(0, head_pos)


    #먹이 먹기
    if head_pos in foods:
        foods.remove(head_pos)
        add_food()
        score += 10
    else:
        bodies.pop()



    screen.fill(BLACK)

    #격자 글기
    for c_idx in range(COL_COUNT):
        for r_idx in range(ROW_COUNT):
            rect = (c_idx*CELL_SIZE, r_idx*CELL_SIZE , CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)
    for one in bodies:
        rect = (one[0]*CELL_SIZE, one[1] *CELL_SIZE, CELL_SIZE, CELL_SIZE)
        if one == bodies[0]:
            pygame.draw.rect(screen, (120, 0, 0), rect)
        elif one == bodies[1]:
            pygame.draw.rect(screen, (255, 0, 0), rect)
        elif one == bodies[2]:
            pygame.draw.rect(screen, (255, 120, 0), rect)
        elif one == bodies[3]:
            pygame.draw.rect(screen, (255, 255, 0), rect)
        elif one == bodies[4]:
            pygame.draw.rect(screen, (255, 255, 120), rect)
        elif one == bodies[5]:
            pygame.draw.rect(screen, (255, 255, 255), rect)
        else:
            pygame.draw.rect(screen, (255, 255, 255), rect)

    for one in foods:
        rect = (one[0]*CELL_SIZE, one[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE )
        pygame.draw.rect(screen, GREEN, rect)

    #점수 출력
    score_img = score_font.render(f"SCORE:{score}", True, YELLOW)
    screen.blit(score_img, (10, 10))
    #게임오버출력
    if GAMEOVER:
        gover_img = gameover_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(gover_img,(SCREEN_WDIGHT//2 - gover_img.get_width()//2, SCREEN_HEIGHT//2))

    pygame.display.update()
    clock.tick(10)
#게임 종료
pygame.quit()