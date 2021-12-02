# 壁球小游戏
import pygame, sys

# 初始化
pygame.init()
VInfo = pygame.display.Info()
size = width, height = VInfo.current_w, VInfo.current_h
speed = [1, 1]
BLACK = 0, 0, 0
screen = pygame.display.set_mode(size)  # 设置窗口大小
pygame.display.set_caption("壁球小游戏")
ball = pygame.image.load("Ball.png")
ballrect = ball.get_rect()
fps = 300  # 每秒钟刷新 300 帧
fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # 左右减速
                speed[0] = 0 if speed[0] == 0 else (abs(speed[0]) - 1) * int(speed[0] / abs(speed[0]))  # 值 * 符号
            elif event.key == pygame.K_RIGHT:  # 左右加速
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_DOWN:  # 上下减速
                speed[1] = 0 if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))
            elif event.key == pygame.K_UP:  # 上下加速
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_ESCAPE:
                sys.exit()

    ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(BLACK)
    screen.blit(ball, ballrect)
    pygame.display.update()
    fclock.tick(fps)  # 刷新事件间隔

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')
