import pygame
###########################################################
# 기본 초기화 ( 반드시 해야 하는 것들)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 640 # 가로
screen_height = 480 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀 설정
pygame.display.set_caption("Test Game")

# FPS
clock = pygame.time.Clock()
###########################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 폰트, 속도도 등)

# 배경 불러오기

# 이동할 좌표

# 이동 속도


# 적 enemy 캐릭터


# 폰트 정의

# 총 시간

# 시작 시간 정보보

# 이벤트 루프
running = True # 게임이 진행중?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    
    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중 X
    
    # 3. 게임 캐릭터 위치 정의
    
    # 4. 충돌 처리
    
    
        
    # 충돌 처리를 위한 rect 정보 업데이트
    
    
    
    # 충돌 체크
    
        
        
    # 5. 화면에 그리기
    
    
    
    pygame.display.update() # 게임화면을 다시 그리기기
    
# 대기 시간


# pygame 종료
pygame.quit()