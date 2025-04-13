import pygame
import random

###########################################################
# 기본 초기화 ( 반드시 해야 하는 것들)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 640 # 가로
screen_height = 480 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀 설정
pygame.display.set_caption("Quiz")

# FPS
clock = pygame.time.Clock()
###########################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 폰트, 속도도 등)

# 배경 불러오기
background = pygame.image.load("C:\\Users\\gmltjr\\Desktop\\작업물\\컴퓨터프로그래밍\\pygame_basic\\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\gmltjr\\Desktop\\작업물\\컴퓨터프로그래밍\\pygame_basic\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해줌
character_width = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)

# 이동할 좌표
to_x = 0
character_speed = 10

# 똥만들기
ddong = pygame.image.load("C:\\Users\\gmltjr\\Desktop\\작업물\\컴퓨터프로그래밍\\pygame_basic\\enemy.png")
ddong_size = ddong.get_rect().size 
ddong_width = ddong_size[0] 
ddong_height = ddong_size[1] 
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 10



# 폰트 정의


# 총 시간


# 시작 시간 정보보
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴

# 이벤트 루프
running = True # 게임이 진행중?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    
    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중 X
            
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed # to_x = to_x -5
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed # to_x = to_x + 5
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
        
                

    
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    ddong_y_pos += ddong_speed
    
    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)
    
    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos
    
    if character_rect.colliderect(ddong_rect):
        print("충돌했어여")
        running = False
    
    
    # 가로 경계값 처리
    
        
    #세로 경계값 처리리
    
        
    # 충돌 처리를 위한 rect 정보 업데이트
    
    
  
    # 충돌 체크
   
        
        
    # 5. 화면에 그리기
    
    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(character,(character_x_pos, character_y_pos)) # 캐릭터 그리기기
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))
    
    # 타이머 집어넣기
    # 경과 시간 계산
    
    # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시
    
    
    # 출력할 글자, True, 글자 색상
    
    
    #만약 시간이 0 이하면 게임 종료
    
    pygame.display.update() # 게임화면을 다시 그리기기
    
# 대기 시간
pygame.time.delay(2000) # 2초 정도 대기기

# pygame 종료
pygame.quit()