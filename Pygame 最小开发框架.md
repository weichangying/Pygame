# Pygame 最小开发框架

# 最小开发框架

```python
# 引入 pygame 和 sys

# 初始化 init 及设置

while True:
	# 获取事件并逐类响应

	# 刷新屏幕
```

## 极简开发框架
```python
# 引入及初始化

while True:
	# 事件及刷新
```

# 1、引入 pygame 和 sys

1）pygame

* Python 最经典的 2D 游戏开发第三方库，也支持 3D 游戏开发
* 适用于游戏逻辑验证、游戏入门、系统演示验证
* 是一种游戏开发引擎

2）sys

* 是 python 的标准库
* 提供 python 运行时环境变量的操控
* sys.exit( ) 用于结束游戏并退出
# 2、初始化 init 及设置
1）pygame.init()

对 pygame 内部各功能模块进行初始化创建及变量设置，默认调用

2）pygame.display.set_mode(size)

初始化显示窗口，size 是一个二值元组，窗口的宽度和高度

3）pygame.display.set_caption(title)

设置显示窗口的标题，title 是一个字符串

4）pygame.image.load(filename)

将 filename 路径下的图像载入游戏，支持 JPG、PNG 等 13 种常用图片格式

5）surface 对象

pygame 使用内部定义的 surface 对象表示所有载入的图像，其中 .get_rect() 方法返回一个覆盖图像的矩形 Rect 对象，如：

```python
ball = pygame.image.load("Ball.png")
ballrect = ball.get_rect()
```

Rect 对象有一些重要属性，例如：top, bottom, left, right 表示上下左右；width, height 表示宽度、高度
```python
ballrect.move(x, y) 
```
矩形移动一个偏移量 (x, y)，x y 为整数（单位为像素）

6）pygame.time.Clock()

创建一个 Clock 对象，用于操作时间

# 3、获取事件并逐类响应

1）pygame.event.get()

从 pygame 的事件队列中取出事件，并从队列中删除该事件。如：键盘按下

2）event.type

获得事件类型。如：pygame.QUIT 是退出事件常量

3）pagame.KEYDOWN

对键盘敲击的事件定义，键盘每个键对应一个具体定义

# 4、刷新屏幕

1）pygame.display.update()

对显示窗口进行更新，对有变化的区域进行绘制

2）screen.fill(color)

显示窗口背景填充为 color 颜色，采用 RGB 色彩体系

3）screen.blit(src, dest)

将一个图像绘制在另一个图像上，即将 src 绘制到 dest 位置上

4）clock.tick(framerate)

控制帧速度，即窗口刷新速度。如 clock.tick(100) 表示每秒钟 100 次帧刷新速度
