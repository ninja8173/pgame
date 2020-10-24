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

#FPS (Frame per second)
clock = pygame.time.Clock()

#이미지 불러오기
cur_path = os.path.dirname(__file__)
img_path = os.path.join(cur_path, "imges")

background_img = pygame.image.load(os.path.join(img_path, "background.png"))
stage_img = pygame.image.load(os.path.join(img_path, "stage.png"))
stage_height = stage_img.get_rect().size[1]

character_img = pygame.image.load(os.path.join(img_path, "character.png"))
character_rect = character_img.get_rect().size
character_width = character_rect[0]
character_height = character_rect[1]
character_pos_x = screen_width // 2 - character_width // 2
character_pos_y = screen_height - stage_height - character_height
character_speed = 0

weapon_img = pygame.image.load(os.path.join(img_path, "weapon.png"))
weapon_width = weapon_img.get_rect().size[0]
weapon_pos_x = character_pos_x + character_width // 2 - weapon_width // 2
weapon_pos_y =character_pos_y
weapon_speed = 10
weapons = []

#게임 루프
running = True
while running:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                character_speed = 5
            elif event.key == pygame.K_LEFT:
                character_speed = -5
            elif event.key == pygame.K_SPACE:
                weapon_pos_x = character_pos_x + character_width // 2 - weapon_width // 2
                weapon_pos_y = character_pos_y
                weapons.append([weapon_pos_x, weapon_pos_y])
                #print(weapons)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_speed = 0

    character_pos_x = character_pos_x + character_speed
    if character_pos_x < 0 : character_pos_x = 0
    if character_pos_x > screen_width-character_width:
        character_pos_x = screen_width - character_width

    #무기 이동
    weapons = [[w[0], w[1]-10] for w in weapons]
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    #화면 출력
    screen.blit(background_img, (0, 0))
    for one in weapons:
        screen.blit(weapon_img, (one[0], one[1]))
    screen.blit(stage_img, (0, screen_height - stage_height))
    screen.blit(character_img, (character_pos_x, character_pos_y))

    #화면 업데이트
    pygame.display.update()

#파이게임 종료
pygame.quit()