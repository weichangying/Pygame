# Pygame 事件处理机制

# pygame.event.EventType

* 事件本质上是一种封装后的数据类型（对象）
* EventType 是 pygame  的一个类，表示事件类型
* 事件类型只有属性，没有方法
* 用户可自定义新的事件类型

# 事件处理的重要函数

1、处理事件

1）pygame.event.get()

* 从事件队列中获得事件列表 (所有事件)

* 可以增加参数，获得某类或某些类事件：
  * pygame.event.get(type)
  * pygame.event.get(typelist)

2）pygame.event.poll()

* 从事件队列中获得一个事件
* 事件获取将从事件队列中删除
* 如果事件队列为空，则返回 event.NOEVENT

3）pygame.event.clear()

* 清空事件队列

* 可以增加参数，删除某类或某些类事件：
  * pygame.event.get(type)
  * pygame.event.get(typelist)

2、操作事件队列

1）pygame.event.set_blocked(type or typelist)

不允许某个或某类事件进到队列中

2）pygame.event.set_allowed(type or typelist)

运行某个或某类事件进到队列中

3）pygame.event.get_blocked(type)

某个事件类型是否被禁止，如是返回 True，否则返回 False

3、生成事件

1）pygame.event.post(Event)

* 产生一个事件，并将其放入事件队列
* 一般用于放置用户自定义事件 (pygame.USEREVENT)
* 也可以用于放置系统定义事件 ( 如鼠标键盘等)，给定参数

2）pygame.event.Event(type, dice)

* 创建一个给定类型的事件
* 其中，事件的属性和值采用字典类型复制，属性名采用字符串形式
* 如果创建已有事件，属性需要一致

# 键盘事件

1、pygame.event.KEYDOWN 和 pygame.event.KEYUP

* event.unicode  平台有关，不推荐
* event.key          常用名称（event.key.K_a）
* event.mod        按键修饰符的组合值（KMOD_ALT | KMOD_SHIFT）

# 鼠标事件

1、鼠标移动事件

pygame.event.MOUSEMOTION

* evnet.pos         鼠标当前坐标值 (x, y)
* event.rel           鼠标相对运动距离 (x, y)，相对于上次事件
* event.buttons 鼠标按钮状态 (a, b, c)，对应于鼠标的三个键

2、鼠标释放事件

pygame.event.MOUSEBUTTONUP

* event.pos        鼠标当前坐标值 (x, y)
* event.button  鼠标按下键编号 (0, 1, 2)

3、鼠标按下事件

pygame.event.MOUSEBUTTONDOWN

* event.pos        鼠标当前坐标值 (x, y)
* event.button  鼠标按下键编号 (0, 1, 2)