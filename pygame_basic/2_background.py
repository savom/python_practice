import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 640 # 가로
screen_height = 480 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀 설정
pygame.display.set_caption("Test Game")

# 배경 불러오기
background = pygame.image.load("C:\\Users\\gmltjr\\Desktop\\작업물\\컴퓨터프로그래밍\\pygame_basic\\background.png")

# 이벤트 루프
running = True # 게임이 진행중?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중 X
            
    screen.blit(background, (0,0)) # 배경 그리기
    
    pygame.display.update() # 게임화면을 다시 그리기기
    
# pygame 종료
pygame.quit()