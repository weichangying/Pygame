# Pygame 屏幕绘制机制

# pygame.display

* 用来控制 pygame 游戏的屏幕

* 有且只有一个屏幕

* 左上角坐标为 (0, 0)

* 以像素为单位

# 屏幕尺寸和模式

1）pygame.display.set_mode(size, flags)

* size 是元组 (width, height)

* flags 用来控制显示类型，可用 | 组合使用，常用标签：

  * pygame.RESIZABLE      窗口大小可调
    * .size[0]/event.w
    * .size[1]/event.h
  * pygame.NOFRAME       窗口没有边界
  * pygame.FULLSCREEN  窗口全屏

  注：改变类型时要注意改变相应的响应

2）pygame.display.Info()

产生一个显示信息对象 VideoInfo，表达当前屏幕的参数信息

常用参数：

* current_w
* current_h

# 窗口标题和图标

1）pygame.display.set_caption()

窗口标题（标题 小标题）

2）pygame.display.get_caption()

返回窗口标题、小标题

3）pygame.display.set_icon()

* 设置窗口图标效果

* 图标是一个 Surface 对象

# 窗口感知和刷新

1）pygame.display.get_active()

最小化返回 False，非最小化返回 True

2）pygame.display.flip()

重新绘制整个窗口

3）pygame.display.update()

仅绘制窗口中有变化的区域，比 .flip() 更快

