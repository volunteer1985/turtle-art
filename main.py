import random
from turtle import Turtle, Screen

colors = ["dark olive green", "medium slate blue", "red", "green", "cyan",
          "slate gray", "black", "gold"]
turns = [0, 90, 180, 270,]
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
        tortilla.color(random.choice(colors))
        draw_a_polygon(i, side)

def draw_random_walk(step_width, steps):
    tortilla.width(10)
    for _ in range(steps):
        tortilla.color(random.choice(colors))
        move_and_turn(step_width, random.choice(turns))




tortilla = Turtle()
tortilla.shape("turtle")
tortilla.color("deep pink")


#draw_multiple_polygons(75, 10)
draw_random_walk(20, 200)





my_screen = Screen()
my_screen.exitonclick()