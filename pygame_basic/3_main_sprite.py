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

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\gmltjr\\Desktop\\작업물\\컴퓨터프로그래밍\\pygame_basic\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해줌
character_width = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)


# 이벤트 루프
running = True # 게임이 진행중?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중 X
            
    screen.blit(background, (0,0)) # 배경 그리기
    
    screen.blit(character,(character_x_pos, character_y_pos)) # 캐릭터 그리기기
    
    pygame.display.update() # 게임화면을 다시 그리기기
    
# pygame 종료
pygame.quit()