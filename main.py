import random
import turtle as t

def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

def draw_a_line(distance):
    tortilla.pendown()
    tortilla.forward(distance)

def draw_a_space(distance):
    tortilla.penup()
    tortilla.forward(distance)

def move_and_turn(distance, turn_degree):
    draw_a_line(distance)
    tortilla.setheading(turn_degree)


def draw_a_square(side_length):
    move_and_turn(side_length, 90)
    move_and_turn(side_length, 90)
    move_and_turn(side_length, 90)
    move_and_turn(side_length, 90)

def draw_a_dashed_line(dash_length, line_length):
    while line_length > dash_length:
        draw_a_line(dash_length)
        line_length -= dash_length
        draw_a_space(dash_length)
        line_length -= dash_length

def draw_a_polygon(corners, length):
    for i in range(corners):
        move_and_turn(length, 360 / corners)

def draw_multiple_polygons(up_to_angles, side):
    start_angles = 3
    for i in range(3, up_to_angles + 1):
        tortilla.color(get_random_color())
        draw_a_polygon(i, side)

def draw_random_walk(step_width, steps):
    turns = [0, 90, 180, 270, ]
    tortilla.width(20)
    for _ in range(steps):
        tortilla.color(get_random_color())
        move_and_turn(step_width, random.choice(turns))

def draw_spirograph(radius, tilt):
    for i in range(int(360 / tilt)):
        tortilla.color(get_random_color())
        tortilla.circle(radius)
        tortilla.left(tilt)





tortilla = t.Turtle()
t.colormode(255)
tortilla.shape("turtle")
tortilla.color("deep pink")


#draw_multiple_polygons(75, 10)
#draw_random_walk(20, 400)
draw_spirograph(100, 2)





my_screen = t.Screen()
my_screen.exitonclick()