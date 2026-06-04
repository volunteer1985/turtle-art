import turtle
from turtle import Turtle, Screen

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


tortilla = Turtle()
tortilla.shape("turtle")
tortilla.color("deep pink")

draw_a_dashed_line(10, 100)






my_screen = Screen()
my_screen.exitonclick()