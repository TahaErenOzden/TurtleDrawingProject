import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Star Python Turtle")

turtle_instance = turtle.Turtle()


for i in range(5):
    turtle_instance.right(144)
    turtle_instance.forward(300)

turtle.done()