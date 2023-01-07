import collections
import turtle

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

radius = 100
angular_speed = 2

main_dot = turtle.Turtle()
main_dot.pensize(5)
main_dot.shape("circle")
main_dot.color(0, 160 / 255, 193 / 255)
main_dot.penup()
main_dot.setposition(0, -radius)
main_dot.pendown()

vertical_dot = turtle.Turtle()
vertical_dot.shape("circle")
vertical_dot.color(248 / 255, 237 / 255, 49 / 255)
vertical_dot.penup()
vertical_dot.setposition(0,0)

vertical_plot = vertical_dot.clone()
vertical_plot.hideturtle()
start_x = int(vertical_plot.xcor())
# Get range of x-values from position of dot to edge of screen
x_range = range(start_x, window.window_width() // 2 + 1)
# Create a list to store the y-values to draw at each
# point in x_range.
vertical_values = collections.deque(None for _ in x_range)
# You can populate the first item in this list
# with the dot's starting height
vertical_values[0] = vertical_plot.ycor()

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
    main_dot.circle(radius, angular_speed)

    vertical_dot.sety(main_dot.ycor())
    vertical_plot.clear()
    # Add new value at the start, and delete last value
    vertical_values.appendleft(vertical_dot.ycor())
    vertical_values.pop()
    # Plot all the y-values
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

    window.update()
