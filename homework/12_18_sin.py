import turtle
import collections
import time

window = turtle.Screen()
window.tracer(0)
window.bgcolor(50 / 255, 50 / 255, 50 / 255)


#x轴
x=turtle.Turtle()
x.pensize(2)
x.color(255/255,255/255,255/255)
x.penup()
x.goto(-300, 0)
x.pendown()
x.goto(300, 0)
x.penup()


#y轴
y=turtle.Turtle()
y.left(90)
y.pensize(2)
y.color(255/255,255/255,255/255)
y.penup()
y.goto(0, -300)
y.pendown()
y.goto(0, 300)
y.penup()

radius = 100
angular_speed = 2

fps = 12  # Frames per second
time_per_frame = 1 / fps

main_dot = turtle.Turtle()
main_dot.pensize(5)
main_dot.shape("circle")
main_dot.color(0, 160 / 255, 193 / 255)
main_dot.penup()
main_dot.setposition(0, -radius)
main_dot.pendown()

#y轴追踪(sin)
vertical_dot = turtle.Turtle()
vertical_dot.shape("circle")
vertical_dot.color(248 / 255, 237 / 255, 49 / 255)
vertical_dot.penup()
vertical_dot.setposition(0,0)

vertical_plot = vertical_dot.clone()
vertical_plot.hideturtle()
start_x = int(vertical_plot.xcor())
# 获取从点位置到屏幕边缘的 x 值范围
x_range = range(start_x, window.window_width() // 2 + 1)
# 创建一个列表来存储要在每个值绘制的 y 值
# 标记为 x_range
vertical_values = collections.deque(None for _ in x_range)
# 可以填充此列表中的第一项
# 点的起始高度
vertical_values[0] = vertical_plot.ycor()

#x轴追踪（cos）
horizontal_dot = turtle.Turtle()
horizontal_dot.shape("circle")
horizontal_dot.color(242 / 255, 114 / 255, 124 / 255)
horizontal_dot.penup()
horizontal_dot.setposition(0,0)

horizontal_plot = horizontal_dot.clone()
horizontal_plot.hideturtle()
start_y = int(horizontal_plot.ycor())
y_range = range(start_x, window.window_width() // 2 + 1)
horizontal_values = collections.deque(None for _ in y_range)
horizontal_values[0] = horizontal_plot.ycor()

while True:
    frame_start = time.time()
    main_dot.circle(radius, angular_speed)

    vertical_dot.sety(main_dot.ycor())
    vertical_plot.clear()
    # 在开头添加新值，并删除最后一个值
    vertical_values.appendleft(vertical_dot.ycor())
    vertical_values.pop()
    # 绘制所有 y 值
    for x, y in zip(x_range, vertical_values):
        if y is not None:
            vertical_plot.setposition(x, y)
            vertical_plot.dot(5)

    horizontal_dot.sety(main_dot.xcor())
    horizontal_plot.clear()
    horizontal_values.appendleft(horizontal_dot.ycor())
    horizontal_values.pop()
    for y, x in zip(horizontal_values, y_range):
        if y is not None:
            horizontal_plot.setposition(x, y)
            horizontal_plot.dot(5)

    # Wait until minimum frame time reached
    while time.time() - frame_start < time_per_frame:
        pass
    window.update()