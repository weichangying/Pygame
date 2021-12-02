import pygame, sys

# 初始化及设置
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("最小开发框架测试")

# 事件和刷新
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.display.update()