from turtle import Turtle, Screen

def move_and_turn_left(distance, turn_degree):
    tortilla.forward(distance)
    tortilla.left(turn_degree)


def draw_a_square(side_length):
    move_and_turn_left(side_length, 90)
    move_and_turn_left(side_length, 90)
    move_and_turn_left(side_length, 90)
    move_and_turn_left(side_length, 90)


tortilla = Turtle()
tortilla.shape("turtle")
tortilla.color("deep pink")

draw_a_square(100)






my_screen = Screen()
my_screen.exitonclick()