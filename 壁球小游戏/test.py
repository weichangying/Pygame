# 壁球小游戏
import pygame, sys

# 初始化
pygame.init()
size = width, height = 600, 400
speed = [1, 1]
BLACK = 0, 0, 0
screen = pygame.display.set_mode(size)  # 设置窗口大小
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("壁球小游戏")
ball = pygame.image.load("Ball.png")
ballrect = ball.get_rect()
fps = 300  # 每秒钟刷新 300 帧
fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:


    if pygame.display.get_active():
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
