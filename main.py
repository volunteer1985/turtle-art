import random
from turtle import Turtle, Screen

colors = ["dark olive green", "medium slate blue", "red", "green", "cyan",
          "slate gray", "black", "gold"]
def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def draw_a_line(distance):
    tortilla.pendown()
    tortilla.forward(distance)

def draw_a_space(distance):
    tortilla.penup()
    tortilla.forward(distance)

def move_and_turn_left(distance, turn_degree):
    draw_a_line(distance)
    tortilla.left(turn_degree)


def draw_a_square(side_length):
    move_and_turn_left(side_length, 90)
    move_and_turn_left(side_length, 90)
    move_and_turn_left(side_length, 90)
    move_and_turn_left(side_length, 90)

def draw_a_dashed_line(dash_length, line_length):
    while line_length > dash_length:
        draw_a_line(dash_length)
        line_length -= dash_length
        draw_a_space(dash_length)
        line_length -= dash_length

def draw_a_polygon(corners, length):
    for i in range(corners):
        move_and_turn_left(length, 360 / corners)

def draw_multiple_polygons(up_to_angles, side):
    color_code = 0
    start_angles = 3
    while up_to_angles >= start_angles:
        tortilla.color(colors[color_code])
        draw_a_polygon(start_angles, side)
        start_angles += 1
        color_code += 1




tortilla = Turtle()
tortilla.shape("turtle")
tortilla.color("deep pink")


draw_multiple_polygons(10, 50)





my_screen = Screen()
my_screen.exitonclick()