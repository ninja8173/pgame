import pygame
import os

#게임 환경설정
#캐릭터 이동
#무기 발사
#공 추가
#충돌 처리
#공 나누기
#메시지 출력

#파이게임 초기화
pygame.init()

screen_width = 640
screen_height = 480
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pypang!!")

#게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #화면 업데이트
    pygame.display.update()

#파이게임 종료
pygame.quit()