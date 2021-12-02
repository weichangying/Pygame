# Pygame 色彩与绘图机制

# 色彩表达

Color 类用于表达色彩，使用 RGB 或 RGBA 色彩模式，A 可选(透明度，0 全透明，255 不透明)

* Color(name)          如：Color("grey")
* Color(r, g, b, a)      如：Color(190, 190, 190, 255)
* Color(rgbvalue)    如：Color("#BEBEBEFF")

pygame.Color.r 获得 Color 类红色值

pygame.Color.a 获得不透明度值

pygame.Color.normalize 将 RGBA 各通道值归一到 0~1 之间

# 图形绘制

# pygame.draw

如：pygame.draw.rect(Surface, color, Rect, width = 0)

* Surface   矩形的绘制屏幕 
* color       矩形的绘制颜色
* Rect        矩形的绘制区域
* width = 0 绘制边缘的宽度，默认为 0，即填充图形

如圆形绘制后，用 Rect 类表示

# 文字绘制

pygame.freetype

不能直接 print，而是用像素根据字体点阵图绘制

要 import pygame.freetype

系统中的字体：

C:\Windows\Fonts

扩展名：

.ttf，.ttc

## Font 类

pygame.freetype.Font(file, size = 0)

* file  字体类型名称或路径
* size 字体大小

# Pygame 绘图机制原理精髓

## pygame.Surface

绘图层(绘图平层/图层)

* 用于表示图形、文字或图像的绘制效果
* 与当前屏幕主图层可以并列存在
* 如果不绘制在主图层上，则不会被显示

## pygame.Rect

矩形区域

* 对应于当前主图层的某个具体区域
* 相当于某个矩形区域的指针或标识信息
* 可以指定图层绘制在某个矩形区域中

由 pygame.display.set_mode() 生成了 Surface 对象：

```python
screen = pygame.display.set_mode(600, 400)
```

在主图层上绘制其他图层用 .blit() 方法

```python
screen.blit(ball, ballrect)
```

pygame.Surface --> pygame.Rect